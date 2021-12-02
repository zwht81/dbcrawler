<template>
  <div class="GlobalAnalysisTabOverviewCmp">
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
      <el-select v-model="countries" multiple filterable style="width:200px;margin-right:20px;">
        <el-option
          v-for="item in list"
          :key="item.value"
          :label="item.label"
          :value="item.value"
        >
        </el-option>
      </el-select>
      <el-select v-model="type" style="width:200px;">
        <el-option
          v-for="item in options"
          :key="item.value"
          :label="item.label"
          :value="item.value"
        >
        </el-option>
      </el-select>
    </div>
    

      <div id="FourTypeSelector2" style="width: 1200px; height: 540px;">
      </div>

  </div>
</template>
<script>
var option;
import * as echarts from "echarts";

var json_data = ["Date", "Number", "Type", "Country"];
var global_data = [];
var region_data = [];
var countryen2zh = require("../data/utils/countryen2zh.json");
export default {
  name: "GlobalAnalysisTabOverviewCmp",
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
    this.getGlobalData();
    this.getRegionData();
    this.update(this.countries, this.type, this.date)
  },
  watch: {
    t2(newvalue) {
      this.timevalue = this.maxTimeNum - newvalue;
    },
    timevalue(newvalue) {
      this.date = this.data[newvalue]["date"];
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
    }
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
        var zhname = ""
       for (var j in countryen2zh) {
          if (countryen2zh[j]["value"] == enname) {
            zhname = countryen2zh[j]["label"];
            break;
          }
        }
        if(zhname == "")zhname = enname;
        this.list.push({
          value:enname,
          label:zhname
        })
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
    getGlobalData() {
      global_data = []
      global_data.push(json_data)
      for(let i = this.$props.data.length - 1; i >= 0; i--) {
        global_data.push([this.$props.data[i]['date'], this.$props.data[i]["overview"]['cases']['nownum'], 'cases', 'Global']);
        global_data.push([this.$props.data[i]['date'], this.$props.data[i]["overview"]['deaths']['nownum'], 'deaths', 'Global']);
        global_data.push([this.$props.data[i]['date'], this.$props.data[i]["overview"]['nowcases']['nownum'], 'nowcases', 'Global']);
        global_data.push([this.$props.data[i]['date'], this.$props.data[i]["overview"]['recovered']['nownum'], 'recovered', 'Global']);
      }
    },
    getRegionData() {
      region_data = []
      region_data.push(json_data)
      for(let i = this.$props.data.length - 1; i >= 0; i--) {
        var item = this.$props.data[i];


        for(let j = 0; j < item['detailed'].length; j++) {
          region_data.push([item['date'], item['detailed'][j]['cases'], 'cases', item['detailed'][j]['name']])
          region_data.push([item['date'], item['detailed'][j]['deaths'], 'deaths', item['detailed'][j]['name']])
          region_data.push([item['date'], item['detailed'][j]['nowcases'], 'nowcases', item['detailed'][j]['name']])
          region_data.push([item['date'], item['detailed'][j]['recovered'], 'recovered', item['detailed'][j]['name']])
        }
      }
    },
    update(now_countries, type, date) {
      var tmp_list = [];
      var countries_data = [];

      for(let j = 0; j < region_data.length; j++) {
        if(region_data[j][0] === date) {
          if(region_data[j][2] === type) {
            tmp_list.push(region_data[j])
          }
        }
      }
      for(let j = 0; j < now_countries.length; j++) {
        for(let k = 0; k < tmp_list.length; k++) {
          if(tmp_list[k][3] === now_countries[j])
            countries_data.push(tmp_list[k][1])
        }
      }

      option = {
        title: {
          text: '每日数据',
          subtext: "数据来源于网络"
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'shadow'
          }
        },
        // grid: {
        //   top: 10,
        //   bottom: 30,
        //   left: 150,
        //   right: 80
        // },
        xAxis: {
          // 表示用数据的最大值最为X轴最大值
          max: 'dataMax',
          type: 'value',
        },
        yAxis: {
          name: 'category',
          inverse: true,
          animationDuration: 300,
          animationDurationUpdate: 300,
          data: this.countries,
        },
        // animationDuration: 300,
        series: [{
          realtimeSort: true,
          type: 'bar',
          data: countries_data,
          label: {
            show: true,
            position: 'right',
            valueAnimation: true
          }
        }],
        legend: {
          show: true
        },

      };
      this.myChart.setOption(option, true);
    },
  },
};
</script>

<style scoped>
.GlobalAnalysisTabDetailedCmp {
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
