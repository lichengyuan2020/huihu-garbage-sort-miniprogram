<template>
	<div class="fillcontain">
		<div class="btn-wrapper">
			<div class="page-title">拍照搜索记录管理</div>
			<div class="btn-top-wrapper"></div>
		</div>
		<div class="table-container">
			<el-table
				:fit="true"
				ref="multipleTable"
				:data="tableData"
				:row-key="(row) => row.index"
				@selection-change="handleSelectionChange"
				style="width: 100%"
			>
				<el-table-column type="selection"> </el-table-column>
				<el-table-column label="OpenID" prop="openid">
				</el-table-column>
				<el-table-column label="用户昵称" prop="name">
				</el-table-column>
				<el-table-column label="拍摄图片" prop="input">
					<template #default="scope">
						<img
							class="product-img"
							:src="
								'http://garbage1234.nat300.top' +
								scope.row.input
							"
							alt=""
						/>
					</template>
				</el-table-column>
				<el-table-column label="垃圾名称" prop="result">
				</el-table-column>
				<el-table-column label="垃圾类别" prop="result_class">
				</el-table-column>
				<!-- <el-table-column label="用户类型" prop="role">
					<template #default="scope">
						<el-tag v-if="scope.row.role === 1" type="info"
							>普通用户</el-tag
						>
						<el-tag v-if="scope.row.role === 2">管理员</el-tag>
					</template>
				</el-table-column> -->
				<el-table-column label="拍照时间" prop="search_time">
					<template #default="scope">
						<div>{{ scope.row.search_time }}</div>
					</template>
				</el-table-column>
				<el-table-column
					label="操作"
					prop="status"
					class="flex flex-row gap-4"
				>
					<template #default="scope">
						<div v-if="scope.row.role === 1">
							<!-- <el-popconfirm
								title="请确定是否重置密码"
								@confirm="handleResetPasswd(scope.row)"
							>
								<template #reference>
									<el-button
										class="btn-delete"
										type="primary"
										plain
										>重置密码</el-button
									>
								</template>
							</el-popconfirm> -->
							<!-- <el-button
								@click="handleEdit(scope.row)"
								type="primary"
								plain
								class="mr-2"
								>修改</el-button
							> -->
							<el-popconfirm
								title="请确定是否删除此记录"
								@confirm="handleDelete(scope.row)"
							>
								<template #reference>
									<el-button
										class="btn-delete"
										type="danger"
										plain
									>
										删除
									</el-button>
								</template>
							</el-popconfirm>
						</div>
					</template>
				</el-table-column>
			</el-table>
			<div class="pagination-wrapper" style="text-align: left">
				<el-pagination
					@size-change="handleSizeChange"
					@current-change="handleCurrentChange"
					:current-page="currentPage"
					:page-size="10"
					layout="total, prev, pager, next"
					:total="count"
				>
				</el-pagination>
			</div>
		</div>
		<!-- <el-dialog
			:title="isEdit ? '编辑用户' : '新增用户'"
			v-model="dialogVisible"
			width="30%"
		>
			<el-form ref="form" :model="form" label-width="80px">
				<el-form-item label="用户ID">
					<el-input v-model="form.openid" disabled></el-input>
				</el-form-item>
				<el-form-item label="注册时间">
					<el-input v-model="form.log_time" disabled></el-input>
				</el-form-item>

				<el-form-item label="用户昵称">
					<el-input v-model="form.name"></el-input>
					</el-form-item>
				<el-form-item label="用户签名"> 
					<el-input placeholder="" v-model="form.name"></el-input>
				</el-form-item> 
			</el-form>
			<template #footer>
				<div class="dialog-footer">
					<el-button @click="dialogVisible = false">取消</el-button>
					<el-button type="primary" @click="update">确定</el-button>
				</div>
			</template>
		</el-dialog> -->
	</div>
</template>

<script>
/* eslint-disable */
import header from '../components/header';
import http from './http';
import http2 from './http2';
import api from './_api';
import moment from 'moment';

