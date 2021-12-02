<template>
  <div class="root">
    <!-- <span class="title">
      <b>Covid</b> News
    </span> -->
    <el-divider/>
    <div class="newsSection"  style="margin-top:20px">
      <NoticesList title="中国新冠疫情最新通告" style="width: 700px"/>
      <NewsList title="中国疫情防控政策" style="width: 500px"/>
      <!-- <NewsList title="国际疫情防控措施" style="width: 400px"/> -->
    </div>
  </div>
</template>
<script>
import NewsList from '@/components/NewsList.vue';
import NoticesList from '@/components/NoticesList.vue';
export default {
  name: "News",
  components: {
    NewsList,
    NoticesList
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

  .newsSection {
    width: 85%;
    display: flex;
    justify-content: space-around;
  }
</style>
