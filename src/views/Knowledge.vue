<template>
  <div class="root">
    <!-- <span class="title">
      <b>Covid</b> Knowledge
    </span> -->
      
    <el-divider/>
    <KnowledgeList/>
  </div>
</template>


<script>
import KnowledgeList from '../components/KnowledgeList.vue'

export default {
  name: 'QuestionAll',
  components: {
    KnowledgeList,
  },

}
</script>

<style scoped>
.root {
    display: flex;
    justify-content: center;
    flex-direction: column;
    align-items: center;
  }

.title {
    margin-top: 70px;
    font-size: 30px; 
    align-self: flex-start; 
    position: relative;
    left: 250px;
  }
</style>