export default {
	data() {
		return {
			dialogVisible: false,
			tableData: [],
			count: 0,
			currentPage: 1,
			selectedIds: [],
			isEdit: false,
			tree: [],
			form: {
				openid: null,
				name: null,
				input: null,
				search_time: null,
				result: null,
				result_class: null,
				role: null,
			},
		};
	},
	components: {
		header,
	},
	created() {},
	mounted() {
		this.initData();
	},
	methods: {
		getHeader() {
			return {
				jwt_token: sessionStorage.getItem('token') || null,
			};
		},
		handleDelete(row) {
			http2
				.post(api.pictureDelete + '?openid=' + row.openid, {
					openid: row.openid,
					search_time: row.search_time,
				})
				.then((res) => {
					if (res.code === 1) {
						this.$message({
							type: 'success',
							message: '删除成功',
						});
						this.initData();
					} else {
						this.$message({
							type: 'error',
							message: res.msg,
						});
					}
				});
		},
		handleChange(v) {
			console.log('vvv:', v);
		},
		handleAvatarSuccess(res, file) {
			if (res.status === 10000) {
				this.form.imageUrl = res.data;
				this.$message({
					type: 'success',
					message: '上传成功',
				});
			} else {
				this.$message({
					type: 'error',
					message: res.msg,
				});
			}
		},

		handleAdd() {
			this.dialogVisible = true;
			this.isEdit = false;
			this.form.name = null;
			this.form.detail = null;
			this.form.stock = null;
			this.form.price = null;
			this.form.imageUrl = null;
			this.form.openid = null;
			this.form.value = null;
		},
		update() {
			console.log('form:', this.form);
			http2
				.post(api.userUpdate, {
					name: this.form.name,
					// personalizedSignature: this.form.personalizedSignature,
					// avatar: this.form.avatar,
					openid: this.form.openid,
					log_time: this.log_time,
				})
				.then((res) => {
					if (res.code === 1) {
						this.dialogVisible = false;
						this.initData();
						this.$message({
							type: 'success',
							message: `${this.isEdit ? '编辑成功' : '新增成功'}`,
						});
					} else {
						this.$message({
							type: 'error',
							message: res.msg,
						});
					}
				});
		},
		handleResetPasswd(row) {
			http2
				.post(api.userResetPasswd + '?openid=' + row.openid, {})
				.then((res) => {
					if (res.status === 10000) {
						this.initData();
						this.$message({
							type: 'success',
							message: '重置密码成功',
						});
					} else {
						this.$message({
							type: 'error',
							message: res.msg,
						});
					}
				});
		},
		handleEdit(row) {
			console.log('row:', row);
			this.isEdit = true;
			this.form.openid = row.openid;
			this.form.name = row.name;
			this.form.avatar = row.avatar;
			this.form.personalizedSignature = row.personalizedSignature;
			this.form.log_time = row.log_time;
			this.dialogVisible = true;
		},
		// handleDelete(row) {
		// 	http2
		// 		.post(api.pictureDelete + '?openid=' + row.openid, {
		// 			openid: row.openid,
		// 			search_time:row.search_time,
		// 		})
		// 		.then((res) => {
		// 			if (res.code === 1) {
		// 				this.initData();
		// 				this.$message({
		// 					type: 'success',
		// 					message: '删除成功!',
		// 				});
		// 			} else {
		// 				this.$message({
		// 					type: 'error',
		// 					message: res.msg,
		// 				});
		// 			}
		// 		});
		// },
		timeFormat(t) {
			return moment(t).format('YYYY-MM-DD HH:mm:ss');
		},
		handleSelectionChange(val) {
			console.log('value:::', val);
			this.selectedIds = val;
		},
		async initData() {
			http.get(api.picture_search_list, {
				pageNum: this.currentPage,
				pageSize: 10,
			}).then((res) => {
				this.tableData = res.data.list;
				this.count = res.data.total;
			});
			//   this.tableData = [{
			//       id: 1,
			//       name: 'root',
			//       signature: 'sig_1',
			//       avatar: '1145141919@qq.com',
			//       role: 2,
			//       log_time: '2022-11-15 23:47:23'
			//   }, {
			//       id: 2,
			//       name: 'alice',
			//       signature: 'sig_2',
			//       avatar: 'alice@example.com',
			//       role: 1,
			//       log_time: '2023-03-20 03:12:52'
			//   }]
		},
		handleSizeChange(val) {
			console.log(`每页 ${val} 条`);
		},
		handleCurrentChange(val) {
			this.currentPage = val;
			this.initData();
		},
		onSubmit() {},
	},
};
</script>

<style lang="less" scoped>
.btn-top-wrapper {
	margin-left: 20px;
	display: flex;
	align-items: center;
	gap: 8px;
}

.avatar-uploader {
	height: 40px;
}

.el-pagination {
	text-align: right;
}

.avatar-uploader-dialog {
	height: auto;
}

.avatar-uploader .el-upload {
	border: 1px dashed #d9d9d9;
	border-radius: 6px;
	cursor: pointer;
	position: relative;
	overflow: hidden;
}

.avatar-uploader .el-upload:hover {
	border-color: #409eff;
}

.avatar-uploader-icon {
	font-size: 28px;
	color: #8c939d;
	width: 178px;
	height: 178px;
	line-height: 178px;
	text-align: center;
	position: relative;

	&::before {
		top: 50%;
		left: 50%;
		position: absolute;
		transform: translate(-50%, -50%);
	}
}

.avatar-upload {
	width: 100px;
	height: 100px;
	display: block;
}

.btn-wrapper {
	display: flex;
	justify-content: space-between;
	align-items: center;
	padding: 21px 28px;
	height: 64px;
	background: #ffffff;

	.page-title {
		margin-left: 20px;
		font-family: PingFangSC-Semibold;
		font-size: 16px;
		color: #545c63;
		font-weight: 600;
	}
}

.el-cascader {
	width: 100%;
}

.table-container {
	margin-top: 10px;
}

.pagination-wrapper {
	background: #fff;
	height: 60px;
	display: flex;
	align-items: center;
	justify-content: center;
}

.btn-delete {
	margin-left: 0px !important;
}

.product-img {
	width: 90px;
	height: 160px;
	object-fit: cover;
	object-position: center;
	border-radius: 8px;
}
</style>
