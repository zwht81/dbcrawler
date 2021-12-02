<template>
  <div>
    <div id="main"  > </div>
  </div>
</template>

<script>
// import axios from "axios";
import * as echarts from 'echarts';
import axios from "axios";
// import data_table from '@/static/test.json'

// var json_data = [["Data", "Doses", "Country"]];
// var load = false;x
var timeData = []
var vaccine_list = []
var new_cases_list = []

export default{
  data() {
    return {
      name: "复兴组",
    };
  },
  created() {
    this.getChinaVaccine()
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
            timeData.push(key);
            vaccine_list.push(response1.data.timeline[key])
          }
          _this.getChinaNewcases()
        } else {
          console.log("请求失败");
          // _this.fail()
        }
      });
    },
    getChinaNewcases() {
      let formData = new FormData();
      // formData.append("author_id", this.authorId);
      let config = {
        headers: {"Content-Type": "multipart/form-data",},
      };
      var _this = this;
      axios.get(
          "https://disease.sh/v3/covid-19/historical/China?lastdays=30",
          formData,
          config
      ).then(function (response1) {
        if (response1.status == 200) {
          // console.log(response1.data.timeline.cases)
          for(var key in response1.data.timeline.cases) {
            new_cases_list.push(response1.data.timeline.cases[key])
          }
          // console.log(new_cases_list);
          // console.log(json_data)
          _this.mycharts();
        } else {
          console.log("请求失败");
          // _this.fail()
        }
      });
    },
    mycharts(){
      // 时间点

      // if(load == true) {

        var option = {
          title: {
            text: '新增病例和疫苗接种对比关系',
            subtext: 'disease.sh',
            left: 'center'
          },
          tooltip: {
            trigger: 'axis',
            axisPointer: {
              animation: false
            }
          },
          legend: {
            data: ['疫苗接种', '新增病例'],
            left: 10
          },
          toolbox: {
            feature: {
              dataZoom: {
                yAxisIndex: 'none'
              },
              restore: {},
              saveAsImage: {}
            }
          },
          axisPointer: {
            link: {xAxisIndex: 'all'}
          },
          dataZoom: [
            {
              show: true,
              realtime: true,
              start: 30,
              end: 70,
              xAxisIndex: [0, 1]
            },
            {
              type: 'inside',
              realtime: true,
              start: 30,
              end: 70,
              xAxisIndex: [0, 1]
            }
          ],
          grid: [{
            left: 50,
            right: 50,
            height: '35%'
          }, {
            left: 50,
            right: 50,
            top: '55%',
            height: '35%'
          }],
          xAxis: [
            {
              type: 'category',
              boundaryGap: false,
              axisLine: {onZero: true},
              data: timeData
            },
            {
              gridIndex: 1,
              type: 'category',
              boundaryGap: false,
              axisLine: {onZero: true},
              data: timeData,
              position: 'top'
            }
          ],
          yAxis: [
            {
              name: '疫苗接种(剂)',
              type: 'value',
              max: 1200000000,
              min: 800000000
            },
            {
              gridIndex: 1,
              name: '新增病例(例)',
              type: 'value',
              inverse: true,
              min: 103000,
              max: 104000
            }
          ],
          series: [
            {
              name: '疫苗接种',
              type: 'line',
              symbolSize: 8,
              hoverAnimation: false,
              data: vaccine_list
            },
            {
              name: '新增病例',
              type: 'line',
              xAxisIndex: 1,
              yAxisIndex: 1,
              symbolSize: 8,
              hoverAnimation: false,
              data: new_cases_list
            }
          ]
        };

        // console.log(data_table)
        // 使用 macarons 主题
        let myChart = echarts.init(document.getElementById("main"), 'light');
        myChart.setOption(option)
        //图表自适应
        window.addEventListener("resize",function(){
          myChart.resize()  // myChart 是实例对象
        })
      // }
    },
  },

  watch: {

  },
};
</script>
<style scoped>
#main{
  width: 1000px;
  height: 800px;
}
</style>
