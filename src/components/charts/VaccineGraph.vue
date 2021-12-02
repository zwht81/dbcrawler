<template>
  <div class="vaccine_root">
    <h3>截止到{{ convertDate(date) }}的疫苗统计饼图（目前全球已累积接种{{total_vaccine}}剂）</h3>
    <div id="vaccine_graph" style="width: 800px; height: 540px"></div>
  </div>
</template>

<script>
import * as echarts from "echarts";
import axios from "axios";
import api from "../../commonApi.js";
export default {
  name: "VaccineGraph",
  mounted() {
    this.myChart = echarts.init(document.getElementById("vaccine_graph"));
    this.myChart.setOption(this.option);
    this.getVaccineData();
  },
  data() {
    return {
      date: "",
      total_vaccine:"",
      myChart: "",
      option: {
        title: {
          subtext: "图中显示了各国/地区的疫苗接种剂数，接种越多，在图中的占比即越大。",
          left: "center",
        },
        tooltip: {
          trigger: "item",
        },
        // legend: {
        //     orient: 'vertical',
        //     left: 'left',
        // },
        series: [
          {
            name: "地区/国家",
            type: "pie",
            radius: "60%",
            data: [],
            emphasis: {
              itemStyle: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: "rgba(0, 0, 0, 0.5)",
              },
            },
            label: false,
          },
        ],
      },
    };
  },
  methods: {
    getVaccineData() {
      var _this = this;
      axios
        .get(api.baseApi + "/data/list_vaccine_overview")
        .then(function (response) {
          if (response.status == 200) {
            _this.date = response.data.Global[0].date;
            _this.total_vaccine = response.data.Global[0].overview.vaccine;
            var detai_vaccine_list = response.data.Global[0].detailed;
            var len_data = detai_vaccine_list.length;
            for (var i = 0; i < len_data; i++) {
              var tmp = {
                value: detai_vaccine_list[i].vaccine,
                name: detai_vaccine_list[i].name,
              };
              _this.option.series[0].data.push(tmp);
            }
            _this.myChart.setOption(_this.option);
          } else {
            console.log("请求失败");
          }
        });
    },
    convertDate(value) {
      return value.slice(0, 10);
    },
  },
};
</script>
<style scoped>
.vaccine_root{
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
</style>