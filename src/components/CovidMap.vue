<template>
  <div class="CovidMapRoot">

    <i class="el-icon-loading" v-if="!dataloaded"> </i>
    <!-- left side -->
    <div class="CovidMap" v-if='dataloaded'>
      <main-map
        ref="MainMap"
        :country="this.country"
        :type="type"
        :data="mapData"
      ></main-map>

      <div
        style="
          width: 500px;
          display: flex;
          justify-content: space-between;
          margin-top: 15px;
        "
      >
        <SelectBarForCovidMap
          :buttons="TypeButtons"
          style="margin-left: 120px"
        />

        <el-select v-model="country" placeholder="请选择" size="small">
          <el-option
            v-for="item in countries"
            :key="item.value"
            :label="item.label"
            :value="item.value"
          >
            <span style="float: left">{{ item.label }}</span>
            <span style="float: right; color: #8492a6; font-size: 13px">{{
              item.value
            }}</span>
          </el-option>
        </el-select>
      </div>

      <el-slider
        v-model="timevalue"
        :max="maxTimeNum"
        :format-tooltip="formatTime"
        style="margin-top: 20px"
      ></el-slider>

      <el-radio-group size="medium">
        <el-button
          class="timeButton"
          type="text"
          icon="el-icon-caret-left"
          @click="timeMinus"
        ></el-button>
        <el-button
          class="timeButton"
          type="text"
          icon="el-icon-video-play"
          size="medium"
          @click="timePlayStart"
        ></el-button>
        <el-button
          class="timeButton"
          type="text"
          icon="el-icon-caret-right"
          size="medium"
          @click="timeAdd"
        ></el-button>
      </el-radio-group>
    </div>

    <!-- right side -->

    <div class="CovidMapTables" v-if='dataloaded'>
      <div class="countryshow">{{ countryData }}</div>
      <div style="display: flex; justify-content: center; align-items: center">
        <el-autocomplete
          class="inline-input"
          v-model="searchinput"
          :fetch-suggestions="querySearch"
          placeholder="请输入国家"
          @select="handleSelect"
          size="small"
        >
          <template slot-scope="{ item }">
            <span style="float: left">{{ item.label }}</span>
            <span style="float: right; color: #8492a6; font-size: 13px">{{
              item.value
            }}</span>
          </template></el-autocomplete
        >

        <i class="el-icon-search" @click="search()"></i>
      </div>

      <time-show :time="timeData" style="margin-top: 5px"></time-show>
      <map-top-show
        :data="maptopshowData"
        style="margin-bottom: 10px"
      ></map-top-show>

      <div class="mapDown">
        <SelectBarForCovidMap :buttons="buttons" style="margin-bottom: 20px" />
        <map-table :data="tableData" v-show="showTable"></map-table>
        <cases-deaths-vaccine-recovered-cmp
          :data_table="data"
          v-show="showChart"
        ></cases-deaths-vaccine-recovered-cmp>
        <death-rate :data_table="data" v-show="showRate"></death-rate>
      </div>
    </div>
  </div>
</template>
<script>
import MainMap from "./charts/MainMap.vue";
import MapTable from "./charts/MapTable.vue";
import MapTopShow from "./common/MapTopShow.vue";
import TimeShow from "./common/TimeShow.vue";
import CasesDeathsVaccineRecoveredCmp from "./charts/Cases_Deaths_Vaccine_Recovered_Cmp.vue";
import SelectBarForCovidMap from "../components/common/SelectBarForCovidMap.vue";
import DeathRate from "../components/charts/Death_Rate.vue";
var countrymapping = require("../data/utils/countries.json");

