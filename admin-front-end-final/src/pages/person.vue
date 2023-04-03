<template>
	<div class="box-card-container">
		<div class="btn-wrapper">
			<div class="page-title">基本信息</div>
		</div>
		<div class="box-card">
			<el-form ref="form" :model="form" label-width="80px">
				<el-form-item label="用户名">
					<el-input disabled v-model="form.username"></el-input>
				</el-form-item>
				<el-form-item label="个性签名">
					<el-input
						disabled
						v-model="form.personalizedSignature"
					></el-input>
				</el-form-item>
			</el-form>
		</div>
	</div>
</template>

<script>
/* eslint-disable */
import header from '../components/header';
export default {
	data() {
		return {
			form: {
				username: localStorage.getItem('username'),
				personalizedSignature: localStorage.getItem(
					'personalizedSignature'
				),
			},
		};
	},
	components: {
		header,
	},
	created() {},
	methods: {},
};
</script>

<style lang="less">
.box-card {
	margin: 20px;
}
.btn-wrapper {
	display: flex;
	justify-content: space-between;
	align-items: center;
	padding: 21px 28px;
	height: 64px;
	background: #ffffff;
	.page-name {
		margin-left: 20px;
	}
}
.box-card-container {
	flex: 1;
	height: 100vh;
}
.page-title {
	margin-left: 20px;
	font-family: PingFangSC-Semibold;
	font-size: 16px;
	color: #545c63;
	font-weight: 600;
}
.box-card {
	width: 400px;
	background: #f4f5f8;
	border: 1px solid #f4f5f8;
	margin: 0 auto;
	padding: 40px;
}
.box-card-container {
	background: #fff;
}
</style>
