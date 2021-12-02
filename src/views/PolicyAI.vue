<template>
  <div class="policy_root">
    <span class="title"> <b>Covid</b> AI Policy </span>
    <el-divider />

    <div
      style="
        font-size: 30px;
        color: #444444;
        align-self: center;
        display: flex;
        justify-content: center;
        align-items: center;
      "
      @click="dialogTableVisible = true"
    >
      <el-button
        type="primary"
        icon="el-icon-edit"
        circle
        style="margin-right: 20px"
      ></el-button>
      请输入您的问题，耐心等待回复
    </div>

    <div class="question_panel">
      <el-input
        type="textarea"
        :autosize="{ minRows: 8, maxRows: 20 }"
        placeholder="请输入内容"
        v-model="textarea"
      >
      </el-input>
    </div>

    <div class="homeHeader"      style="
        font-size: 30px;
        align-self: center;
        display: flex;
        justify-content: center;
        align-items: center;
      ">
      <div class="region">
        <el-button type="text" @click="open" style="color:#FFFFFF;">点击获取回答</el-button>
      </div>
     
    </div>

  </div>
</template>

<script>
export default {
  name: "PolicyAI",
  components: {},
  data() {
    return {
      textarea: "",
    };
  },
  methods: {
    open() {
      this.$alert("这是一段内容", "标题名称", {
        confirmButtonText: "确定",
        callback: (action) => {
          this.$message({
            type: "info",
            message: `action: ${action}`,
          });
        },
      });
    },
  },
};
</script>

<style scoped>
.policy_root {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  margin-top: 100px;
}
.title {
  font-size: 80px;
  align-self: flex-start;
  position: relative;
  left: 250px;
}
.question_panel {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 60px;
  margin-bottom: 60px;
  width: 700px;

  /* align-self: flex-start; */
  /* 
  margin-right: 40%; */
}
.homeHeader {
  display: flex;
  justify-content: center;
  align-items: flex-end;
  margin-bottom: 20px;

  align-self: start;
}
.homeOverview {
  display: flex;
  justify-content: space-between;
  align-items: center;

  padding-left: 30px;
  padding-right: 30px;
  padding-top: 10px;
  padding-bottom: 10px;
  border: #cccccc solid thin;
  border-radius: 40px;
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
