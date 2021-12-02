<template>
  <div>
    <div id="Four_Type_Cmp" style="width: 1200px; height: 540px"></div>
  </div>
</template>
e
<script>
// import axios from "axios";
import * as echarts from "echarts";
var global_data = [];
var option;
var json_data = ["Date", "Number", "Type", "Country"];
export default {
  name: "CasesDeathsVaccineRecoveredCmp",
  props: {
    data_table: {
      type: Array,
      require: true,
    },
  },
  data() {
    return {
      name: "复兴组",
    };
  },
  watch: {
    data_table() {
      this.getData();
    },
  },
  mounted() {
    this.getData();
  },
  methods: {
    getData() {
      global_data = [];
      global_data.push(json_data);
      for (let i = this.$props.data_table.length - 1; i >= 0; i--) {
        global_data.push([
          this.$props.data_table[i]["date"].replace("T00:00:00Z", ""),
          this.$props.data_table[i]["overview"]["cases"]["nownum"],
          "cases",
          "Global",
        ]);
        global_data.push([
          this.$props.data_table[i]["date"].replace("T00:00:00Z", ""),
          this.$props.data_table[i]["overview"]["deaths"]["nownum"],
          "deaths",
          "Global",
        ]);
        global_data.push([
          this.$props.data_table[i]["date"].replace("T00:00:00Z", ""),
          this.$props.data_table[i]["overview"]["nowcases"]["nownum"],
          "nowcases",
          "Global",
        ]);
        global_data.push([
          this.$props.data_table[i]["date"].replace("T00:00:00Z", ""),
          this.$props.data_table[i]["overview"]["recovered"]["nownum"],
          "recovered",
          "Global",
        ]);
        // global_data.push([this.$props.data_table[i]['date'], this.$props.data_table[i]["overview"]['vaccine']['nownum'], 'vaccine', 'Global']);
      }
      this.mycharts();
    },
    mycharts() {
      let type_list = ["cases", "deaths", "nowcases", "recovered"];
      var seriesList = [];
      var datasetWithFilters = [];
      echarts.util.each(type_list, function (type) {
        datasetWithFilters.push({
          id: type,
          fromDatasetId: "dataset_raw",
          transform: {
            type: "filter",
            config: {
              and: [
                { dimension: "Number", gte: 0 },
                { dimension: "Type", "=": type },
                { dimension: "Country", "=": "Global" },
              ],
            },
          },
        });
        seriesList.push({
          type: "line",
          datasetId: type,
          showSymbol: false,
          endLabel: {
            show: true,
            formatter: function (params) {
              var mapping = {
                nowcases: "现有确诊",
                cases: "累计确诊",
                recovered: "累积治愈",
                deaths: "累积死亡",
              };
              return mapping[params.value[2]];
            },
          },
          emphasis: {
            focus: "series",
          },

          encode: {
            x: "Date",
            y: "Number",
            label: ["Type", "Number"],
            itemName: "Date",
            tooltip: ["Number"],
          },
        });
      });

      option = {
        dataset: [
          {
            id: "dataset_raw",
            source: global_data,
          },
        ].concat(datasetWithFilters),
        dataZoom: [
          {
            id: "dataZoomx",
            type: "slider",
            realtime: true,
            filterMode: "empty",
            start: 0,
            end: 1000,
            xAxisIndex: [0],
          },
          {
            id: "dataZoomY",
            type: "slider",
            realtime: true,
            filterMode: "empty",
            start: 0,
            end: 100,
            yAxisIndex: [0],
          },
        ],
        tooltip: {
          trigger: "axis",
          formatter: function (param) {
            var res = param[0].value[0] + "</br>";
            var mapping = {
              nowcases: "现有确诊",
              cases: "累计确诊",
              recovered: "累积治愈",
              deaths: "累积死亡",
            };
            for (var i in param) {
              res+=mapping[param[i].value[2]]+":"+param[i].value[1]+"</br>";
            }
            return res;
          },
        },
        xAxis: {
          type: "category",
          nameLocation: "middle",
        },
        yAxis: {
          name: "Number",
        },
        series: seriesList,
      };

      // 使用 macarons 主题
      let myChart = echarts.init(document.getElementById("Four_Type_Cmp"));
      myChart.clear();
      myChart.setOption(option);
      //图表自适应
    },
  },
};
</script>
<style scoped>
</style>
