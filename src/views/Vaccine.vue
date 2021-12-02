<template>
  <div class="VaccineRoot">
    <span class="title">
      <b>Covid</b> Vaccine
    </span>
    <el-divider/>
<!--    <bargraph/>-->
    <linechart/>
    <el-divider/>
    <linechart2/>
<!--    <Cases_Deaths_Vaccine_Recovered_Cmp/>-->
    <Death_Rate/>
  </div>
</template>
<script>
// import bargraph from "@/components/charts/BarGraph.vue"
// import Cases_Deaths_Vaccine_Recovered_Cmp from "@/components/charts/Cases_Deaths_Vaccine_Recovered_Cmp";
import linechart from "@/components/charts/LineChart.vue"
import linechart2 from "@/components/charts/LineChartCmp.vue"
import Death_Rate from "@/components/charts/Death_Rate";
export default {
  name: "VaccineBarGraph",
  components: {
    // bargraph,
    linechart,
    linechart2,
    // Cases_Deaths_Vaccine_Recovered_Cmp,
    Death_Rate,
  },
}
</script>

<style scoped>
.VaccineRoot {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  margin-top: 100px;
}
.title {
    font-size:80px;
    align-self: flex-start;
    position: relative;
    left: 250px;
  }
</style>
