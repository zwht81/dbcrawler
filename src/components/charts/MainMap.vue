<template>
  <div id="main-map" style="width: 600px; height: 500px"></div>
</template>
<script>
import * as echarts from "echarts";

import api from "../../commonApi.js";
import $ from "jquery";
export default {
  name: "MainMap",
  props: {
    country: {
      type: String,
      required: true,
      default: "world",
    },
    type: {
      type: String,
      required: true,
      default: "cases",
    },
    data: {
      type: Array,
      required: true,
    },
  },
  mounted() {
    this.myChart = echarts.init(document.getElementById("main-map"));
    this.myChart.showLoading();
    var _this = this;
    this.myChart.on("click", function (param) {
      _this.clickevent(param);
    });
    this.loadMap();
    this.loadData();
    this.loadType();
  },
  data() {
    return {
      myChart: "",
      option: {
        title: {
          text: "新型冠状病毒肺炎疫情图",
          textStyle: {
            color: "#fff",
          },
          subtext: "数据来源于官方",
          subtextStyle: {
            color: "#fff",
          },
          left: "center",
        },
        tooltip: {
          trigger: "item",
          showDelay: 0,
          transitionDuration: 0.2,
          formatter: function (params) {
            // 光标浮动显示内容控制
            var mapping = {
              cases: "确诊人数",
              deaths: "死亡人数",
              recovered: "治愈人数",
              vaccine: "疫苗接种人数",
            };
            var res = params.name + "<br/>";
            res += mapping[params.seriesName] + ":" + params.value;
            return res;
          },
        },
        visualMap: {
          left: "right",
          textStyle: {
            color: "#fff",
          },
          pieces: [
            { min: 0, max: 999, label: "小于1000", color: "#FFFACD" },
            { min: 1000, max: 10000, label: "1000-10000", color: "#fee090" },
            {
              min: 10000,
              max: 100000,
              label: "10000-100000",
              color: "#f46d43",
            },
            { min: 100000, label: "大于100000", color: "#a50026" },
          ],
        },
        series: [
          {
            name: "",
            nameProperty: "NAME_1",
            type: "map",
            roam: true,
            map: "",
            emphasis: {
              label: {
                show: true,
              },
            },
            data: [],
          },
        ],
      },
    };
  },
  watch: {
    country() {
      this.loadMap();
    },
    type() {
      this.loadType();
    },
    data() {
      this.loadData();
    },
  },
  methods: {
    loadMap() {
      let formData = new FormData();
      formData.append("name", this.$props.country);
      var mapData;
      $.ajax({
        url:api.baseApi + "/data/query_data",
        type:'POST',
        async:false,
        data:{
          name:this.$props.country
        },
        dataType:'json',
        success:function(response){
          mapData = response.data;
        }
      })
      //const mapData = require("../../data/map/json/" + this.$props.country);
      echarts.registerMap(this.$props.country, mapData);
      this.option["series"][0]["map"] = this.$props.country;
      this.option["series"][0]["center"] = ["50%, 50%"];
      this.option["series"][0]["zoom"] = 1;
      this.option["series"][0]["center"] = undefined;
      this.myChart.setOption(this.option);
      this.myChart.hideLoading();
    },
    clickevent(param) {
      //地图点击事件函数
      this.changemap(param.name);
    },
    changemap(name) {
      //地图改变事件函数
      this.$parent.changeCountry(name);
    },
    loadData() {
      this.option["series"][0]["data"] = this.$props.data;
      this.myChart.setOption(this.option);
    },
    loadType() {
      this.option["series"][0]["name"] = this.$props.type;
      this.myChart.setOption(this.option);
    },
  },
};
</script>
