import axios from 'axios';

// let host = "localhost";
// let port = 8083;
// let domain = `http://${host}:${port}/`

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
	// 如果code异常(这里已经包括网络错误，服务器错误，后端抛出的错误)，可以弹出一个错误提示，告诉用户
	if (res.status === -404) {
		// message.error('为保证数据正确，本系统仅用于演示后台显示功能，已将修改相关功能关闭');
		return;
	}
	if (res.status === 9999) {
		// message.error('请重新登录');

		return;
	}

	if (res.status === 10007) {
		// message.error('请重新登录');
		console.log(window.location);
		// window.open(window.host+'/login');
		// window.location.href = window.location.origin+'/login';
		window.location.href = 'http://localhost/admin/#/';

		return;
	}

	// console.log('location:',window.location);

	if (res.status !== 10000) {
		// message.error(res.errorMsg);
	}
	return res;
}

export default {
	post(url, data) {
		// if(!sessionStorage.getItem('token')){
		//   window.location.href = 'http://localhost/admin/#/';
		// }
		return axios(
			{
				method: 'POST',
				baseURL: domain,
				url,
				// data: JSON.stringify(data),
				data: JSON.stringify(data),
				timeout: 10000,
				headers: {
					'X-Requested-With': 'XMLHttpRequest',
					'Content-Type': 'application/json; charset=UTF-8',
					jwt_token: sessionStorage.getItem('token') || null,
					// 'jwt_token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX3JvbGUiOjIsInVzZXJfaWQiOjEyLCJ1c2VyX25hbWUiOiJtdW11NCIsImV4cCI6MTcwNjA5OTk1NH0.FS_i3-0Ai7fRm16fvc_nX6GMxFq_dY78Qg7XgkLTl7o'
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
					// 'jwt_token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX3JvbGUiOjIsInVzZXJfaWQiOjEyLCJ1c2VyX25hbWUiOiJtdW11NCIsImV4cCI6MTcwNjA5OTk1NH0.FS_i3-0Ai7fRm16fvc_nX6GMxFq_dY78Qg7XgkLTl7o'
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
};