import api from "../commonApi.js";
//var sampledata = require("../data/samples/sample.json");
export default {
  name: "CovidMap",
  components: {
    MainMap,
    MapTable,
    MapTopShow,
    TimeShow,
    CasesDeathsVaccineRecoveredCmp,
    SelectBarForCovidMap,
    DeathRate,
  },
  data() {
    return {
      countries: [],
      country: "World",
      type: "cases",
      timevalue: 0,
      searchinput: "",
      data: {},
      dataloaded: false, //数据是否加载完成，控制所有组件的加载
      TypeButtons: ['确诊','死亡','治愈','接种'],
      buttons: ['table', 'chart','rate'],
      showTable: true,
      showRate: false,
      showChart: false,
    };
  },
  watch: {
    country(newvalue, oldvalue) {
      if (newvalue == oldvalue || newvalue == "") return;
      this.countryChange(newvalue);
    },
  },
  mounted() {
    this.countries = countrymapping;
    this.loadWorldData();
    // this.data = sampledata;
    // this.timevalue = this.maxTimeNum;
    // this.dataloaded = true;
  },
  computed: {
    typeName: {
      //控制显示数据类别get set function
      get: function () {
        var mapping = {
          cases: "确诊",
          deaths: "死亡",
          recovered: "治愈",
          vaccine: "接种",
        };
        return mapping[this.type];
      },
      set: function (value) {
        var mapping = {
          确诊: "cases",
          死亡: "deaths",
          治愈: "recovered",
          接种: "vaccine",
        };
        this.type = mapping[value];
      },
    },
    maxTimeNum() {
      //滑块的最大值
      return this.data["cases"].length - 1;
    },
    mapData() {
      // 给地图返回的当前类别当前区域的数据
      return this.data[this.type][this.timevalue]["value"];
    },
    tableData() {
      //给表格的数据
      var res = [];
      var len = this.data[this.type][this.timevalue]["value"].length;
      for (var i = 0; i < len; i++) {
        res.push({
          region: this.data["cases"][this.timevalue]["value"][i]["name"],
          cases: this.data["cases"][this.timevalue]["value"][i]["value"],
          deaths: this.data["deaths"][this.timevalue]["value"][i]["value"],
          recovered:
            this.data["recovered"][this.timevalue]["value"][i]["value"],
          vaccine: this.data["vaccine"][this.timevalue]["value"][i]["value"],
        });
      }
      return res;
    },
    maptopshowData() {
      //给topshow的数据，包括累积和新增的当前总数
      var res = {};
      for (var key in this.data) {
        var reslist = [];
        reslist.push(this.data[key][this.timevalue]["value"]);
        if (this.timevalue != 0)
          reslist.push(this.data[key][this.timevalue - 1]["value"]);
        res[key] = reslist;
      }
      return res;
    },
    timeData() {
      // 给时间显示器的数据
      return this.formatTime();
    },
    countryData() {
      //显示当前地图名称
      for (var i in this.countries) {
        if (this.countries[i]["value"] == this.country)
          return this.countries[i]["label"];
      }
      return "";
    },
  },
  methods: {
    countryChange(name) {
      //全局地图改变触发的方法
      this.$refs.MainMap.changemap(name);
      this.changeData(name);
    },
    changeCountry(name) {
      //被其他组件修改当前地图的方法
      this.country = name;
    },
    formatTime() {
      // 滑块的时间显示控制
      return this.data["cases"][this.timevalue]["date"];
    },
    changeData(name) {
      //改变地图数据，需要重新请求
      if (name == "World") {
        this.loadWorldData();
      } else {
        this.loadCountryData();
      }
    },
    loadWorldData() {
      var _this = this;
      this.$axios
        .get(api.baseApi + "/data/list_all_covid_cdrv_response")
        .then(function (response) {
          if (response.data.success) {
            _this.data = response.data.data;
            _this.timevalue = _this.maxTimeNum;
            _this.dataloaded = true;
          }
        });
    },
    loadCountryData(){
      var _this = this;
      let formData = new FormData();
      console.log(this.country);
      formData.append("province",this.country);
      this.$axios
        .post(api.baseApi + "/data/list_all_covid_cdrv_response_province",formData)
        .then(function (response) {
          if (response.data.success) {
            _this.data = response.data.data;
            _this.dataprocessing();
            _this.timevalue = _this.maxTimeNum;
            _this.dataloaded = true;
          }
        });
    },
    dataprocessing(){//第一次迭代的数据问题处理
      var key = ["cases","deaths","recovered","vaccine"];
      var res = {}
      for(var i in key){
        var type = key[i];
        var list = [];
        for(var item in this.data[type]){
          
          var outres = {
            date:this.data[type][item]["date"]
          };
          var value = JSON.parse(this.data[type][item]["value"]);
          var outvalue = [];
          for(var j in value){
            var temp = {}
            temp["name"] = j;
            temp["value"] = value[j];
            outvalue.push(temp);
            //console.log(outvalue);
          }
          outres["value"] = outvalue;
          list.push(outres);
        }
        res[type] = list;
      }
      this.data = res;
      return ;
    },
    querySearch(queryString, cb) {
      var countries = this.countries;
      var results = queryString
        ? countries.filter(function (val) {
            return (
              val.value.toLowerCase().indexOf(queryString.toLowerCase()) !=
                -1 || val.value.indexOf(queryString) != -1
            );
          })
        : countries;
      cb(results);
    },
    handleSelect(item) {
      this.changeCountry(item.value);
    },
    timeAdd() {
      if (this.timevalue + 1 > this.maxTimeNum) return;
      this.timevalue++;
    },
    timeMinus() {
      if (this.timevalue == 0) return;
      this.timevalue--;
    },
    timePlayStart() {
      let _this = this;
      if (this.timevalue + 1 > this.maxTimeNum) return;
      this.timevalue++;
      setTimeout(function () {
        _this.timePlayStart();
      }, 2000);
    },
    selected(index, differkey) {
      if (differkey == "table") {
        switch (index) {
          case 0:
            this.showTable = true;
            this.showRate = false;
            this.showChart = false;
            break;
          case 1:
            this.showTable = false;
            this.showChart = true;
            this.showRate = false;
            break;
          case 2:
            this.showTable = false;
            this.showChart = false;
            this.showRate = true;
        }
      } else if (differkey == "确诊") {
        switch (index) {
          case 0:
            this.type = "cases";
            break;
          case 1:
            this.type = "deaths";
            break;
          case 2:
            this.type = "recovered";
            break;
          case 3:
            this.type = "vaccine";
            break;
        }
      }
    },
    search() {
      console.log("search");
    },
  },
};
</script>

