<template>
  <div class="subscribe_root">
    <span class="title">
    </span>

    <el-divider />

    <el-tag
      type="danger"
      v-if="!isLogined"
      style="font-weight: bold; font-size: 15px"
      >请管理员登录!</el-tag
    >

    <v-app style="height: 20px" v-if="isLogined">
      <v-btn
        rounded
        color="cyan"
        dark
        @click="dialogTableVisible = true"
        width="200px"
        height="100px"
      >
        <v-icon left> mdi-pencil </v-icon>
        开始爬新数据！
      </v-btn>
    </v-app>

    <div class="homeMain" v-if="isLogined">
      <el-dialog title="爬新的数据" :visible.sync="dialogTableVisible">

      <!-- 地址 -->
      <div class="inputSection">
          <div style="font-size: 14px; padding: 5px;">爬虫URL地址</div>
          <el-input v-model="loginForm.url" placeholder="URL">
              <i slot="prefix" class="el-input__icon el-icon-user" style="font-size: 17px;"></i>
          </el-input >
      </div>

      <div class="inputSection">
          <div style="font-size: 14px; padding: 5px;">接口类型</div>
          <el-input v-model="loginForm.method" placeholder="GET">
              <i slot="prefix" class="el-input__icon el-icon-user" style="font-size: 17px;"></i>
          </el-input >
      </div>
      <div class="question_panel">
        <div style="font-size: 14px; padding: 5px;">传值</div>
        <el-input
          type="textarea"
          :autosize="{ minRows: 8, maxRows: 20 }"
          placeholder="请输入接口需要传入的内容"
          v-model="loginForm.in"
        >
        </el-input>
      </div>

        <el-button
          type="primary"
          icon="el-icon-search"
          style="margin-top: 15px"
          @click="subCity"
          >开始！</el-button
        >
      </el-dialog>
 
        </div>
      </div>

