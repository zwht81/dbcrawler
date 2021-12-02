<template>
    <div class="root">
      <div id = "LoginCard">

        <div id="title">
            <span style="font-weight: bold;">Zha</span>  <span>Covid</span>
        </div>


        <div>
            <span style="font-size: 45px; font-weight: bold;"> Login </span>
        </div>


        <!-- 用户名 -->
        <div class="inputSection">
            <div style="font-size: 14px; padding: 5px;">用户名</div>
            <el-input v-model="loginForm.username" placeholder="Username">
                <i slot="prefix" class="el-input__icon el-icon-user" style="font-size: 17px;"></i>
            </el-input >
        </div>


        <!-- 密码 -->
        <div class="inputSection">
            <div style="font-size: 14px; padding: 5px;">密码</div>
            <el-input v-model="loginForm.password" placeholder="Password" show-password>
                <i slot="prefix" class="el-input__icon el-icon-lock" style="font-size: 17px;"></i>
            </el-input >
        </div>

        <!-- 登陆按钮 -->
        <div id="LoginButton" @click="login()" @mouseenter="mouseEnter()" @mouseleave="mouseLeave()">
          <i class="el-icon-arrow-right"></i>
        </div>

      </div>
    </div>


</template>

<script>
import api from '../commonApi.js'
export default {
	name: 'LoginPage',
	data() {
		return {
			loginForm:{
				username:'',
				password:'',
			},
		}
	},
	methods: {
		login () {
			let formData = new FormData();
			formData.append('username', this.loginForm.username);
			formData.append('password', this.loginForm.password);
			
			// - TODO: test response
			let _this = this
			this.$axios
			.post(api.baseApi+'/user/login',formData)
			.then(function (response) {
				if (response.data.success) {
					_this.$message({message: response.data.message,
									type: 'success'})
					
					_this.$store.commit('login', {
						name: response.data.detail.username,
						type: response.data.detail.user_type,
						affiliation: response.data.detail.affiliation,
						id: response.data.detail.user_id,
            show_sub: response.data.show_sub,
					})
					
					_this.$router.push({path: '/'})
				}else {
					_this.$message({message: response.data.message,
									type: 'error'})
				}
			})
		},
		mouseEnter () {
			this.$gsap.to("#LoginButton", {duration: 0.1, height: '85px', width: '85px', top: '52px',  boxShadow:'0px 0px 10px 10px rgba(128, 128, 128, 0.3)'})
		},
		mouseLeave () {
			this.$gsap.to("#LoginButton", {duration: 0.1, height: '70px', width: '70px', top: '60px',  boxShadow:'0px 0px 10px 0px #b3b3b3'})
		},
	},
	
}
</script>

<style scoped>
 .root {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;

    background-image: url(../assets/backgroundImage/login.jpg);
    background-repeat: no-repeat;
    background-size: cover;
    background-position: center;

    width: 100vw;
    height: 100vh;
  }


  #LoginCard {
    /* outline: #808080 dotted thick;*/
    border: #cccccc solid thin;
    border-radius: 30px;

    backdrop-filter: blur(20px);
    background-color: rgba(255,255,255,0.5);

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
	margin-top: 10px
  }

  #LoginButton {
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

  #LoginButton i {
    /* outline: #00ff00 dotted thick; */
    font-size: 35px;
    color: black;
  }

</style>
