<template>
  <div id="analysis-global-map"></div>
</template>
<script>
import * as echarts from "echarts";
var countryen2zh = require("../../data/utils/countryen2zh.json");
import api from "../../commonApi.js";
import $ from "jquery";
var coviddata; //为了显示所有数据存储一份全局数据
export default {
  name: "AnalysisGlobalMap",
  props: {
    data: {
      type: Array,
      required: true,
    },
    type: {
      // 控制热力图主键
      type: String,
      required: false,
    },
    country: {
      type: String,
      required: true,
    },
  },
  mounted() {
    coviddata = this.$props.data;
    var mapname = this.$props.country;
    this.myChart = echarts.init(document.getElementById("analysis-global-map"));
    this.loadMap(mapname);
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
            var name = params.name;
            var zhname;
            for (var i in countryen2zh) {
              if (countryen2zh[i]["value"] == name){
                zhname = countryen2zh[i]["label"];
                break;
              }
            }
            if(zhname==undefined)zhname = name;
            var mapping = {
              nowcases: "现有",
              cases: "确诊",
              deaths: "死亡",
              recovered: "治愈",
            };
            var res =
              "<b>" +
              zhname +
              "</b>" +
              "<br/>";
            var tmp = {};
            for (i in coviddata) {
              if (coviddata[i]["name"] == name) {
                tmp = coviddata[i];
                break;
              }
            }
            for (var key in mapping) {
              if (tmp[key] == undefined) tmp[key] = 0;
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
            name: "WorldMap",
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
    data() {
      // data若变则country必定已经变
      coviddata = this.$props.data;
      var mapname = this.$props.country;
      this.loadMap(mapname);
      this.option["series"][0]["data"] = coviddata;
      this.loadData();
    },
  },
  methods: {
    loadMap(name) {
      this.myChart.showLoading();
      var mapData;
      if (name == "World")
        mapData = require("../../data/map/json/" + name);
      else {
        $.ajax({
          url: api.baseApi + "/data/query_data",
          type: "POST",
          async: false,
          data: {
            name: this.$props.country,
          },
          dataType: "json",
          success: function (response) {
            mapData = response.data;
          },
        });
      }
      echarts.registerMap(name, mapData);
      this.option["series"][0]["map"] = name;
      this.option["series"][0]["zoom"] = 2;
      this.option["series"][0]["center"] = undefined;
      this.myChart.setOption(this.option);
    },
    clickevent(newcountry) {
      if (this.$props.country != "World") return; //最多到二级
      if(newcountry == 'China') this.$router.push({path: '/chinaanalysis'});
      else this.$parent.$parent.$parent.changeCountry(newcountry);
    },
    loadData() {
      // 数据已经加载完毕，改变数据中value对应的值
      for (var i in this.option["series"][0]["data"]) {
        this.option["series"][0]["data"][i]["value"] =
          this.option["series"][0]["data"][i][this.$props.type];
      }
      this.myChart.setOption(this.option);
      this.myChart.hideLoading();
    },
  },
};
</script>
<style scoped>
#analysis-global-map {
  width: 900px;
  height: 540px;
}
</style>