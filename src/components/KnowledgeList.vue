<template>
  <div class="main">
    

    <div
      style="display: flex; justify-content: center; align-items: flex-start"
    >
      <v-app style="margin: 30px">
        

        <h1>辟谣专区</h1>
        <p style="color: grey">
          共{{ this.rumor_list_show.length }}条谣言/辟谣
        </p>

        <center>
        <el-input
          placeholder="Search"
          v-model="search"
          style="width: 85%; margin-bottom: 10px;"
          >
          <i slot="prefix" class="el-input__icon el-icon-search"></i>
        </el-input>
        </center>

        <div
          style="margin: 30px"
          v-for="rumor in rumor_list_show.slice(
            (this.currentPage_1 - 1) * this.eachPage,
            this.currentPage_1 * this.eachPage
          )"
          v-bind:key="rumor.rumor_id"
        >
          <RumorCard
            v-bind:title="rumor.rumor_title"
            :content="rumor.rumor_content"
            :rumor_type="rumor.rumor_type"
            :link="'rumor/' + rumor.rumor_id"
          />
        </div>
        <v-pagination
          style="margin-top: 30px"
          v-model="currentPage_1"
          :length="Math.ceil(this.rumor_list_show.length / eachPage)"
          circle
          color="cyan"
        ></v-pagination>
      </v-app>

      <v-app style="margin: 30px">
        <h1>防疫小知识</h1>

        <p style="color: grey; margin-bottom: 45px">
          共{{ this.knowledge_list_show.length }}条防疫小知识
        </p>

        <v-card>
          <v-card-title>
            防疫小知识
            <v-spacer></v-spacer>
            <v-text-field
              v-model="search_knowledge"
              append-icon="mdi-magnify"
              label="Search"
              single-line
              hide-details
            ></v-text-field>
          </v-card-title>
          <v-data-table
            :headers="headers"
            :items="knowledge_list"
            :search="search_knowledge"
            @click:row="handleClick"
            :footer-props="{
              disableItemsPerPage: true,
              itemsPerPageOptions: [25],
            }"
          ></v-data-table>
        </v-card>
      </v-app>
    </div>
  </div>
</template>


<script>
import api from "../commonApi.js";
import RumorCard from "./common/RumorCard";
// import QuestionCard from "./common/QuestionCard.vue";
import moment from "moment";

export default {
  name: "KnowledgeList",
  data() {
    return {
      knowledge_list: [],
      rumor_list: [],
      currentPage_1: 1,
      currentPage_2: 1,
      eachPage: 5,
      dialogVisible: false,
      search: "",
      search_knowledge: "",
      headers: [
        {
          text: "标题",
          align: "start",
          sortable: false,
          value: "knowledge_title",
        },
        { text: "日期", value: "knowledge_date" },
        // { text: "Fat (g)", value: "fat" },
        // { text: "Carbs (g)", value: "carbs" },
        // { text: "Protein (g)", value: "protein" },
        // { text: "Iron (%)", value: "iron" },
      ],
      // desserts: [
      //   {
      //     name: "Frozen Yogurt",
      //     date: 159,
      //   },
      // ],
    };
  },
  props: ["title"],
  components: {
    // QuestionCard,
    RumorCard,
  },
  computed: {
    knowledge_list_show() {
      return this.knowledge_list.filter(
        (item) => item.knowledge_title.indexOf(this.search) >= 0
      );
    },
    rumor_list_show() {
      return this.rumor_list.filter(
        (item) => item.rumor_title.indexOf(this.search) >= 0
      );
    },
  },
  methods: {
    sleep(ms) {
      return new Promise((resolve) => setTimeout(resolve, ms));
    },
    getAllKnowledge() {
      let formData = new FormData();
      let config = {
        headers: { "Content-Type": "multipart/form-data" },
      };
      var _this = this;
      this.$axios
        .get(api.baseApi + "/notice/list_all_knowledge", formData, config)
        .then(function (response) {
          console.log(response.status);
          if (response.status == 200) {
            // console.log((response))
            _this.knowledge_list = response.data.data;
          } else {
            console.log("请求失败");
            // console.log(response.data);
            // _this.fail()
          }
        });
    },
    getAllRumors() {
      let formData = new FormData();
      let config = {
        headers: { "Content-Type": "multipart/form-data" },
      };
      var _this = this;
      this.$axios
        .get(api.baseApi + "/notice/list_all_rumor", formData, config)
        .then(function (response) {
          console.log(response);
          console.log(response.status);
          if (response.status == 200) {
            console.log(response);
            _this.rumor_list = response.data.data;
            for (var i = 0; i < _this.rumor_list.length; i++) {
              _this.rumor_list[i].rumor_time = moment(
                _this.rumor_list[i].rumor_time
              )
                .subtract(12, "hours")
                .startOf("day")
                .fromNow();
            }
            _this.total = _this.rumor_list.length;
          } else {
            console.log("请求失败");
            // console.log(response.data);
            // _this.fail()
          }
        });
    },
    handleClick(value) {
      // console.log(value)
      window.location.href = value.knowledge_link
      // this.viewDetails(value);
    },
  },
  mounted: function () {
    this.getAllRumors();
    this.getAllKnowledge();
  },
};
</script>

<style scoped>
.main {
  /*background-color: violet;*/
  display: flex;
  flex-direction: column;
  align-items: center;
}
.rumor {
  background-image: url(../static/tag1.png);
  background-size: 200px 200px;
}
</style>
