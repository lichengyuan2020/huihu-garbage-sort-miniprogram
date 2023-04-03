export default {
	// login: '/adminLogin',

	login: '/admin_login',
	logout: '/admin_logout',
	goodList: '/admin/product/list',
	upDownGood: '/admin/product/batchUpdateSellStatus',
	adminStatics: 'admin/order/statistics',
	getToken: '/loginWithJwt',

	picture_search_list: 'admin/search_picture_history/list',
	pictureDelete: 'admin/search_picture_history/delete',

	text_search_list: 'admin/search_txt_history/list',
	textDelete: 'admin/search_txt_history/delete',

	audio_search_list: 'admin/search_video_history/list',
	audioDelete: 'admin/search_video_history/delete',

	rubbishList: 'admin/rubbish/list',
	rubbishAdd: 'admin/rubbish/add',
	rubbishUpdate: 'admin/rubbish/update',
	rubbishDelete: 'admin/rubbish/delete',
	rubbishSearch: 'admin/rubbish/search',

	userList: '/admin/user/list',
	userUpdate: '/admin/user/update',
	userDelete: '/admin/user/delete',

	charts_rubbish_times: 'admin/rubbish_times',
	charts_rubbish_week: 'admin/user_times',
	charts_rubbish_exam: 'admin/test_accuary',
	charts_rubbish_exam_last: 'admin/user_accuary',

	charts_title: 'admin/total',

	getLog: '/getLog',
};
