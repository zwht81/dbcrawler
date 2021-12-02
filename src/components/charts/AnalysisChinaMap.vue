<template>
  <div id="analysis-china-map"></div>
</template>
<script>
import * as echarts from "echarts";
var chinaen2zh = require("../../data/utils/provinceen2zh.json");
var mapdata = require("../../data/utils/provincezhname2adcode.json")
var coviddata; //为了显示所有数据存储一份全局数据
var chinazh2en = {};
export default {
  name: "AnalysisChinaMap",
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
      type: Object,
      required: true,
    },
  },
  mounted() {
    this.loadzh2en();
    coviddata = this.$props.data;
    var mapname;
    if (this.$props.country["name"] == "中国") {
      mapname = "China";
      this.dataprocessing(); //全国数据需要转中文
    } else {
      mapname = this.$props.country["info"]["adcode"];
    }
    this.myChart = echarts.init(document.getElementById("analysis-china-map"));
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
          text: "全国新型冠状病毒肺炎疫情图",
          textStyle: {
            color: "#000",
          },
          subtext: "数据来源于政府机构等",
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
            var name = params.name; //name是中文，数据可能是英文
            var enname = ""; //英文名字
            for (var j in chinaen2zh) {
              if (chinaen2zh[j]["label"] == name) {
                enname = chinaen2zh[j]["value"];
                break;
              }
            }
            var mapping = {
              nowcases: "现有",
              cases: "确诊",
              deaths: "死亡",
              recovered: "治愈",
            };
            var res =
              "<b>" +
              name +
              "</b>" +
              "<br/>";
            var tmp = {};
            for (var i in coviddata) {
              if (
                coviddata[i]["name"] == name ||
                coviddata[i]["name"] == enname
              ) {
                tmp = coviddata[i];
                break;
              }
            }
            for (var key in mapping) {
              if(tmp[key]==undefined)tmp[key] = 0;
              res +=
                '<p align="left">' +
                "<b>" +
                mapping[key] +
                "</b>" +
                ":  "+
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
            { min: 0, max: 9, label: "小于10", color: "#FFFACD" },
            { min: 10, max: 100, label: "10-100", color: "#fee090" },
            {
              min: 100,
              max: 1000,
              label: "100-1000",
              color: "#fdae61",
            },
            {
              min: 1000,
              max: 10000,
              label: "1000-10000",
              color: "#f46d43",
            },
            { min: 10000, label: "大于10000", color: "#a50026" },
          ],
        },
        series: [
          {
            name: "ChinaMap",
            nameProperty: "name",
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
    country(){
      var mapname;
      if (this.$props.country["name"] == "中国") {
        mapname = "China";
        //this.dataprocessing(); //全国数据需要中文和拼音
      } else {
        mapname = this.$props.country["info"]["adcode"];
      }
      this.loadMap(mapname);
    },
    data() {
      coviddata = this.$props.data;
      if(this.$props.country["name"]=="中国"){
        this.dataprocessing();
      }
      this.option["series"][0]["data"] = coviddata;
      this.loadData();
    },
  },
  methods: {
    loadzh2en(){
      for(var item in chinaen2zh){
        chinazh2en[chinaen2zh[item]] = [item];
      }
    },
    dataprocessing() {
      // 当前图为China时将获取的省会数据英文名称转中文
      for (var i in coviddata) {
        var zhname = chinaen2zh[coviddata[i]["name"]];
        if(zhname!=undefined){
          coviddata[i]["name"] = zhname;
        }
      }
    },
    loadMap(name) {
      this.myChart.showLoading();
      const mapData = require("../../data/map/json/GeoMapData_CN/" + name);
      echarts.registerMap(name, mapData);
      this.option["series"][0]["map"] = name;
      this.option["series"][0]["zoom"] = 2;
      this.option["series"][0]["center"] = undefined;
      this.myChart.setOption(this.option);
    },
    clickevent(newcountry) {
      if (this.$props.country.name != "中国") return; //最多到二级
      this.$parent.$parent.$parent.changeCountry({
        name: newcountry,
        info:{
          name: chinazh2en[newcountry],
          adcode: mapdata[newcountry],
        }
        
      });
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
#analysis-china-map {
  width: 900px;
  height: 540px;
}
</style>