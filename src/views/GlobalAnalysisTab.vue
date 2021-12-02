<template>
  <v-tabs>
    <v-tab>{{titlename}}增长趋势</v-tab>
    <v-tab>{{titlename}}各{{refer}}疫情数据占比</v-tab>
    <v-tab>{{titlename}}各{{refer}}疫情数据增长趋势对比分析</v-tab>
    <v-tab>{{titlename}}各{{refer}}单日疫情数据对比分析</v-tab>

    <v-tab-item
      > <cmp-chart :data_table="data" style="margin-top:5px;"></cmp-chart></v-tab-item>
    <v-tab-item>
      <global-analysis-tab-pie-chart :data="data" style="margin-top:5px;"></global-analysis-tab-pie-chart>
    </v-tab-item>
    <v-tab-item>
      <global-analysis-tab-overview-cmp :data_table="data" style="margin-top:5px;"></global-analysis-tab-overview-cmp>
    </v-tab-item>
    <v-tab-item>
      <global-analysis-tab-detailed-cmp :data="data" style="margin-top:5px;"></global-analysis-tab-detailed-cmp>
    </v-tab-item>
  </v-tabs>
</template>
<script>
import GlobalAnalysisTabPieChart from "./GlobalAnalysisTabPieChart.vue";
import CmpChart from "../components/charts/Cases_Deaths_Vaccine_Recovered_Cmp";
import GlobalAnalysisTabOverviewCmp from "./GlobalAnalysisTabOverviewCmp.vue";
import GlobalAnalysisTabDetailedCmp from "./GlobalAnalysisTabDetailedCmp.vue"
var countryen2zh = require("../data/utils/countryen2zh.json")
export default {
  name: "GlobalAnalysisTab",
  components: {
    GlobalAnalysisTabPieChart,
    CmpChart,
    GlobalAnalysisTabOverviewCmp,
    GlobalAnalysisTabDetailedCmp
  },
  props: {
    data: {
      type: Array,
      required: true,
    },
    country:{//控制tab的显示
      type:String,
      required:true,
    }
  },
  computed:{
    titlename(){
      for(var i in countryen2zh){
        if(countryen2zh[i]["value"] == this.$props.country)return countryen2zh[i]["label"];
      }
      return this.$props.country;
    },
    refer(){
      if(this.$props.country == "World")return "国";
      return "区域";
    }
  }
};
</script>
