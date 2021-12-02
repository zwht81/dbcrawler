<template>
  <div>
    <div id="main2"> </div>
  </div>
</template>

<script>
import axios from "axios";
import * as echarts from 'echarts';
// import data_table from '@/static/test.json'

var option;
var json_data = [["Data", "Doses", "Country"]];
var load = false;
export default{
  data() {
    return {
      name: "复兴组",
    };
  },
  created() {
    this.getChinaVaccine();
  },
  mounted() {
    // this.mycharts();
  },
  methods: {
    getChinaVaccine() {
      let formData = new FormData();
      // formData.append("author_id", this.authorId);
      let config = {
        headers: {"Content-Type": "multipart/form-data",},
      };
      var _this = this;
      axios.get(
          "https://disease.sh/v3/covid-19/vaccine/coverage/countries/China?lastdays=30&fullData=false",
          formData,
          config
      ).then(function (response1) {
            if (response1.status == 200) {
              for (var key in response1.data.timeline) {
                var tmpt = []
                tmpt[0] = key
                tmpt[1] = response1.data.timeline[key]
                tmpt[2] = "China"
                json_data.push(tmpt);
              }
              // console.log(json_data)
              _this.getUSAVaccine();

              // _this.relatedloaded = true;
            } else {
              // console.log("请求失败");
              // _this.fail()
            }
          });
    },
    getUSAVaccine() {
      let formData = new FormData();
      // formData.append("author_id", this.authorId);
      let config = {
        headers: {"Content-Type": "multipart/form-data",},
      };
      var _this = this;
      axios.get(
          "https://disease.sh/v3/covid-19/vaccine/coverage/countries/USA?lastdays=30&fullData=false",
          formData,
          config
      ).then(function (response2) {
        if (response2.status == 200) {
          // console.log(response2)
          for (var key in response2.data.timeline) {
            var tmpt = []
            tmpt[0] = key
            tmpt[1] = response2.data.timeline[key]
            tmpt[2] = "USA"
            json_data.push(tmpt);
          }
          load = true
          _this.mycharts();
          // console.log(json_data)
          // _this.relatedloaded = true;
        } else {
          console.log("请求失败");
          // console.log(response.data);
          // _this.fail()
        }
      });
    },
    mycharts(){
      if(load == true) {
        // console.log(load)
        // console.log(json_data)
        option = {
          dataset: [{
            id: 'dataset_raw',
            source: json_data
          }, {
            id: 'dataset_last_30days_of_China',
            fromDatasetId: 'dataset_raw',
            transform: {
              type: 'filter',
              config: {
                and: [
                  { dimension: 'Doses', gte: 10000 },
                  { dimension: 'Country', '=': 'China' }
                ]
              }
            }
          },{
            id: 'dataset_last_30days_of_USA',
            fromDatasetId: 'dataset_raw',
            transform: {
              type: 'filter',
              config: {
                and: [
                  { dimension: 'Doses', gte: 10000 },
                  { dimension: 'Country', '=': 'USA' }
                ]
              }
            }
          }],
          title: {
            text: '中美过去30天内疫苗接种剂数对比'
          },
          tooltip: {
            trigger: 'axis'
          },
          xAxis: {
            type: 'category',
            nameLocation: 'middle'
          },
          yAxis: {
            name: 'Doses'
          },
          series: [{
            type: 'line',
            datasetId: 'dataset_last_30days_of_China',
            showSymbol: false,
            endLabel: {
              show: true,
              formatter: function (params) {
                return params.value[2] + ': ' + params.value[1] / 1000 + "k";
              }
            },
            encode: {
              x: 'Data',
              y: 'Doses',
              label: ['Country', 'Doses'],
              itemName: 'Data',
              tooltip: ['Doses'],
            }
          }, {
            type: 'line',
            datasetId: 'dataset_last_30days_of_USA',
            showSymbol: false,
            endLabel: {
              show: true,
              formatter: function (params) {
                return params.value[2] + ': ' + params.value[1];
              }
            },
            encode: {
              x: 'Data',
              y: 'Doses',
              label: ['Country', 'Doses'],
              itemName: 'Data',
              tooltip: ['Doses'],
            }
          }]
        };
      }

      // console.log(data_table)
      // 使用 macarons 主题
      let myChart = echarts.init(document.getElementById("main2"), 'light');
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
#main2{
  width: 1000px;
  height: 800px;
}
</style>
