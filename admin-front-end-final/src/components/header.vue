<template>
	<div class="header">
		<el-menu
			:default-active="activeIndex"
			class="el-menu-demo"
			mode="horizontal"
		>
			<el-menu-item index="1">"慧湖垃圾通"后台管理系统</el-menu-item>
			<el-button @click="signout" class="float-right mt-2 mr-4"
				>退出登录</el-button
			>
		</el-menu>

		<div class="header-left" style="display: none">
			<img width="50" src="../assets/micon.png" alt="" />
			<span class="page-name">"慧湖垃圾通" 后台管理系统</span>
		</div>
		<div class="right" style="display: none">
			<a
				class="page-name-yes"
				target="_blank"
				href="http://localhost/#/index"
				>"慧湖垃圾通"</a
			>
			<el-dropdown @command="handleCommand" menu-align="start">
				<img
					width="32"
					height="32"
					class="avator"
					src="../assets/person.png"
					alt=""
				/>
				<template #dropdown>
					<el-dropdown-menu>
						<el-dropdown-item command="home">
							<a target="_blank" href="http://localhost/#/index"
								>"慧湖垃圾通"首页</a
							>
						</el-dropdown-item>
						<el-dropdown-item command="signout"
							>退出登陆</el-dropdown-item
						>
					</el-dropdown-menu>
				</template>
			</el-dropdown>
		</div>
	</div>
</template>

<script>
import http from '../pages/http';
import api from '../pages/_api';

export default {
	data() {
		return {
			activeIndex: '1',
		};
	},
	props: ['text'],
	created() {},
	computed: {},
	methods: {
		async handleCommand(command) {
			if (command == 'signout') {
				this.signout();
			}
		},
		signout() {
			http.post(api.logout).then((res) => {
				if (res.code === 1) {
					sessionStorage.setItem('token', null);
					window.location.href = '/#/';
				} else {
					this.$message({
						type: 'error',
						message: res.msg,
					});
				}
			});
		},
	},
};
</script>

<style lang="less">
.header {
	display: flex;
	position: sticky;
	top: 0;
	justify-content: space-between;
	align-items: center;
	height: 64px;
	z-index: 100;
	filter: drop-shadow(0px 0px 6px rgba(0, 0, 0, 0.08));
	.el-menu-demo {
		width: 100%;
	}
}

.avator {
	cursor: pointer;
	border-radius: 50%;
	margin-left: 37px;
}

.el-dropdown-menu__item {
	text-align: center;
}

.header-left {
	display: flex;
	align-items: center;
	a {
		color: #409eff;
		text-decoration: none;
	}
	img {
		width: 25px;
		height: 25px;
		margin-right: 20px;
	}
}

.page-name,
.page-name-yes {
	font-family: PingFangSC-Regular;
	font-size: 16px;
	text-align: left;
	font-weight: 400;
	text-decoration: none;
}

.right {
	display: flex;
	align-items: center;
}
</style>
