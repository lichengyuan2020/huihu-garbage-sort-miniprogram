<template>
	<div class="login_page fillcontain">
		<video
			poster="../assets/video-cover.jpeg"
			style="
				width: 100%;
				height: 100%;
				position: absolute;
				margin: 0px;
				padding: -1;
				object-fit: cover;
			"
			loop
			autoplay
			muted
		>
			<source src="../assets/night.mp4" />
		</video>

		<section class="card" v-show="showLogin" style="position: fixed">
			<div class="left"></div>
			<el-form :model="loginForm" :rules="rules" ref="loginForm">
				<div class="welcom">慧湖垃圾通-管理系统登录</div>

				<el-form-item prop="username">
					<el-input
						class="login-item"
						v-model="loginForm.username"
						placeholder="请输入用户名"
					></el-input>
				</el-form-item>

				<el-form-item prop="password">
					<el-input
						class="login-item"
						type="password"
						placeholder="请输入密码"
						v-model="loginForm.password"
					></el-input>
				</el-form-item>

				<el-form-item>
					<center>
						<el-button
							type="primary"
							@click="submitForm('loginForm')"
							>登录</el-button
						>
					</center>
				</el-form-item>
			</el-form>
		</section>
	</div>
</template>

<script>
/* eslint-disable */
import http from './http';
import api from './_api';

export default {
	data() {
		return {
			loginForm: {
				username: '',
				password: '',
			},
			rules: {
				username: [
					{
						required: true,
						message: '请输入用户名',
						trigger: 'blur',
					},
				],
				password: [
					{ required: true, message: '请输入密码', trigger: 'blur' },
				],
			},
			showLogin: false,
		};
	},
	mounted() {
		this.showLogin = true;
	},
	computed: {},
	methods: {
		async submitForm(formName) {
			this.$refs[formName].validate(async (valid) => {
				if (valid) {
					// const res = await login({user_name: this.loginForm.username, password: this.loginForm.password})

					http.get(api.login, {
						userName: this.loginForm.username,
						password: this.loginForm.password,
					}).then((res) => {
						if (res.code === 1) {
							this.$router.push('picture');
						} else {
							this.$message({
								type: 'error',
								message: res.msg,
							});
						}
					});
				} else {
					this.$notify.error({
						title: '错误',
						message: '请输入正确的用户名密码',
						offset: 100,
					});
					return false;
				}
			});
		},
	},
};
</script>

<style lang="less">
.login_page {
	background-size: contain;
	background-repeat: no-repeat;
	background-position: top;
	height: 100vh;
	display: flex;
	align-items: center;
	justify-content: center;
}
.welcom {
	font-size: 24px;
	color: #cc6a7c;
	line-height: 90px;
	font-weight: 600;
	margin-top: 5px;
	text-align: left;
	margin-bottom: 8px;
}
.manage_tip {
	width: 100%;
	top: -100px;
	left: 0;
	p {
		font-size: 20px;
		font-weight: 700;
		color: #e4393c;
	}
}
.card {
	// background: #ffffff;
	box-shadow: 0px 8px 16px 0px rgba(0, 0, 0, 0.05);
	border-radius: 8px;
	display: flex;
	padding: 30px;
	background: rgb1(133, 158, 162, 0.1);
	box-shadow: 0px 8px 16px 0px rgba(0, 0, 0, 0.2);
	.left {
		display: flex;
		flex-direction: column;
	}
}
.form_contianer {
	// .wh(320px, 210px);
	// .ctp(320px, 210px);
	top: auto !important;
	border: 1px solid #eee;
	padding: 24px;
	left: auto;
	height: auto;
	border-radius: 5px;
	text-align: center;
	background-color: #fff;
}
.tip {
	font-size: 12px;
	color: red;
}

.welcom-tip {
	font-family: PingFangSC-Regular;
	font-size: 16px;
	color: #9199a1;
	line-height: 24px;
	font-weight: 400;
	text-align: left;
	padding-bottom: 24px;
}
.login-item,
.el-form-item__content {
	display: flex;
	align-items: center;
	justify-content: space-between;
	span {
		flex: none;
		width: 70px;
	}
}
.input-wrapper {
	width: 320px;
	height: 48px;
	border-radius: 8px;
}
.submit_btn {
	width: 320px;
	height: 48px;
	// background: rgba(0,139,255,0.30);
	border-radius: 8px;
}

// .login-item {
// 	background-color: transparent !important;
// 	/* 使边框也变透明 */
// 	border-color: transparent;
// 	/* 给边框加阴影能够使其有立体感 */
// 	box-shadow: 2px 2px 0 0 rgba(0, 0, 0, 0.2);
// 	/* 改变获取焦点后的竖线颜色 */
// 	caret-color: rgba(0, 255, 255, 0.8);
// 	color: #ffffff !important;
// }

.login_page {
	.el-form-item__label {
		/* 给el-form组件的label标签颜色修改 */
		color: #ffffff;
	}

	.el-input__inner {
		/* 使input框的背景变透明 */
		background-color: transparent !important;
		/* 使边框也变透明 */
		border-color: transparent;
		/* 给边框加阴影能够使其有立体感 */
		box-shadow: 2px 2px 0 0 rgba(0, 0, 0, 0.2);
		/* 改变获取焦点后的竖线颜色 */
		caret-color: rgba(0, 255, 255, 0.8);
		color: #ffffff !important;
	}

	.el-input__inner:hover {
		border-color: rgb(0, 255, 255);
	}

	.el-input__inner:focus {
		border-color: aqua;
	}
}
</style>
