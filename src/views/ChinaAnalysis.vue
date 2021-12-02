<template>
  <div class="homeRoot">
    <center>
      <i
        class="el-icon-loading"
        v-if="!dataloaded"
        style="font-size: 40px; margin-top: 100px"
      ></i>
    </center>

    <div class="MainSection" v-if="dataloaded">
      <div class="page-header">
        <el-page-header
          @back="backtoChina"
          :content="country['name'] + '疫情数据'"
          v-if="country['name'] != '中国'"
        ></el-page-header>
        <div v-if="country['name'] == '中国'">中国疫情数据</div>
      </div>
      <el-tabs :tab-position="'left'" style="height: 700px; margin-top: 5px">
        <el-tab-pane class="tabPane" label="疫情地图">
          <div class="MapMain">
            <div class="Map">
              <div
                style="
                  border: #cccccc solid thin;
                  border-radius: 10px;
                  overflow: hidden;
                "
              >
                <analysis-china-map
                  :data="mapData"
                  :country="country"
                  :type="type"
                ></analysis-china-map>
              </div>
              <div class="TimeLine">
                <el-date-picker
                  class="datepicker"
                  v-model="date"
                  type="date"
                  value-format="yyyy-MM-ddT00:00:00Z"
                  format="yyyy 年 MM 月 dd 日"
                >
                </el-date-picker>
                <el-slider
                  class="slider"
                  v-model="t2"
                  :max="maxTimeNum"
                  :show-tooltip="false"
                ></el-slider>
              </div>
            </div>

            <div class="overviewData">
              <div v-for="(data, index) in overviewData" :key="index">
                <div @click="changeKey(data.type)">
                  <LittleDataCard
                    :nownum="data.nownum"
                    :type="data.type"
                    :newnum="data.newnum"
                    :color="data.color"
                  />
                </div>
              </div>
            </div>
          </div>
        </el-tab-pane>

        <el-tab-pane class="tabPane" label="疫情数据表">
          <div class="TableSection">
            <analysis-table
              :type="country['name']"
              :tableData="mapData"
              style="width: 950px"
            ></analysis-table>
            <div class="TimeLine">
              <el-date-picker
                class="datepicker"
                v-model="date"
                type="date"
                value-format="yyyy-MM-ddT00:00:00Z"
                format="yyyy 年 MM 月 dd 日"
              >
              </el-date-picker>
              <el-slider
                class="slider"
                v-model="t2"
                :max="maxTimeNum"
                :show-tooltip="false"
              ></el-slider>
            </div>
          </div>
        </el-tab-pane>

        <el-tab-pane class="tabPane" label="疫情数据分析">
          <div class="ChartSection">
            <china-analysis-tab
              :data="data"
              :country="country"
            ></china-analysis-tab>
          </div>
        </el-tab-pane>

        <el-tab-pane class='tabPane' label="疫苗接种分析" v-if="country['name'] == '中国'">
          <ChinaVaccineGraph/>
        </el-tab-pane>
      </el-tabs>
    </div>
  </div>
