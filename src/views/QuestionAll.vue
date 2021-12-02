<template>
  <div class="root">
    <!-- <span class="title">
      <b>Covid</b> Q&A
    </span> -->
      
    <el-divider/>
    <QuestionList/>
  </div>
</template>


<script>
import QuestionList from '../components/QuestionList'

export default {
  name: 'QuestionAll',
  components: {
    QuestionList,
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

