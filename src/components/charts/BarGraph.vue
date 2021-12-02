<template>
  <div>
    <div class="proCharts" ref='charts'></div>
  </div>
</template>

<script>
import axios from "axios";
// 引入基本模板
// import echarts from "echarts";
let echarts = require('echarts/lib/echarts');
// 引入柱状图组件
require('echarts/lib/chart/bar');
// 引入提示框和title组件
require('echarts/lib/component/tooltip');
require('echarts/lib/component/title');

import { LegendComponent } from 'echarts/components';
echarts.use([LegendComponent]);
import { GridComponent } from 'echarts/components';
echarts.use([GridComponent]);
import { LineChart } from 'echarts/charts';
echarts.use([LineChart]);


export default{
  data() {
    return {
      name: "复兴组",
      ROOT_PATH: 'https://cdn.jsdelivr.net/gh/apache/echarts-website@asf-site/examples',
      option:{
        color:['rgb(8,252,7)','rgb(255,168,0)',],
        title: {
          text: ''
        },
        tooltip: { //提示框
          trigger: 'axis',
        },
        legend: {//图例的类型
          icon:'roundRect',//图例icon图标
          data: [
            {
              name:"上年",
              textStyle: {
                color: '#fff'
              }

            },{
              name:"本年",
              textStyle: {
                color: '#fff'
              }
            },
          ],

        },
        grid: {
          left: '3%',
          right: '4%',
          bottom: '3%',
          top:'17%',
          containLabel: true //grid区域是否包含坐标轴的刻度标签
        },
        xAxis: {
          type: 'category', //坐标轴类型。
          boundaryGap: false, //坐标轴两边留白策略
          data: ['1月', '2月', '3月', '4月', '5月', '6月', '7月','8月','9月','10月','11月','12月'],
          axisLabel: {//坐标轴刻度标签的相关设置
            interval:0,
            textStyle: {
              color: '#fff',
              fontSize :10
            },
          },
          axisLine:{//坐标轴轴线相关设置
            show :true,
            lineStyle:{
              color:'rgb(2,121,253)'
            }
          },
          axisTick:{ //坐标轴刻度相关设置。
            show :false,
          }
        },
        yAxis: {
          type: 'value',
          axisLabel: { //x轴的坐标文字
            show: true,
            textStyle: {
              color: '#fff' //文字的颜色
            },

          },
          max:100,//最大值100
          axisLine:{//坐标轴轴线相关设置
            show :true,
            lineStyle:{
              color:'rgb(2,121,253)'
            }
          },
          axisTick:{ //坐标轴刻度相关设置。
            show :false,
          },
          splitLine:{  //坐标在grid区域的分割线
            // eslint-disable-next-line no-irregular-whitespace
            lineStyle: { //设置分割线的样式(图表横线颜色)
              color: ['#153a8a']
            }
          }
        },
        series: [
          {
            name: '上年',
            type: 'line',
            data: [10,20,30,50,50,10,50,60,10,50,10,30],
            lineStyle:{
              color:'rgb(8,252,7)'  //线的颜色
            }
          },
          {
            name: '本年',
            type: 'line',
            data: [20,20,30,50,50,10,50,20,30,50,50,30],
            lineStyle:{
              color:'rgb(255,168,0)' //线的颜色
            }
          }
        ]
      },
    };
  },
  mounted() {
    // this.getChinaVaccine();
    this.mycharts();
  },
  methods: {
    getChinaVaccine() {
      console.log(1);
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
      )
          .then(function (response) {
            console.log(response)
            console.log(response.status)
            if (response.status == 200) {
              _this.name = response.data.timeline
              // _this.relatedloaded = true;
            } else {
              // console.log("请求失败");
              // console.log(response.data);
              // _this.fail()
            }
          });
    },
    mycharts(){
      // 使用 macarons 主题
      let myChart = echarts.init(this.$refs.charts, "macarons");
      myChart.setOption(this.option)
      //图表自适应
      window.addEventListener("resize",function(){
        myChart.resize()  // myChart 是实例对象
      })
    },
  },
};
</script>
<style scoped>
.proCharts{
  width: 100%;
  height: 400px;
}
</style>
