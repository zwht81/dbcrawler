<template>
	<div>

	<el-dialog center
			title="更改您的个人信息"
			:visible.sync="dialogVisible"
			width="40%"
			:modal-append-to-body=false
			>
			
			<el-form :model="userForm">
				<el-form-item label="新用户名">
					<el-input v-model="userForm.name" autocomplete="off"></el-input>
				</el-form-item>
				<el-form-item label="旧密码">
					<el-input v-model="userForm.password" autocomplete="off" show-password></el-input>
				</el-form-item>
				<el-form-item label="新密码">
					<el-input v-model="userForm.newPassword" autocomplete="off" show-password></el-input>
				</el-form-item>
				<el-form-item label="个人信息">
					<el-input v-model="userForm.user_info" autocomplete="off"></el-input>
				</el-form-item>
			</el-form>
			
			<span slot="footer" class="dialog-footer">
				<el-button @click="dialogVisible = false">Cancel</el-button>
				<el-button type="primary" @click="modify()">Confirm</el-button>
			</span>
	</el-dialog>

	<div class='avatar' @mouseenter="mouseEnter()" @mouseleave="mouseLeave()">
		<div style="white-space: nowrap; ">
			<img v-if="isLogined" src="../../assets/avatar/cat.jpg">
			<img v-if="!isLogined" src="../../assets/avatar/cat_grey.jpg">

			<span v-if="isLogined" class="name">{{ userState.name }}</span>

			<router-link to='/login' v-if="!isLogined">
				<el-button type="success" round plain
				style="margin-left: 20px;"
				>Login</el-button>
			</router-link>
			<router-link to='/register' v-if="!isLogined">
				<el-button type="primary" round plain
				style="margin-left: 20px;"
				>Register</el-button>
			</router-link>

		</div>
		<div v-if="isLogined" style="height: 30px;"></div>
		<div v-if="isLogined" class='info'>
			
			<div style="display: flex; flex-wrap: wrap; justify-content: center;">
				<b class='userTag'>
					<i class='el-icon-s-custom'></i>
					{{userType}}
				</b>
				<span v-if="userState.type==1" class='userTag' style="background-color: #dace0a;">
					<i class='el-icon-school'></i>
					{{userState.affiliation}}
				</span>
			</div>
			
		</div>
		<div v-if="isLogined">
			<el-divider></el-divider>
			<div>
				<el-button type="danger" round plain
				size="medium"
				@click='unlogin()'
				>退出登陆</el-button>
				
				<el-button type="primary" round plain
				size="medium"
				@click='dialogVisible = true'
				>修改信息</el-button>
			</div>
		</div>
	</div>

	</div>
</template>

<script>
import api from '../../commonApi.js'
export default {
	name: 'UserAvatar',
	data() {
		return {
			dialogVisible: false,
			userForm: {
				name: '',
				password: '',
				newPassword: ''
			}
		}
	},
	computed: {
		userState () {
			return this.$store.getters.userState
		},
		isLogined () {
			return this.userState.isLogined
		},
		userType() {
			return this.userState.type=='0' ? '普通用户' : '认证机构用户'
		}
	},
	methods: {
		unlogin () {
			this.$confirm('This will unlogin your account. Continue?', 'Warning', {
				confirmButtonText: 'OK',
				cancelButtonText: 'Cancel',
				type: 'warning'
			}).then(() => {
				this.$store.commit('reset')
				this.$router.push({path: '/'})
			}).catch(()=>{})
		},
		modify () {
			this.dialogVisible = false
			
			let formData = new FormData();
			formData.append('user_id', this.$store.getters.userState.id);
			formData.append('username', this.userForm.name);
			formData.append('password_old', this.userForm.password);
			formData.append('password_new', this.userForm.newPassword);
			formData.append('user_info', this.userForm.user_info);
			// - TODO: test response
			let _this = this
			this.$axios
			.post(api.baseApi+'/user/modify',formData)
			.then(function (response) {
				if (response.data.success) {
					_this.$message({message: response.data.message,
									type: 'success'})
					
					_this.$store.commit('login', {
						name: response.data.data.username,
						type: response.data.data.user_type,
						affiliation: response.data.data.affiliation,
						id: response.data.data.user_id,
					})
					
				}else {
					_this.$message({message: response.data.message,
									type: 'error'})
				}
			})
		},
		mouseEnter () {
			if (this.userState.isLogined) {
				this.$gsap.to(".avatar", {
							duration: 0.5, ease: 'power4.out',
							height: '220px', width: '250px', 
							boxShadow:'0px 0px 30px 5px rgba(128, 128, 128, 0.25)',
							borderRadius: '30px',
							})
			} else {
				this.$gsap.to(".avatar", {
							duration: 0.5, ease: 'power4.out',
							height: '72px', width: '350px', 
							boxShadow:'0px 0px 30px 5px rgba(128, 128, 128, 0.25)',
							borderRadius: "20px",
							})
			}
			this.$gsap.to(".avatar img", {
						duration: 0.5, ease: 'power4.out',
						top: "15px"
						})
		},
		mouseLeave () {
			this.$gsap.to(".avatar", {
						duration: 0.5, ease: 'power4.out',
						height: '40px', width: '40px', 
						boxShadow: '0px 0px 10px 2px rgba(128, 128, 128, 0.1)',
						borderRadius: '50%',
						})
			this.$gsap.to(".avatar img", {
						duration: 0.5, ease: 'power4.out',
						top: "0px"
						})
		},
	}
}
</script>

<style scoped>
.avatar {
	/* outline: #00ff00 dotted thick; */
	height: 40px;
	width: 40px;
	position: relative;
	backdrop-filter: blur(20px);
	background-color: rgba(255,255,255,0.5);
	z-index: 11;

	position: fixed;
	right: 30px;
	top: 3px;
	
	border-radius: 50%;
	border: #bfbec0 solid thin;
	
	box-shadow: 0px 0px 10px 2px rgba(128, 128, 128, 0.1);
	
	overflow: hidden;
}
.avatar img {
	height: 40px;
	width: 40px;
	
	border-radius: 50%;	
	position: relative;
}
.name {
	margin-left: 10px;
	position: relative;
}
.userTag {
  white-space: nowrap;
  text-align: center;

  font-size: 13px;

  background-color: #26BEB8;
  color: white;

  border-radius: 10px;

  padding: 2px 8px 2px 8px;
  margin: 3px;
}
</style>
