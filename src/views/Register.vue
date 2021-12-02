<template>
  <div class="root">
    <div id="RegisterCard">
      <div style="font-size: 45px; font-weight: bold; margin-top: 30px">
        Register
      </div>

      <!-- 用户名 -->
      <div class="inputSection">
        <div style="font-size: 14px; padding: 5px">用户名</div>
        <el-input v-model="RegisterForm.username" placeholder="Username">
          <i
            slot="prefix"
            class="el-input__icon el-icon-user"
            style="font-size: 17px"
          ></i>
        </el-input>
      </div>

      <!-- 密码 -->
      <div class="inputSection">
        <div style="font-size: 14px; padding: 5px">密码</div>
        <el-input
          v-model="RegisterForm.password"
          placeholder="Password"
          show-password
        >
          <i
            slot="prefix"
            class="el-input__icon el-icon-lock"
            style="font-size: 17px"
          ></i>
        </el-input>
      </div>

      <!-- 确认 -->
      <div class="inputSection">
        <div style="font-size: 14px; padding: 5px">确认密码</div>
        <el-input
          v-model="RegisterForm.confirmation"
          placeholder="Password"
          show-password
        >
          <i
            slot="prefix"
            class="el-input__icon el-icon-lock"
            style="font-size: 17px"
          ></i>
        </el-input>
      </div>

      <!-- 注册按钮 -->
      <div
        id="RegisterButton"
        @click="register()"
        @mouseenter="mouseEnter()"
        @mouseleave="mouseLeave()"
      >
        <i class="el-icon-arrow-right"></i>
      </div>
    </div>
  </div>
</template>

<script>
import api from "../commonApi.js";
export default {
  name: "LoginPage",
  data() {
    return {
      RegisterForm: {
        username: "",
        password: "",
        confirmation: "",
        user_info: "",
        userType: "普通用户",
        affiliation: "",
      },
    };
  },
  methods: {
    register() {
      var _this = this;
      if (_this.RegisterForm.username.length == 0 || _this.RegisterForm.username.length > 10) {
        _this.$message({
          message: "用户名长度不能为空，且长度不能超过10",
          type: "false",
        });
      } else if (_this.RegisterForm.password.length == 0 || _this.RegisterForm.password.length > 10) {
        _this.$message({
          message: "密码长度不能为空，且长度不能超过10",
          type: "false",
        });
      } else if (
        _this.RegisterForm.password != _this.RegisterForm.confirmation
      ) {
        _this.$message({ message: "两次密码不一致", type: "error" });
      } else {
        let formData = new FormData();
        formData.append("username", this.RegisterForm.username);
        formData.append("password", this.RegisterForm.password);

        let _this = this;
        this.$axios
          .post(api.baseApi + "/user/register", formData)
          .then(function (response) {
            if (response.data.success) {
              _this.$message({
                message: response.data.message,
                type: "success",
              });

              _this.$router.push({ path: "/login" });
            } else {
              _this.$message({ message: response.data.message, type: "error" });
            }
          });
      }
    },
    mouseEnter() {
      this.$gsap.to("#RegisterButton", {
        duration: 0.1,
        height: "85px",
        width: "85px",
        top: "52px",
        boxShadow: "0px 0px 10px 10px rgba(128, 128, 128, 0.3)",
      });
    },
    mouseLeave() {
      this.$gsap.to("#RegisterButton", {
        duration: 0.1,
        height: "70px",
        width: "70px",
        top: "60px",
        boxShadow: "0px 0px 10px 0px #b3b3b3",
      });
    },

  },
};
</script>

<style scoped>
.root {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;

  background-image: url(../assets/backgroundImage/register.jpg);
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center;

  width: 100vw;
  height: 100vh;
}

#RegisterCard {
  /* outline: #808080 dotted thick;*/
  border: #cccccc solid thin;
  border-radius: 30px;

  backdrop-filter: blur(20px);
  background-color: rgba(255, 255, 255, 0.5);

  display: flex;
  flex-direction: column;
  align-items: center;

  width: 350px;
  height: 500px;
}

#title {
  /* outline: #00ff00 dotted thick; */
  font-size: 30px;
  width: 230px;

  margin-top: 50px;
  margin-bottom: 15px;
}
.inputSection {
  /* outline: #00ff00 dotted thick; */

  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;

  width: 270px;
  position: relative;
  top: 20px;
  margin-top: 10px;
}

#RegisterButton {
  /* outline: #00ff00 dotted thick; */
  border-radius: 70px;
  background-color: #e6e6e6;
  /* opacity: 0.3; */
  height: 70px;
  width: 70px;

  cursor: pointer;

  display: flex;
  justify-content: center;
  align-items: center;

  position: relative;
  top: 60px;
}

#RegisterButton i {
  /* outline: #00ff00 dotted thick; */
  font-size: 35px;
  color: black;
}
</style>
