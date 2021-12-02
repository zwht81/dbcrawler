<template>
  <div class="about_root">
    <span class="title"> <b>Covid</b> 数据来源 </span>
    <el-divider />

    <v-data-table
      dense
      :headers="headers"
      :items="data_source"
      item-key="name"
      class="elevation-1"
      :footer-props="{
        disableItemsPerPage: true,
        itemsPerPageOptions: [25],
      }"
    ></v-data-table>
  </div>
</template>

<script>
export default {
  name: "About",
  components: {},
  data() {
    return {
      data_source: [
        {
          name: "各国历史疫苗数据",
          url: "https://disease.sh/v3/covid-19/vaccine/coverage/countries?lastdays=all&fullData=true",
        },
        {
          name: "各国历史确诊/死亡/治愈人数",
          url: "https://covid19.health",
        },
        {
          name: "各国分省历史确诊/死亡/治愈人数",
          url: "https://covid19.health",
        },
        {
          name: "中国各省级行政区历史确诊/死亡/治愈人数",
          url: "https://covid19.health",
        },
        {
          name: "中国各二级行政区历史确诊/死亡/治愈人数",
          url: "https://covid19.health",
        },
        {
          name: "中高风险区域",
          url: "http://www.gd.gov.cn/gdywdt/zwzt/yqfk/content/mpost_3021711.html",
        },
        {
          name: "中国各省份的疫苗数据",
          url: "来自各地的政府网站",
        },
        {
          name: "谣言/辟谣",
          url: "https://www.piyao.org.cn/2020yqpy/",
        },
        {
          name: "疫情最新通告",
          url: "http://www.gov.cn/fuwu/zt/yqfwzq/yqfkblt.htm",
        },
        {
          name: "疫情防控政策",
          url: "http://www.gov.cn/fuwu/zt/yqfwzq/yqfkblt.htm#1",
        },
        {
          name: "疫情防控小知识",
          url: "http://www.gov.cn/fuwu/zt/yqfwzq/yfcs.htm#5",
        },
        {
          name: "航班班次信息",
          url: "https://flights.ctrip.com/itinerary/oneway/bjs-sha?date=2019-07-18",
        },
        {
          name: "航班状态信息",
          url: "http://www.umetrip.com/mskyweb/fs/fc.do?flightNo={code}&date={date}&channel={}",
        },
        {
          name: "火车班次信息",
          url: "https://huoche.tuniu.com/tn?r=train/trainTicket/getTickets",
        },
        {
          name: "火车经停站信息",
          url: "https://huoche.tuniu.com/tn?r=train/trainTicket/getTrainInfo",
        },
      ],
      headers: [
        {
          text: "来源数据",
          value: "name",
          align: "start",
        },
        { text: "链接地址", value: "url", align: "start" },
      ],
    };
  },
};
</script>

<style scoped>
.about_root {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  margin-top: 100px;
}
.title {
  font-size: 25px;
  align-self: flex-start;
  position: relative;
  left: 250px;
}
</style>
