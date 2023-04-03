<template>
	<div class="manage_page fillcontain">
		<Header></Header>
		<div class="main-grid">
			<el-menu
				:default-active="defaultActive"
				class="menu"
				style="min-height: 100%"
				theme="dark"
				router
			>
				<el-menu-item index="picture"
					><span class="material-symbols-rounded"> party_mode </span
					>拍照搜索记录</el-menu-item
				>
				<el-menu-item index="text"
					><span class="material-symbols-rounded">find_in_page</span
					>文本搜索记录</el-menu-item
				>
				<el-menu-item index="voice"
					><span class="material-symbols-rounded"
						>auto_detect_voice</span
					>语音搜索管理</el-menu-item
				>
				<el-menu-item index="person" class="hidden"
					><span class="material-symbols-rounded"> person </span
					>个人信息</el-menu-item
				>
				<el-menu-item index="statistic"
					><span class="material-symbols-rounded">bar_chart</span
					>统计数据</el-menu-item
				>
				<el-menu-item index="user"
					><span class="material-symbols-rounded">
						account_circle </span
					>用户管理</el-menu-item
				>
				<el-menu-item index="rubbish"
					><span class="material-symbols-rounded"> delete </span
					>垃圾管理</el-menu-item
				>
				<!-- <el-menu-item index="log"
					><span class="material-symbols-rounded">dvr</span
					>系统日志</el-menu-item
				> -->
			</el-menu>
			<router-view class="content"></router-view>
		</div>
		<div class="page" style="height: 100%"></div>
	</div>
</template>

<script>
import Header from '../components/header.vue';
/* eslint-disable */
export default {
	computed: {
		defaultActive: function () {
			return this.$route.path.replace('/', '');
		},
	},
	components: {
		Header,
	},
};
</script>
<style lang="scss" scoped>
:root {
	--sidebar-width: 200px;
}

.page {
	padding: 0;
}

.main-grid {
	// display: grid;
	grid-template-columns: 1fr 3fr;
}

.menu {
	// grid-column: 1;
	// width: 200px;
	position: fixed;
	width: 180px;
	padding: 14px;
	background-color: white;
	border-right: none;
	z-index: 50;
	filter: drop-shadow(0 0 4px rgba(0, 0, 0, 0.05));

	.el-menu-item {
		border-radius: 12px;
	}
	.material-symbols-rounded {
		margin-right: 16px;
	}
}

.content {
	width: calc(100% - 212px); // 212px = 180px + 2 * 16px(padding)
	margin-left: 212px;
}

.fillcontain {
	flex: 1;
}
</style>
