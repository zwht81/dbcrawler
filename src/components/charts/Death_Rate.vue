<template>
  <div>
    <div id="Death_rate" style="width: 450px; height: 300px;"> </div>
  </div>
</template>

<script>
// import axios from "axios";
import * as echarts from 'echarts';
//import dataTable from "@/data/samples/sample.json"
var option;
var json_data = [["Date", "Number", "Type"]];
export default{
  props:{
    data_table:{
      type:Object,
      required:true
    }
  },
  data() {
    return {
      name: "复兴组",
    };
  },
  created() {

  },
  mounted() {
    this.getGlobalData();
  },
  methods: {
    getGlobalData() {

      var data_Table = {
        'cases': this.$props.data_table['cases'],
        'deaths': this.$props.data_table['deaths'],
        'recovered': this.$props.data_table['recovered'],
      }
      for(var key in data_Table) {
        for(let i = 0; i < data_Table[key].length; i++) {
          var tmp = [];
          tmp[0] = data_Table[key][i].date;
          tmp[2] = key;
          let sum_value = 0.0;
          for (let j = 0; j < data_Table[key][i].value.length; j++) {
            sum_value += data_Table[key][i].value[j].value;
          }
          tmp[1] = sum_value.toString() + '.0';
          json_data.push(tmp);
        }
      }
      var num_data = (json_data.length - 1)/ 3;
      for (var i = 1; i <= num_data; i++) {
        json_data.push([json_data[i][0], parseFloat(json_data[i+num_data][1]) / parseFloat(json_data[i][1]), "death_rate"])
        json_data.push([json_data[i][0], parseFloat(json_data[i+2*num_data][1]) / parseFloat(json_data[i][1]), "heal_rate"])
      }
      this.mycharts();
    },
    getRegionData() {
    },
    mycharts(){
      option = {
        animation: 10000,
        dataset: [{
          id: 'dataset_raw',
          source: json_data
        },{
          id: 'death_rate',
          fromDatasetId: 'dataset_raw',
          transform: {
            type: 'filter',
            config: {
              and: [
                { dimension: 'Number', gte: 0.0},
                { dimension: 'Type', '=': 'death_rate' },
              ]
            }
          }
        },{
          id: 'heal_rate',
          fromDatasetId: 'dataset_raw',
          transform: {
            type: 'filter',
            config: {
              and: [
                { dimension: 'Number', gte: 0.0},
                { dimension: 'Type', '=': 'heal_rate' },
              ]
            }
          }
        }],
        title: {
          text: '死亡率/治愈率',
          textStyle: {
            color: "#fff",
          },
        },
        grid: {
          right: 140
        },
        tooltip: {
          order: 'valueDesc',
          trigger: 'axis'
        },
        xAxis: {
          type: 'category',
          nameLocation: 'middle'
        },
        yAxis: {
          name: 'Number'
        },
        series: [{
          type: 'line',
          datasetId: 'death_rate',
          showSymbol: false,
          endLabel: {
            show: true,
            formatter: function (params) {
              return params.value[2];
            }
          },
          encode: {
            x: 'Date',
            y: 'Number',
            label: ['Type', 'Number'],
            itemName: 'Date',
            tooltip: ['Number'],
          }
        }, {
          type: 'line',
          datasetId: 'heal_rate',
          showSymbol: false,
          endLabel: {
            show: true,
            formatter: function (params) {
              return params.value[2];
            }
          },
          encode: {
            x: 'Date',
            y: 'Number',
            label: ['Type', 'Number'],
            itemName: 'Date',
            tooltip: ['Number'],
          }
        },]
      };

      // 使用 macarons 主题
      let myChart = echarts.init(document.getElementById('Death_rate'));
      myChart.setOption(option)
      //图表自适应
      window.addEventListener("resize",function(){
        myChart.resize()  // myChart 是实例对象
      })
    },
  },
  watch: {

  },
};
</script>
<style scoped>

</style>
