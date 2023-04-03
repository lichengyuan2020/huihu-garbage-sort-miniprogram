import axios from 'axios';

//连接本地后端
// let host = 'localhost';
// let port = 8083;
// let domain = `http://${host}:${port}/`;

//连接旭升后端
let host = 'http://garbage1234.nat300.top';
let domain = `${host}`;

axios.interceptors.request.use(
	(config) => {
		return config;
	},
	(error) => {
		return Promise.reject(error);
	}
);

axios.interceptors.response.use(
	(response) => {
		return response;
	},
	(error) => {
		return Promise.resolve(error.response);
	}
);

axios.defaults.withCredentials = true;

function checkStatus(response) {
	// loading
	// 如果http状态码正常，则直接返回数据
	if (
		response &&
		(response.status === 200 ||
			response.status === 304 ||
			response.status === 400)
	) {
		return response.data;
		// 如果不需要除了data之外的数据，可以直接 return response.data
	}
	// 异常状态下，把错误信息返回去
	return {
		status: -404,
		msg: '网络异常',
	};
}

function checkCode(res) {
	if (res.status === -404) {
		// message.error('为保证数据正确，本系统仅用于演示后台显示功能，已将修改相关功能关闭');
		return;
	}

	if (res.status === 10007) {
		// message.error('请重新登录');
		window.location.href = 'http://localhost/admin/#/';
		return;
	}

	if (res.status === 9999) {
		// message.error('请重新登录');

		return;
	}
	if (res.status !== 10000) {
		// message.error(res.errorMsg);
	}
	return res;
}

export default {
	post(url, params) {
		// if(!sessionStorage.getItem('token')){
		//   window.location.href = 'http://localhost/admin/#/';
		// }
		return axios(
			{
				method: 'POST',
				baseURL: domain,
				url,
				// data: JSON.stringify(data),
				params: params,
				timeout: 10000,
				headers: {
					'X-Requested-With': 'XMLHttpRequest',
					jwt_token: sessionStorage.getItem('token') || null,
				},
				withCredentials: true,
				// credentials: 'same-origin',
			},
			{ withCredentials: true }
		)
			.then((response) => {
				return checkStatus(response);
			})
			.then((res) => {
				return checkCode(res);
			});
	},
	get(url, params) {
		// if(!sessionStorage.getItem('token')){
		//   window.location.href = 'http://localhost/admin/#/';
		// }
		return axios(
			{
				method: 'get',
				baseURL: domain,
				url,
				params, // get 请求时带的参数
				timeout: 10000,
				headers: {
					'X-Requested-With': 'XMLHttpRequest',
					jwt_token: sessionStorage.getItem('token') || null,
				},
				withCredentials: true,
			},
			{ withCredentials: true }
		)
			.then((response) => {
				return checkStatus(response);
			})
			.then((res) => {
				return checkCode(res);
			});
	},
};
