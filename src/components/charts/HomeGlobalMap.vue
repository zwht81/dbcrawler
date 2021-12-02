<template>
  <div id="global-main-map"></div>
</template>
<script>
/*
功能：
1. 展示世界地图
2. 可以改变热力图主键
3. 鼠标悬浮显示该国家所有数据
4. 点击国家跳转到该国家分析页面
5. 国家显示中文
*/
import * as echarts from "echarts";
var countrymapping = require("../../data/utils/countryen2zh.json");
var countryName = function (name) {
  // en2zh
  for (var key in countrymapping) {
    if (countrymapping[key]["value"] == name)
      return countrymapping[key]["label"];
  }
  return name;
};
var coviddata; //为了显示所有数据存储一份全局数据
export default {
  name: "GlobalMap",
  /*
    data:所有区域或国家的**当天**四个数据
    {
      "cases":[{name:"",value:""}],
      "deaths":[],
      "recovered":[],
      "vaccine":[]
    }

    type:热力图主键:
    __type__=["cases","deaths","recovered","vaccine","nowcases"]

    country:当前国家/World String
  */
  props: {
    data: {
      type: Array,
      required: true,
    },
    type: {
      type: String,
      required: false,
    },
  },
  mounted() {
    coviddata = this.$props.data;
    this.myChart = echarts.init(document.getElementById("global-main-map"));
    this.loadMap();
    this.option["series"][0]["data"] = coviddata;
    this.loadData();
    var _this = this;
    this.myChart.on("click", function (param) {
      _this.clickevent(param.name);
    });
  },
  data() {
    return {
      myChart: "",
      country: "World", //不变
      option: {
        title: {
          text: "全球新型冠状病毒肺炎疫情图",
          textStyle: {
            color: "#000",
          },
          subtext: "数据来源于各国政府机构等",
          subtextStyle: {
            color: "#000",
          },
          left: "center",
        },
        tooltip: {
          trigger: "item",
          showDelay: 0,
          transitionDuration: 0.2,
          padding: 10,
          formatter: function (params) {
            // 光标浮动显示内容控制
            var name = countryName(params.name);
            var mapping = {
              nowcases: "现有",
              cases: "确诊",
              deaths: "死亡",
              recovered: "治愈",
            };
            var res = "<b>" + name + "</b>" + "<br/>";
            var tmp = {};
            for (var i in coviddata) {
              if (coviddata[i]["name"] == params.name) {
                tmp = coviddata[i];
                break;
              }
            }
            for (var key in mapping) {
              res +=
                '<p align="left">' +
                "<b>" +
                mapping[key] +
                "</b>" +
                ":  " +
                tmp[key] +
                "<br/>" +
                "</p >";
            }
            return res;
          },
        },
        visualMap: {
          left: "right",
          textStyle: {
            color: "#000000",
          },
          pieces: [
            { min: 0, max: 999, label: "小于1000", color: "#FFFACD" },
            { min: 1000, max: 10000, label: "1000-10000", color: "#fee090" },
            {
              min: 10000,
              max: 100000,
              label: "10000-100000",
              color: "#fdae61",
            },
            {
              min: 100000,
              max: 1000000,
              label: "100000-1000000",
              color: "#f46d43",
            },
            { min: 1000000, label: "大于1000000", color: "#a50026" },
          ],
        },
        series: [
          {
            name: "GlobalMap",
            nameProperty: "NAME_1",
            type: "map",
            roam: true,
            zoom: 2,
            scaleLimit: {
              min: 1,
              max: 4,
            },
            map: "",
            emphasis: {
              label: {
                show: true,
                formatter: function (param) {
                  var name = param.name;
                  return countryName(name);
                },
              },
            },
            data: [],
          },
        ],
      },
    };
  },
  watch: {
    type() {
      this.loadData();
    },
  },
  methods: {
    loadMap() {
      this.myChart.showLoading();
      const mapData = require("../../data/map/json/" + this.country);
      echarts.registerMap(this.country, mapData);
      this.option["series"][0]["map"] = this.country;
      this.option["series"][0]["zoom"] = 2;
      this.option["series"][0]["center"] = undefined;
      this.myChart.setOption(this.option);
      this.myChart.hideLoading();
    },
    clickevent(newcountry) {
      //地图点击事件
      if (newcountry == "China") {
        const { href } = this.$router.resolve({
          path: "chinaanalysis",
        });
        window.open(href, "_blank");
      } else {
        const { href } = this.$router.resolve({
          path: "globalanalysis",
          query:{
            name:newcountry
          }
        });
        window.open(href, "_blank");
      }
    },
    loadData() {
      for (var i in this.option["series"][0]["data"]) {
        this.option["series"][0]["data"][i]["value"] =
          this.option["series"][0]["data"][i][this.$props.type];
      }
      this.myChart.setOption(this.option);
    },
  },
};
</script>
<style scoped>
#global-main-map {
  width: 700px;
  height: 500px;
}
</style>
