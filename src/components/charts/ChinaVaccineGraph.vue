<template>
  <div class="vaccine_root">
    <h3 v-show="isParent">
      各省/直辖市的疫苗接种率表（显示每个人的平均接种剂数）
    </h3>
    <h3 v-show="!isParent">{{ curCity }}的疫苗接种情况</h3>
    <v-card style="margin: 30px">
      <v-card-title>
        <v-text-field
          v-model="search"
          append-icon="mdi-magnify"
          label="Search"
          single-line
          hide-details
        ></v-text-field>
      </v-card-title>
      <v-data-table
        dense
        :headers="headers"
        :items="provinces"
        :search="search"
        @click:row="handleClick"
        :footer-props="{
          disableItemsPerPage: true,
          itemsPerPageOptions: [10],
        }"
      ></v-data-table>
    </v-card>
    <v-btn
      v-show="!isParent"
      class="ma-2"
      color="orange darken-2"
      light
      @click="handleBack"
    >
      <v-icon dark left> mdi-arrow-left </v-icon>返回
    </v-btn>
  </div>
</template>

<script>
// import * as echarts from "echarts";
import axios from "axios";
import api from "../../commonApi.js";
export default {
  name: "ChinaVaccineGraph",
  mounted() {
    // this.myChart = echarts.init(document.getElementById("vaccine_graph"));
    // this.myChart.setOption(this.option);
    this.getChinaVaccineData();
  },
  data() {
    return {
      data: [],
      search: "",
      isParent: true,
      curCity: "",
      headers: [
        // {
        //   text: "Dessert (100g serving)",
        //   align: "start",
        //   filterable: false,
        //   value: "name",
        // },
        { text: "地名", value: "city", align: "center" },
        { text: "累计接种", value: "total", align: "center" },
        { text: "接种率", value: "rate", align: "center" },
      ],
      provinces: [],
    };
  },
  methods: {
    getChinaVaccineData() {
      var _this = this;
      axios
        .get(api.baseApi + "/data/list_vaccine_province_info")
        .then(function (response) {
          if (response.status == 200) {
            _this.data = response.data.data;
            var lenData = _this.data.length;
            // console.log(response.data.data)
            // console.log(lenData)
            for (var i = 0; i < lenData; i++) {
              var tmp;
              tmp = {
                city: _this.data[i].parent_city,
                total: _this.data[i].parent_count,
                rate: _this.data[i].rate,
              };
              _this.provinces.push(tmp);
            }
          } else {
            console.log("请求失败");
          }
        });
    },
    handleClick(value) {
      var _this = this;
      if (_this.isParent == true) {
        _this.isParent = false;
        _this.curCity = value.city;
        // console.log(_this.isParent, _this.curCity);
        _this.provinces.length = 0;
        for (var i = 0; i < _this.data.length; i++) {
          if (value.city == _this.data[i].parent_city) {
            for (var j = 0; j < _this.data[i].child_city.length; j++) {
              var tmp;
              tmp = {
                city: _this.data[i].child_city[j].child,
                total: _this.data[i].child_city[j].count,
                rate: "/",
              };
              _this.provinces.push(tmp);
            }
            break;
          }
        }
      }
    },
    handleBack() {
      var _this = this;
      _this.isParent = !_this.isParent;
      _this.provinces.length = 0;
      var lenData = _this.data.length;
      // console.log(response.data.data)
      // console.log(lenData)
      for (var i = 0; i < lenData; i++) {
        var tmp;
        tmp = {
          city: _this.data[i].parent_city,
          total: _this.data[i].parent_count,
          rate: _this.data[i].rate,
        };
        _this.provinces.push(tmp);
      }
    },
  },
};
</script>
<style scoped>
.ma-2 {
  display: flex;
  /* flex-direction: column; */
  justify-content: flex-end;
  /* align-items: center; */
}
</style>