</template>
<script>
// import LittleDataCard from "../components/common/LittleDataCard";
import axios from "axios";
import api from "../commonApi.js";
export default {
  name: "Subscribe",
  components: {
    // LittleDataCard,
  },
  computed: {
    cityList_show() {
      return this.cityList.filter(
        (item) => item.name.indexOf(this.search) >= 0
      );
    },
    isLogined() {
      if (
        this.$store.getters.userState.isLogined &&
        this.$store.getters.userState.type == 1
      ) {
        return 1;
      }
      return 0;
    },
  },
  data() {
    return {
      loginForm: {
        url: "http://10.46.159.39:8080/api/v0/writefileflag/readfile",
        method: "GET",
        in: '{"id":31,"fileName":"2021-12-01Num899506.txt","userId":"acavfad0sdwd","taskId":30}',
      },
      dialogTableVisible: false,
      cityList: [],
      search: "",
      information: [],
      // options: [
      //   { value: "安徽省", label: "安徽省" },
      //   { value: "北京市", label: "北京市" },
      //   { value: "重庆市", label: "重庆市" },
      //   { value: "福建省", label: "福建省" },
      //   { value: "甘肃省", label: "甘肃省" },
      //   { value: "广东省", label: "广东省" },
      //   { value: "广西壮族自治区", label: "广西壮族自治区" },
      //   { value: "贵州省", label: "贵州省" },
      //   { value: "海南省", label: "海南省" },
      //   { value: "河北省", label: "河北省" },
      //   { value: "黑龙江省", label: "黑龙江省" },
      //   { value: "河南省", label: "河南省" },
      //   { value: "香港", label: "香港" },
      //   { value: "湖北省", label: "湖北省" },
      //   { value: "湖南省", label: "湖南省" },
      //   { value: "江苏省", label: "江苏省" },
      //   { value: "江西省", label: "江西省" },
      //   { value: "吉林省", label: "吉林省" },
      //   { value: "辽宁省", label: "辽宁省" },
      //   { value: "澳门", label: "澳门" },
      //   { value: "内蒙古自治区", label: "内蒙古自治区" },
      //   { value: "宁夏回族自治区", label: "宁夏回族自治区" },
      //   { value: "青海省", label: "青海省" },
      //   { value: "陕西省", label: "陕西省" },
      //   { value: "山东省", label: "山东省" },
      //   { value: "上海市", label: "上海市" },
      //   { value: "山西省", label: "山西省" },
      //   { value: "四川省", label: "四川省" },
      //   { value: "台湾", label: "台湾" },
      //   { value: "天津市", label: "天津市" },
      //   { value: "新疆维吾尔自治区", label: "新疆维吾尔自治区" },
      //   { value: "西藏自治区", label: "西藏自治区" },
      //   { value: "云南省", label: "云南省" },
      //   { value: "浙江省", label: "浙江省" },
      // ],
      options: [
        {
          label: "热门城市",
          options: [
            { value: "深圳市", label: "深圳市" },
            { value: "北京市", label: "北京市" },
            { value: "上海市", label: "上海市" },
            { value: "海南市", label: "海南市" },
          ],
        },
        {
          label: "城市名",
          options: [
            { value: "安徽省", label: "安徽省" },
            // { value: "北京市", label: "北京市" },
            { value: "重庆市", label: "重庆市" },
            { value: "福建省", label: "福建省" },
            { value: "甘肃省", label: "甘肃省" },
            // { value: "广东省", label: "广东省" },
            { value: "广西壮族自治区", label: "广西壮族自治区" },
            { value: "贵州省", label: "贵州省" },
            { value: "海南省", label: "海南省" },
            { value: "河北省", label: "河北省" },
            { value: "黑龙江省", label: "黑龙江省" },
            { value: "河南省", label: "河南省" },
            { value: "香港", label: "香港" },
            { value: "湖北省", label: "湖北省" },
            { value: "湖南省", label: "湖南省" },
            { value: "江苏省", label: "江苏省" },
            { value: "江西省", label: "江西省" },
            { value: "吉林省", label: "吉林省" },
            { value: "辽宁省", label: "辽宁省" },
            { value: "澳门", label: "澳门" },
            { value: "内蒙古自治区", label: "内蒙古自治区" },
            { value: "宁夏回族自治区", label: "宁夏回族自治区" },
            { value: "青海省", label: "青海省" },
            { value: "陕西省", label: "陕西省" },
            { value: "山东省", label: "山东省" },
            // { value: "上海市", label: "上海市" },
            { value: "山西省", label: "山西省" },
            { value: "四川省", label: "四川省" },
            { value: "台湾", label: "台湾" },
            { value: "天津市", label: "天津市" },
            { value: "新疆维吾尔自治区", label: "新疆维吾尔自治区" },
            { value: "西藏自治区", label: "西藏自治区" },
            // { value: "云南省", label: "云南省" },
            { value: "浙江省", label: "浙江省" },
          ],
        },
      ],
      convertEngOptions: [
        { value: "Anhui", label: "安徽省" },
        { value: "Beijing", label: "北京市" },
        { value: "Chongqing", label: "重庆市" },
        { value: "Fujian", label: "福建省" },
        { value: "Gansu", label: "甘肃省" },
        { value: "Guangdong", label: "广东省" },
        { value: "Guangxi", label: "广西壮族自治区" },
        { value: "Guizhou", label: "贵州省" },
        { value: "Hainan", label: "海南省" },
        { value: "Hebei", label: "河北省" },
        { value: "Heilongjiang", label: "黑龙江省" },
        { value: "Henan", label: "河南省" },
        { value: "Hong Kong", label: "香港" },
        { value: "Hubei", label: "湖北省" },
        { value: "Hunan", label: "湖南省" },
        { value: "Jiangsu", label: "江苏省" },
        { value: "Jiangxi", label: "江西省" },
        { value: "Jilin", label: "吉林省" },
        { value: "Liaoning", label: "辽宁省" },
        { value: "Macao", label: "澳门" },
        { value: "Nei Mongol", label: "内蒙古自治区" },
        { value: "Ningxia Hui", label: "宁夏回族自治区" },
        { value: "Qinghai", label: "青海省" },
        { value: "Shaanxi", label: "陕西省" },
        { value: "Shandong", label: "山东省" },
        { value: "Shanghai", label: "上海市" },
        { value: "Shanxi", label: "山西省" },
        { value: "Sichuan", label: "四川省" },
        { value: "Taiwan", label: "台湾" },
        { value: "Tianjin", label: "天津市" },
        { value: "Xinjiang Uygur", label: "新疆维吾尔自治区" },
        { value: "Xizang", label: "西藏自治区" },
        { value: "Yunnan", label: "云南省" },
        { value: "Zhejiang", label: "浙江省" },
      ],
      value: "",
    };
  },
  mounted: function () {
    // this.querySubCity();
    this.getSubsData();
  },
  methods: {
    getSubsData() {
      let formData = new FormData();
      formData.append("user_id", this.$store.getters.userState.id);
      let config = {
        headers: { "Content-Type": "multipart/form-data" },
      };
      var _this = this;
      axios
        .post(api.baseApi + "/sub/list_subs_data", formData, config)
        .then(function (response) {
          if (response.status == 200) {
            // console.log(response)
            _this.information = response.data.information;
            _this.cityList = response.data.data;
          } else {
            console.log("请求失败");
          }
        });
    },

    // querySubCity() {
    //   let formData = new FormData();
    //   formData.append("user_id", this.$store.getters.userState.id);
    //   let config = {
    //     headers: { "Content-Type": "multipart/form-data" },
    //   };
    //   var _this = this;
    //   axios
    //     .post(api.baseApi + "/sub/list_all_subs", formData, config)
    //     .then(function (response) {
    //       if (response.status == 200) {
    //         _this.cityList = response.data.data;
    //       } else {
    //         console.log("请求失败");
    //       }
    //     });
    // },
    handleDelete(index, row) {
      let formData = new FormData();
      formData.append("name", row.name);
      formData.append("user_id", this.$store.getters.userState.id);
      let config = {
        headers: { "Content-Type": "multipart/form-data" },
      };
      var _this = this;
      axios
        .post(api.baseApi + "/sub/del_sub", formData, config)
        .then(function (response) {
          if (response.status == 200) {
            _this.$message({ message: "成功删除订阅", type: "true" });
            _this.cityList.forEach(function (item, ind, arr) {
              if (item.name == row.name) {
                arr.splice(ind, 1);
              }
            });
          } else {
            console.log("请求失败");
          }
        });
    },
    clickevent(cityname) {
      const { href } = this.$router.resolve({
        path: "chinaanalysis",
        query: {
          name: cityname,
        },
      });
      window.open(href, "_blank");
    },
    subCity() {
      var _this = this;
      // console.log(this.value);


      let data = '"JYFW": "一般经营范围：文化活动策划；展览展示策划；, "TYSHXYDM": "91440300MA5FL7HX16", "ZZJGDM": "MA5FL7HX1", "RECORDID": "8a8084546a5454c7016a6314907b3647", "BIZHONG": "156", "HZRQ": "2020-09-09", "YYZT": "1", "CLRQ": "2019-04-30", "QYMC": "深圳市恒河文化传媒有限公司", "ZCZB": 50.000000, "DJJGDH": "4403", "JYCS": "深圳市福田区沙头街道沙嘴社区沙嘴路 8 号红树华府 A、B、C、D 栋 A 栋 10 层1009", "ZCH": "440300206975310"'
      _this.$message({
        showClose: true,
        message: data,
        type: "success",
        duration: 0,
      });
    },
  },
};
</script>

<style scoped>
.subscribe_root {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}
.title {
  margin-top: 70px;
  font-size: 30px;
  align-self: flex-start;
  position: relative;
  left: 250px;

  display: flex;
  justify-content: center;
  align-items: center;
}

.homeMain {
  display: flex;
  justify-content: center;
  align-content: center;
  margin: 20px;
}

.homeSection {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin: 20px;
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

  font-size: 22px;
  font-weight: 500;

  background-color: #06a19c;
  color: white;

  border-radius: 30px;

  padding: 2px 12px 2px 12px;
  margin: 3px;
}
</style>
