<template>
  <div class="homeRoot">
    <div class="hometitle">
      <div class="titleText">数据库课程大作业</div>
    </div>
    <div>
      <img src="https://pic.rmb.bdstatic.com/22d0149798daed118d40b44957f04cf5.jpeg" height="700" width="100%" alt="主页"/>
    </div>
    
  </div>
</template>

<script>

export default {
  name: "Home",
  components: {

  },
  data() {
    return {

    };
  },
  watch: {},
  mounted() {

  },
  methods: {

  },
};
</script>

<style scoped>
.hometitle {
  /* outline: #00ff00 dotted thick; */

  display: flex;
  justify-content: center;
  align-items: center;

  margin-top: 60px;

  margin-right: 1160px;
}
.titleText {
  font-size: 30px;
}
.hometitle .SelectBar {
  /* outline: #00ff00 dotted thick; */
  margin-left: 30px;
}

.homeMain {
  display: flex;
  justify-content: center;
  align-content: center;
}

.homeLeftSection {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.homeRightSection {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.homeChinaTable {
  margin-left: 30px;
  width: 650px;
}

.homeMapSection {
  margin-top: 20px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 100%;

  border: #cccccc solid thin;
  border-radius: 10px;
  overflow: hidden;
}
.homeHeader {
  display: flex;
  justify-content: center;
  align-items: flex-end;
  margin-bottom: 20px;

  align-self: start;
}
.homeOverview {
  position: relative;

  display: flex;
  justify-content: space-between;
  align-items: center;

  padding-left: 25px;
  padding-right: 25px;
  padding-top: 5px;
  padding-bottom: 5px;
  border: #cccccc solid thin;
  border-radius: 10px;
  width: 700px;
}
.homeTable {
  margin-top: 70px;
  margin-left: 30px;
  width: 650px;
}

.region {
  white-space: nowrap;
  text-align: center;

  font-size: 27px;
  font-weight: 500;

  background-color: #06a19c;
  color: white;

  border-radius: 30px;

  padding: 5px 15px 5px 15px;
  margin: 3px;
}
</style>
