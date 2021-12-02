<template>
  <div id="china-map" style="width: 1000px; height: 800px; border: 1px #191919;"></div>
</template>
<script>
import * as echarts from "echarts";
// import $ from "jquery";

var data = [];
var mapData;
export default {
  name: "ChinaMap",
  props: {
    medium_risk: {
      type: Array,
      required: true,
    },
    high_risk: {
      type: Array,
      required: true,
    }
  },
  mounted() {
    this.myChart = echarts.init(document.getElementById("china-map"));
    this.myChart.showLoading();
    this.loadMap();
    var _this = this;
    this.myChart.on("click", function (param) {
      _this.clickevent(param);
    });
  },
  data() {
    return {
      myChart: "",
      mapName: "China",
      option: {
        title: {
          text: "国内疫情中高风险地区",
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
            trigger: 'item',
            showDelay: 0,
            transitionDuration: 0.2,
            formatter: function (params) {
              // console.log(params);
              // var res = data.filter(function (item) {
                // return item.adcode === params.name;
              // });
                      // + '<br/>';
              // res += params.seriesName;
              if (params.value === 0)
                return params.name + '<br/>低风险';
              if (params.value === 1)
                return params.name + '<br/>中风险';
              if (params.value === 2)
                return params.name + '<br/>高风险';
            }
        },
        visualMap: {
            left: 'right',
            textStyle: {
              color: "#fff",
            },
            pieces: [
                {min: 0, max: 0,label:'低风险',color:'#EAE0D7'},
                {min: 1, max: 1,label:'中风险',color:'#f46d43'},
                {min: 2, max: 2,label:'高风险',color:'#a50026'},
            ],
        },
        series: [
          {
            name: "",
            nameProperty: "name",
            type: "map",
            roam: true,
            map: "",
            // emphasis: {
            //   label: {
            //     show: true
            //   }
            // },
            normal: {
              label: {
                show: true,
              },
            },
            emphasis: {
                label: {
                  show: true
                }
              },
            data: [],
            itemStyle: {
              normal: {
                label: {
                  show: true,
                  textStyle: {
                    color: "rgb(144 144 144)",
                  },
                },
              },
              emphasis: {
                label: {
                  show: true,
                }
              }
            }
            // nameMap: {
            //   '110000' : '北京市'
            // }
          },
        ]
      },
    };
  },
  watch: {
    mapName() {
      this.loadMap();
    },
  },
  methods: {
    loadMap() {
      mapData = require("../../data/map/json/GeoMapData_CN/" + this.mapName);
      echarts.registerMap(this.mapName, mapData);
      this.option["series"][0]["name"] = this.mapName;
      this.option["series"][0]["map"] = this.mapName;
      if(this.mapName === 'China') {
        this.option["series"][0]["center"] = undefined;
        this.option["series"][0]["zoom"] = 1.5;
      }
      else {
        this.option["series"][0]["center"] = undefined;
        this.option["series"][0]["zoom"] = 1.3;
      }

      this.option["series"][0].normal.label.show = false;
      this.option["series"][0].emphasis.label.show = false;
      // console.log(mapData.features);
      var features = mapData.features;
      var medium_risk = this.$props.medium_risk;
      var high_risk = this.$props.high_risk;
      features.forEach((item)=>{
        // console.log(item.properties);
        var properties = item.properties;
        // properties.adcode = properties.adcode.toString();
        data.push(properties);
        // var adcode = properties.adcode.toString();
        var newdata = {name: properties.name, value: 0};
        // console.log(medium_risk);
        // console.log(typeof medium_risk);
        medium_risk.forEach((item1)=>{
          // console.log(properties.name);
          // console.log(item1.province);
          // console.log("aaa");
          if(properties.name === item1.province || properties.name === item1.city){
            // console.log("aaa");
            newdata.value = 1;
          }
        });
        high_risk.forEach((item1)=>{
          if(properties.name === item1.province || properties.name === item1.city){
            newdata.value = 2;
          }
        });
        // console.log(newdata);
        // this.option["series"][0].data.push(newdata);
        if (this.option["series"][0].data.find(function (item1) {
          return item1.name === newdata.name;
        }) === undefined) this.option["series"][0].data.push(newdata);
      });
      // console.log(medium_risk);
      // console.log(this.option["series"][0].data);
      // console.log(data);
      this.myChart.setOption(this.option);
      this.myChart.hideLoading();
    },

    clickevent(param) {
      // console.log(param);
      this.changemap(param.name);
    },
    backtochina() {
      this.mapName = "China";
    },
    changemap(name) {
      this.mapName = data.find(function (item) {
        return item.name === name;
      }).adcode;
      // this.$refs.RiskMap.updatePath(name);
    },
    getMapName() {
      return this.mapName;
    }
  },
};
</script>

