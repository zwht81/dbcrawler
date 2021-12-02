<template>
  <v-container class="grey lighten-5">
    <v-row no-gutters>
      <v-col cols="12" sm="6" md="8"  style="padding: 10px">
        <v-card class="pa-2" outlined tile>
          <el-dialog
            title="提示"
            :visible.sync="dialogVisible"
            width="30%"
            :before-close="handleClose"
          >
            <el-form
              :model="ruleForm"
              :rules="rules"
              ref="ruleForm"
              label-width="100px"
              class="demo-ruleForm"
            >
              <el-form-item label="问题名称" prop="name">
                <el-input v-model="ruleForm.name"></el-input>
              </el-form-item>
              <el-form-item label="问题内容" prop="content">
                <el-input v-model="ruleForm.content" type="textarea"></el-input>
              </el-form-item>

              <el-form-item>
                <el-button type="primary" @click="submitForm('ruleForm')"
                  >立即创建</el-button
                >
                <el-button @click="resetForm('ruleForm')">重置</el-button>
              </el-form-item>
            </el-form>
            <span slot="footer" class="dialog-footer"> </span>
          </el-dialog>

          <div
            style="
              display: flex;
              justify-content: center;
              align-items: flex-start;
            "
          >
            <v-app style="margin: 30px">
              <h1>问答专区</h1>
              <p style="color: grey">
                共{{ this.question_list_show.length }}条提问
              </p>

              <center>
                <v-btn v-if='isLogined'
                  rounded
                  color="cyan"
                  dark
                  @click="dialogVisible = true"
                  width="140px"
                >
                  <v-icon left> mdi-pencil </v-icon>
                  我要提问
                </v-btn>


                <v-btn v-if='!isLogined' 
                  rounded
                  color="gray"
                  dark
                  width="140px"
                >
                  <v-icon left> mdi-pencil </v-icon>
                  提问前请先登录
                </v-btn>
              </center>

              <center>
                <el-input
                  placeholder="Search"
                  v-model="search"
                  style="width: 350px; margin-top: 20px"
                >
                  <i slot="prefix" class="el-input__icon el-icon-search"></i>
                </el-input>
              </center>

              <div class="listSection">
                <div
                  style="margin: 30px"
                  v-for="question in question_list_show.slice(
                    (this.currentPage - 1) * this.eachPage,
                    this.currentPage * this.eachPage
                  )"
                  v-bind:key="question.question_id"
                >
                  <QuestionCard
                    v-bind:title="question.question_title"
                    :link="'question/' + question.question_id"
                    :content="question.question_content"
                  />
                </div>
              </div>

              <v-pagination
                style="margin-top: 30px"
                v-model="currentPage"
                :length="Math.ceil(this.question_list_show.length / eachPage)"
                circle
                color="cyan"
              ></v-pagination>
            </v-app>
          </div>
        </v-card>
      </v-col>
      <v-col cols="6" md="4" style="padding: 10px">
        <v-card class="pa-2" outlined tile>
          <template>
            <v-simple-table style="margin: 30px">
              <template v-slot:default>
                <thead>
                  <tr>
                    <th class="text-left"><h1 style="color:black; margin-bottom: 20px">为您推荐问题</h1></th>
                  </tr>
                </thead>
                <tbody>
                  <tr
                    v-for="item in recommend_questions"
                    :key="item.question_id"
                    @click="goToNewsPage('/question/' + item.question_id)"
                  >
                    <td>{{ item.question_title }}</td>
                  </tr>
                </tbody>
              </template>
            </v-simple-table>
          </template>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>




<script>
import api from "../commonApi.js";
import QuestionCard from "./common/QuestionCard.vue";
import moment from "moment";

export default {
  name: "QuestionList",
  inject:['reload'],
  data() {
    return {
      recommend_questions: [],
      question_list: [],
      currentPage: 1,
      eachPage: 10,
      dialogVisible: false,
      search: "",
      ruleForm: {
        name: "",
        content: "",
      },
      rules: {
        name: [
          { required: true, message: "请输入问题标题", trigger: "blur" },
          {
            min: 1,
            max: 10,
            message: "长度在 1 到 10 个字符",
            trigger: "blur",
          },
        ],
        content: [
          { required: true, message: "请输入问题内容", trigger: "blur" },
          {
            min: 1,
            max: 100,
            message: "长度在 1 到 100 个字符",
            trigger: "blur",
          },
        ],
      },
    };
  },
  props: ["title"],
  components: {
    QuestionCard,
  },
  computed: {
    question_list_show() {
      return this.question_list.filter(
        (item) => item.question_title.indexOf(this.search) >= 0
      );
    },
    isLogined () {
      return this.$store.getters.userState.isLogined
    }
  },
  methods: {
    goToNewsPage(link) {
      this.$router.push(link);
      this.reload;
    },
    sleep(ms) {
      return new Promise((resolve) => setTimeout(resolve, ms));
    },
    getAllQuestions() {
      let formData = new FormData();
      let config = {
        headers: { "Content-Type": "multipart/form-data" },
      };
      var _this = this;
      this.$axios
        .get(api.baseApi + "/notice/list_all_questions", formData, config)
        .then(function (response) {
          console.log(response.status);
          if (response.status == 200) {
            // console.log((response))
            _this.question_list = response.data.data;
            _this.recommend_questions = response.data.recommend_questions;
            for (var i = 0; i < _this.question_list.length; i++) {
              _this.question_list[i].question_time = moment(
                _this.question_list[i].question_time
              )
                .startOf("day")
                .fromNow();
            }
          } else {
            console.log("请求失败");
            // console.log(response.data);
            // _this.fail()
          }
        });
    },
    handleClose(done) {
      this.$confirm("确认关闭？")
        // eslint-disable-next-line no-unused-vars
        .then((_) => {
          done();
        })
        // eslint-disable-next-line no-unused-vars
        .catch((_) => {});
    },
    submitForm(formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          this.dialogVisible = false;
          console.log(this.ruleForm);
          let formData = new FormData();
          formData.append("user_id", this.$store.getters.userState.id);
          formData.append("question_title", this.ruleForm.name);
          formData.append("question_content", this.ruleForm.content);
          let config = {
            headers: { "Content-Type": "multipart/form-data" },
          };
          var _this = this;
          this.$axios
            .post(api.baseApi + "/notice/create_question", formData, config)
            .then(function (response) {
              console.log(response.status);
              if (response.status == 200) {
                console.log(response);
                _this.$message({ message: "提问成功", type: "success" });
                _this.sleep(10).then(() => {
                  _this.$router.go(0);
                });
              } else {
                console.log("请求失败");
                // console.log(response.data);
                // _this.fail()
              }
            });
        } else {
          console.log("error submit!!");
          return false;
        }
      });
    },
    resetForm(formName) {
      this.$refs[formName].resetFields();
    },
  },
  mounted: function () {
    this.getAllQuestions();
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
.listSection {
  /* outline: #00ff00 dotted thick; */

  display: flex;
  justify-content: center;
  align-items: center;
  flex-wrap: wrap;

  width: 850px;
}
</style>
