<template>
  <div class="GlobalAnalysisTabPieChart">
      <el-select v-model="type" class="selector">
        <el-option
          v-for="item in options"
          :key="item.value"
          :label="item.label"
          :value="item.value"
        >
        </el-option>
      </el-select>
      <div>
        <BingChart
        :dataType="type"
        :dataTable="data"
        >
        </BingChart>
      </div>
  </div>
</template>
<script>
import BingChart from "../components/charts/BingChart.vue";
export default {
  name: "ChinaAnalysisTabPieChart",
  components: {
      BingChart,
  },
  props: {
    data: {
      type: Array,
      required: true,
    },
  },
  data() {
    return {
      
      options: [
        {
          value: "nowcases",
          label: "现有确诊",
        },
        {
          value: "cases",
          label: "累积确诊",
        },
        {
          value: "deaths",
          label: "累积死亡",
        },
        {
          value: "recovered",
          label: "累积治愈",
        },
      ],
      type: "nowcases",
    };
  },
  watch: {},
};
</script>

<style scoped>
.GlobalAnalysisTabPieChart {
  display: flex;
  flex-direction: column;
}
.selector{
  width: 200px;
  margin-left: 5px;
}
</style>