<style>
.CovidMapRoot {
  background-color: #575551;

  display: flex;
  justify-content: center;
  align-items: center;

  height: 680px;
}
.CovidMap {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin-top: 20px;
}
.CovidMapTables {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin-left: 80px;
  margin-top: 10px;
}
.CovidMapRoot .el-radio-button__orig-radio:checked + .el-radio-button__inner {
  background-color: #686562 !important;
  border-color: #c7c7c7 !important;
  box-shadow: -1px 0 0 0 #bfbfbf !important;
}
.CovidMapRoot .el-radio-button:last-child .el-radio-button__inner {
  border-radius: 0 20px 20px 0 !important;
}
.CovidMapRoot .el-radio-button:first-child .el-radio-button__inner {
  border-radius: 20px 0 0 20px !important;
}
.CovidMapRoot .el-input__inner {
  border-radius: 20px !important;
}
.CovidMapRoot .el-slider__button {
  border: 2px solid #a1a1a1;
}
.CovidMapRoot .el-slider__runway {
  width: 300px;
}
.CovidMapRoot .el-slider__bar {
  background-color: #cacaca;
}
.CovidMapRoot .timeButton {
  font-size: 30px;
  color: #cacaca;
}
.countryshow {
  /* outline:#00ff00 dotted thick; */
  white-space: nowrap;
  text-align: center;

  font-size: 15px;
  font-weight: bold;

  background-color: rgba(20, 20, 20, 0.2);
  color: white;

  border-radius: 30px;

  padding: 5px 15px 5px 15px;
  margin-bottom: 8px;
}
.mapDown {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
.el-icon-search {
  color: white;
  font-size: 23px;
  font-weight: bold;
  margin-left: 10px;
  cursor: pointer;
}
.el-icon-loading {
  color: white;
  font-size: 40px;
  font-weight: 1000;
}
</style>
