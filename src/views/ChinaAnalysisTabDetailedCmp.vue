<template>
  <div class="ChinaAnalysisTabDetailedCmp">
    <div class="topselector">
       <div class="TimeLine">
      <el-date-picker
        class="datepicker"
        v-model="date"
        type="date"
        value-format="yyyy-MM-ddT00:00:00Z"
        format="yyyy 年 MM 月 dd 日"
      >
      </el-date-picker>
      <el-slider
        class="slider"
        v-model="t2"
        :max="maxTimeNum"
        :show-tooltip="false"
      ></el-slider>
    </div>
      <el-select
        v-model="countries"
        multiple
        filterable
        style="width: 200px; margin-right: 20px"
      >
        <el-option
          v-for="item in list"
          :key="item.value"
          :label="item.label"
          :value="item.value"
        >
        </el-option>
      </el-select>
      <el-select v-model="type" style="width: 200px">
        <el-option
          v-for="item in options"
          :key="item.value"
          :label="item.label"
          :value="item.value"
        >
        </el-option>
      </el-select>
    </div>

   
    <div id="FourTypeSelector2" style="width: 1200px; height: 540px"></div>
  </div>
</template>
<script>
import * as echarts from "echarts";

var region_data = [];
var option;
var json_data = ["Date", "Number", "Type", "Country"];
var provinceen2zh = require("../data/utils/provinceen2zh.json");
export default {
  name: "ChinaAnalysisTabDetailedCmp",
  props: {
    data: {
      type: Array,
      required: true,
    },
  },
  mounted() {
    this.myChart = echarts.init(document.getElementById("FourTypeSelector2"));
    this.loadtimeline();
    this.loadlist(); //区域列表
    this.dataloaded = true;
    this.getRegionData();
  },
  watch: {
    t2(newvalue) {
      this.timevalue = this.maxTimeNum - newvalue;
    },
    timevalue(newvalue) {
      this.date = this.data[newvalue]["date"];
      this.loadporpsdata();
      this.t2 = this.maxTimeNum - this.timevalue;
    },
    date(newvalue, oldvalue) {
      for (var item in this.data) {
        if (this.data[item]["date"] == newvalue) {
          this.update(this.countries, this.type, newvalue);
          this.timevalue = Number(item);
          return;
        }
      }
      this.date = oldvalue;
    },
    countries(newvalue) {
      this.update(newvalue, this.type, this.date);
    },
    type(newvalue) {
      this.update(this.countries, newvalue, this.date);
    },
    data() {
      this.list = [];
      this.countries = [];
      this.loadtimeline();
      this.loadlist(); //区域列表
      this.dataloaded = true;
      this.getRegionData();
    },
  },
  data() {
    return {
      date: "",
      t2: 0,
      timevalue: 0,
      maxTimeNum: 0, //const
      data_table: [],
      dataloaded: false,
      options: [
        {
          value: "nowcases",
          label: "现有确诊",
        },
        {
          value: "cases",
          label: "累积确诊",
        },
        {
          value: "deaths",
          label: "累积死亡",
        },
        {
          value: "recovered",
          label: "累积治愈",
        },
      ],
      type: "nowcases",
      countries: [],
      list: [],
      mychart: "",
    };
  },
  methods: {
    loadlist() {
      var detailed = this.$props.data[0]["detailed"];
      for (var i in detailed) {
        var enname = detailed[i]["name"];
        var zhname = provinceen2zh[enname];
        if (zhname == undefined) {
          //说明name就是中文
          zhname = enname;
          enname = zhname;
        }
        this.list.push({
          value: enname,
          label: zhname,
        });
      }
    },
    loadtimeline() {
      this.maxTimeNum = this.$props.data.length - 1;
      this.t2 = this.maxTimeNum;
      this.date = this.$props.data[this.timevalue]["date"];
      this.loadporpsdata();
    },
    loadporpsdata() {
      this.data_table = this.$props.data[this.timevalue]["detailed"];
    },
    getRegionData() {
      region_data = [];
      region_data.push(json_data);
      for (let i = this.$props.data.length - 1; i >= 0; i--) {
        var item = this.$props.data[i];
        for (let j = 0; j < item["detailed"].length; j++) {
          var enname = item["detailed"][j]["name"];
          var zhname = provinceen2zh[enname];
          if (zhname == undefined) {
            //说明name就是中文
            zhname = enname;
            enname = zhname;
          }

          region_data.push([
            item["date"],
            item["detailed"][j]["cases"],
            "cases",
            zhname,
          ]);
          region_data.push([
            item["date"],
            item["detailed"][j]["deaths"],
            "deaths",
            zhname,
          ]);
          region_data.push([
            item["date"],
            item["detailed"][j]["nowcases"],
            "nowcases",
            zhname,
          ]);
          region_data.push([
            item["date"],
            item["detailed"][j]["recovered"],
            "recovered",
            zhname,
          ]);
        }
      }
    },
    update(now_countries, type, date) {
      var tmp_list = [];
      var countries_data = [];
      var tmp_list_countries = [];
      for (let i = 0; i < now_countries.length; i++) {
        var enname = now_countries[i];
        var zhname = provinceen2zh[enname];
        if (zhname == undefined) {
          //说明name就是中文
          zhname = enname;
          enname = zhname;
        }
        tmp_list_countries.push(zhname);
      }

      for (let j = 0; j < region_data.length; j++) {
        if (region_data[j][0] === date) {
          if (region_data[j][2] === type) {
            tmp_list.push(region_data[j]);
          }
        }
      }
      for (let j = 0; j < tmp_list_countries.length; j++) {
        for (let k = 0; k < tmp_list.length; k++) {
          if (tmp_list[k][3] === tmp_list_countries[j])
            countries_data.push(tmp_list[k][1]);
        }
      }
      var mapping = {
        nowcases:"现有确诊",
        cases:"累计确诊",
        deaths : "累计死亡",
        recovered:"累计治愈"
      }
      option = {
        title: {
          text: "每日数据",
          subtext: "数据来源于网络",
        },
        tooltip: {
          trigger: "axis",
          axisPointer: {
            type: "shadow",
          },
        },
        // grid: {
        //   top: 10,
        //   bottom: 30,
        //   left: 150,
        //   right: 80
        // },
        xAxis: {
          // 表示用数据的最大值最为X轴最大值
          max: "dataMax",
          type: "value",
        },
        yAxis: {
          name: "区域",
          inverse: true,
          animationDuration: 300,
          animationDurationUpdate: 300,
          data: tmp_list_countries,
        },
        // animationDuration: 300,
        series: [
          {
            realtimeSort: true,
            name: mapping[type],
            type: "bar",
            data: countries_data,
            label: {
              show: true,
              position: "right",
              valueAnimation: true,
            },
          },
        ],
        legend: {
          show: false,
        },
      };
      this.myChart.setOption(option, true);
    },
  },
};
</script>

<style scoped>
.ChinaAnalysisTabDetailedCmp {
  display: flex;
  flex-direction: column;
}
.topselector {
  display: flex;
  justify-content: flex-end;
}
.TimeLine {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-right: 20px;
}
.slider {
  margin-left: 20px;
  width: 400px;
}
</style>