</template>
<script>
import api from "../commonApi.js";
import AnalysisTable from "../components/charts/AnalysisTable.vue";
import LittleDataCard from "../components/common/LittleDataCard.vue";
import AnalysisChinaMap from "../components/charts/AnalysisChinaMap.vue";
import ChinaAnalysisTab from "@/views/ChinaAnalysisTab";
import ChinaVaccineGraph from "../components/charts/ChinaVaccineGraph.vue";
var provinceen2zh = require("../data/utils/provinceen2zh.json");
var provincezhname2adcode = require("../data/utils/provincezhname2adcode");
var provincezh2en = require("../data/utils/provincezh2en.json");
export default {
  name: "ChinaAnalysis",
  components: {
    AnalysisTable,
    LittleDataCard,
    AnalysisChinaMap,
    // cmp_chart,
    ChinaVaccineGraph,
    ChinaAnalysisTab
  },
  data() {
    return {
      date: "",
      timevalue: 0,
      t2: 0,
      country: {}, //China或省或省会 {name:"",adcode:"",}
      type: "", //热力图主键
      data: "", //const
      dataloaded: false,
      maxTimeNum: 0, //const
      mapData: [], //表格和地图
      overviewData: [], //littlecard
      loadlocal: false,
    };
  },
  watch: {
    t2(newvalue) {
      this.timevalue = this.maxTimeNum - newvalue;
    },
    timevalue(newvalue) {
      this.date = this.data[newvalue]["date"];
      this.loadporpsdata();
      this.t2 = this.maxTimeNum - this.timevalue;
    },
    date(newvalue, oldvalue) {
      for (var item in this.data) {
        if (this.data[item]["date"] == newvalue) {
          this.timevalue = Number(item);
          return;
        }
      }
      this.date = oldvalue;
    },
  },
  computed: {},
  filters: {
    cutLongDate: function (value) {
      return value.slice(0, 10);
    },
  },
  mounted() {
    var query = this.$route.query.name;
    if (query != undefined) {
      var zhname = provinceen2zh[query];
      if (zhname == undefined) {
        //说明参数是中文
        zhname = query;
        query = provincezh2en[query];
      }
      this.loaddata({
        name: query,
        zhname: zhname,
      });
      this.country = {
        name: provinceen2zh[query],
        info: {
          name: query,
          adcode: provincezhname2adcode[zhname],
        },
      };
    } else {
      this.loaddata({
        name: "China",
        zhname: "中国",
      });
      this.country = {
        name: "中国",
        info: {
          name: "China",
          adcode: "",
        },
      };
    }

    this.type = "nowcases";
  },
  methods: {
    loaddata(name) {
      // 获得中国或指定省会或指定城市
      //this.dataloaded = false;
      if (this.loadlocal) {
        if (name.name == "China")
          this.data = require("../data/samples/" +
            name.name +
            "AnalysisSample.json");
        else
          this.data = require("../data/samples/" +
            name.zhname +
            "AnalysisSample.json");
        this.maxTimeNum = this.data.length - 1;
        this.t2 = this.maxTimeNum;
        this.date = this.data[this.timevalue]["date"];
        this.loadporpsdata();
        this.dataloaded = true;
      } else {
        var formData = new FormData();
        var _this = this;
        let config = {
          headers: { "Content-Type": "multipart/form-data" },
        };
        if (name.name == "China") {
          formData.append("country", "China");
          this.$axios
            .post(api.baseApi + "/data/list_country_overview", formData, config)
            .then(function (response) {
              if (response.data.success) {
                _this.data = response.data.data;
                _this.maxTimeNum = _this.data.length - 1;
                _this.t2 = _this.maxTimeNum;
                _this.date = _this.data[_this.timevalue]["date"];
                _this.loadporpsdata();
                _this.dataloaded = true;
              }
            });
        } else {
          formData.append("name", name.name);
          formData.append("zhname", name.zhname);
          this.$axios
            .post(
              api.baseApi + "/data/list_province_overview",
              formData,
              config
            )
            .then(function (response) {
              if (response.data.success) {
                _this.data = response.data.data;
                _this.maxTimeNum = _this.data.length - 1;
                _this.t2 = _this.maxTimeNum;
                _this.date = _this.data[_this.timevalue]["date"];
                _this.loadporpsdata();
                _this.dataloaded = true;
              }
            });
        }
      }
    },
    changeKey(nowtype) {
      var mapping = {
        现有确诊: "nowcases",
        累计确诊: "cases",
        累计死亡: "deaths",
        累计治愈: "recovered",
      };
      for (var key in mapping) {
        if (key == nowtype) {
          this.type = mapping[key];
          break;
        }
      }
    },
    loadporpsdata() {
      //Update mapData & overviewData
      this.mapData = this.data[this.timevalue]["detailed"];
      var mapping = {
        nowcases: {
          type: "现有确诊",
          color: "orange",
        },
        cases: {
          type: "累计确诊",
          color: "#AC3500",
        },
        deaths: {
          type: "累计死亡",
          color: "#000000",
        },
        recovered: {
          type: "累计治愈",
          color: "#00ACA5",
        },
      };
      var list = [];
      var res = {};
      for (var key in mapping) {
        res = {
          nownum: this.data[this.timevalue]["overview"][key]["nownum"],
          type: mapping[key]["type"],
          newnum: this.data[this.timevalue]["overview"][key]["newnum"],
          color: mapping[key]["color"],
        };
        list.push(res);
      }
      this.overviewData = list;
    },
    changeCountry(obj) {
      this.country = obj;
      this.loaddata({
        name: obj.info.name,
        zhname: obj.name,
      });
    },
    backtoChina() {
      this.changeCountry({
        name: "中国",
        info: {
          name: "China",
          adcode: "",
        },
      });
    },
    loadCasesDeathsVaccieRecoveredCmp() {},
  },
};
</script>
<style scoped>
.homeRoot {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.page-header {
  display: flex;
  justify-content: left;
  align-items: left;
  margin-bottom: 5px;
  font-size: 20px;
}
.MainSection {
  display: flex;
  flex-direction: column;
  justify-content: center;

  margin-top: 70px;
}

.overviewData {
  border: #cccccc solid thin;
  border-radius: 10px;
  overflow: hidden;
  height: 540px;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  align-items: space-around;

  margin-left: 20px;
  align-self: flex-start;
}
.TableSection {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.TimeLine {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 10px;
}
.MapMain {
  display: flex;
  justify-content: center;
  align-items: center;
}

.slider {
  margin-left: 20px;
  width: 500px;
}
.datepicker {
  width: 200px;
}
.tabPane {
  width: 1200px;
}
.ChartSection{
  margin-left:20px;
}
</style>
