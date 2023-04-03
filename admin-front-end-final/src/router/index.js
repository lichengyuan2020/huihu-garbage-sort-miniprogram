import { createRouter, createWebHashHistory } from 'vue-router';
import login from '../pages/login.vue';
import picture_search from '../pages/picture_search.vue';
import manage from '../pages/manage.vue';
import voice from '../pages/voice.vue';
import person from '../pages/person.vue';
import user from '../pages/user.vue';
import statistic from '../pages/statistic';
import log from '../pages/log';
import text from '../pages/text.vue';
import rubbish from '../pages/rubbish.vue';

const routes = [
	{
		path: '/',
		name: 'login',
		component: login,
	},
	{
		path: '/manage',
		component: manage,
		name: '',
		children: [
			{
				path: '/text',
				component: text,
			},
			{
				path: '/picture',
				component: picture_search,
			},
			{
				path: '/person',
				component: person,
			},
			{
				path: '/voice',
				component: voice,
			},
			{
				path: '/user',
				component: user,
			},
			{
				path: '/statistic',
				component: statistic,
			},
			{
				path: '/log',
				component: log,
			},
			{
				path: '/rubbish',
				component: rubbish,
			},
		],
	},
];

const router = createRouter({
	history: createWebHashHistory(process.env.BASE_URL),
	routes,
});

export default router;
