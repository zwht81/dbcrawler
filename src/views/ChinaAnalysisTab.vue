<template>
  <v-tabs>
    <v-tab>{{zhname}}增长趋势</v-tab>
    <v-tab>{{zhname}}各{{refer}}疫情数据占比</v-tab>
    <v-tab>{{zhname}}各{{refer}}疫情数据增长趋势对比分析</v-tab>
    <v-tab>{{zhname}}各{{refer}}单日疫情数据对比分析</v-tab>

    <v-tab-item
      > <cmp-chart :data_table="data" style="margin-top:5px;"></cmp-chart></v-tab-item>
    <v-tab-item>
      <china-analysis-tab-pie-chart :data="data" style="margin-top:5px;"></china-analysis-tab-pie-chart>
    </v-tab-item>
    <v-tab-item>
      <china-analysis-tab-overview-cmp :data_table="data" style="margin-top:5px;"></china-analysis-tab-overview-cmp>
    </v-tab-item>
    <v-tab-item>
      <china-analysis-tab-detailed-cmp :data="data" style="margin-top:5px;"></china-analysis-tab-detailed-cmp>
    </v-tab-item>
  </v-tabs>
</template>
<script>
import ChinaAnalysisTabPieChart from "./ChinaAnalysisTabPieChart.vue";
import CmpChart from "../components/charts/Cases_Deaths_Vaccine_Recovered_Cmp";
import ChinaAnalysisTabOverviewCmp from "./ChinaAnalysisTabOverviewCmp.vue";
import ChinaAnalysisTabDetailedCmp from "./ChinaAnalysisTabDetailedCmp.vue"
export default {
  name: "ChinaAnalysisTab",
  components: {
    ChinaAnalysisTabPieChart,
    CmpChart,
    ChinaAnalysisTabOverviewCmp,
    ChinaAnalysisTabDetailedCmp
  },
  props: {
    data: {
      type: Array,
      required: true,
    },
    country:{//控制tab的显示
      type:Object,
      required:true,
    }
  },
  data(){
      return {
          enname:"",
          zhname:""
      }
  },
  watch:{
    country(){
      this.zhname = this.$props.country.name;
      this.enname = this.$props.country.info.name;
    }
  },
  mounted(){
      this.zhname = this.$props.country.name;
      this.enname = this.$props.country.info.name;
  },
  computed:{
    refer(){
      if(this.enname == "China")return "省";
      return "区";
    }
  }
};
</script>
