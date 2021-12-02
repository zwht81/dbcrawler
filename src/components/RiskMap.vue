<template>
  <div class="RiskMapRoot">
<!--    <el-select v-model="country" placeholder="请选择">-->
<!--      <el-option-->
<!--        v-for="item in countries"-->
<!--        :key="item.value"-->
<!--        :label="item.label"-->
<!--        :value="item.value"-->
<!--      >-->
<!--        <span style="float: left">{{ item.label }}</span>-->
<!--        <span style="float: right; color: #8492a6; font-size: 13px">{{item.value}}</span>-->
<!--      </el-option>-->
<!--    </el-select>-->
    <china-map ref="ChinaMap"
               :medium_risk = "this.medium_risk"
               :high_risk = "this.high_risk"
               style="width: 600px; height: 650px"
               ></china-map>
    <div class="RiskMapSide">

      <div class="backButton" @click="reset" >中国</div>
      <div v-for="item in path"
           :key="item.mapName">
        <div class="backButton" @click="changeMap(item.mapName)">>>{{item.mapName}}</div>
      </div>
      <el-divider/>

      <h2 style="margin: 20px">中风险地区</h2>

        <div class="riskPlaces">
          <div v-for="item in medium_risk"
              :key="item.city">
            {{item.detail}}
          </div>
          <div v-if="medium_risk.length==0">无</div>
        </div>        

      <h2 style="margin: 20px">高风险地区</h2>

        <div class="riskPlaces">
          <div v-for="item in high_risk"
              :key="item.city">
            {{item.detail}}
          </div>
          <div v-if="high_risk.length==0">无</div>
        </div>

    </div>
  </div>
</template>

<script>
import ChinaMap from "./charts/ChinaMap";
// import risk_areas from "../data/map/json/list_all_high_risk_areas.json";
import api from "../commonApi.js";
import $ from "jquery";
import * as echarts from "echarts";

export default {
  name: "RiskMap",
  components: {
    ChinaMap,
  },
  created(){
    var risk_data;
    $.ajax({
      url: api.baseApi + "/data/list_all_high_risk_areas",
      type: 'GET',
      async: false,
      dataType: 'json',
      success: function (response) {
        risk_data = response.data;
        // console.log(risk_data);
      }

    });
    this.risk_data = risk_data;
    // console.log(this.risk_data);
    this.risk_data.forEach((item)=> {
      if(item.type === "中风险") {
        this.medium_risk.push({
          province: item.province,
          city: item.district,
          detail: item.name,
        })
      } else if(item.type === "高风险") {
        this.high_risk.push({
          province: item.province,
          city: item.district,
          detail: item.name,
        })
      }
    });
    // console.log(this.medium_risk);
    // console.log(this.high_risk);
  },
  mounted() {
    var _curr;
    var _this = this;
    this.myChart = echarts.init(document.getElementById("china-map"));
    this.myChart.on("click", function (param) {
      _curr = param.name;
      // console.log(_curr);
      _this.setCurr(_curr);
    });

  },
  data(){
    return {
      // countries:[
      //     {
      //         value:'China',
      //         label:'中国'
      //     }
      // ],
      myChart: "",
      curr: 'China',
      risk_data: [],
      medium_risk: [],
      high_risk: [],
      path: [],
    }
  },
  watch:{
      // country(newvalue){
      //   console.log("aaa");
      //     if(newvalue == '')return ;
      //     this.$refs.ChinaMap.changemap(newvalue);
      //   // console.log(risk_areas);
      // }
    curr() {
      // console.log(this.curr);
      this.updatePath(this.curr);
      console.log(this.path)
    },
    immediate: true
  },
  methods: {
    reset() {
      this.$refs.ChinaMap.backtochina();
      this.curr = "China";
    },
    updatePath(name) {
      if (name === 'China') {
        this.path = [];
        return;
      }
      var index = this.path.findIndex(function (item) {
        return item.mapName === name;
      });
      // console.log(index);
      if(index === -1)
        this.path.push({
          mapName: name,
        });
      else {
        // console.log(index);
        this.path = this.path.slice(0, index + 1);
      }
    },
    setCurr(value) {
      this.curr = value;
    },
    changeMap(name) {
      this.$refs.ChinaMap.changemap(name);
      this.setCurr(name);
    }
  },
};
</script>
<style scoped>
.RiskMapRoot {
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #4E6E62;

  padding-top: 20px;
  padding-bottom: 20px;
}
.RiskMapSide {
  display: flex;
  flex-direction: column;
  align-items: center;
  color: white;
  margin-left: 30px;
}
.backButton {
  white-space: nowrap;
  text-align: center;
  cursor: pointer;

  font-size: 17px;
  font-weight: 100;

  background-color:rgba(20, 20, 20, 0.2);
  color: white;

  border-radius: 30px;

  padding: 5px 15px 5px 15px;
  margin: 3px;
  margin-bottom: 50px;
}

.riskPlaces {

  border-radius: 30px;
  padding: 18px;
  background-color:rgba(20, 20, 20, 0.2);
}
</style>
