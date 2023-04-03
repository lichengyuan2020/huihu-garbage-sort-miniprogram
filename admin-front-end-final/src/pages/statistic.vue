<template>
	<div class="bg-white fillcontain">
		<div class="grid grid-cols-3">
			<div
				class="flex items-center justify-center gap-2 text-red-500"
				style="padding: 12px"
			>
				<span class="material-symbols-rounded">group_add </span>
				<span>用户数量:</span>{{ user_number }}
			</div>
			<div
				class="flex items-center justify-center gap-2 text-pink-500"
				style="padding: 12px"
			>
				<span class="material-symbols-rounded"> star_half </span>
				<span>用户使用搜索功能总次数:</span>{{ search_number }}
			</div>
			<div
				class="flex items-center justify-center gap-2 text-indigo-500"
				style="padding: 12px"
			>
				<span class="material-symbols-rounded"> done_all </span>
				<span>用户答题总次数：</span>{{ test_number }}
			</div>
		</div>

		<el-divider style="width: 90%; margin: 10px auto"></el-divider>
		<div class="grid grid-cols-2 bg-white gird">
			<div class="chart_1">
				<div
					id="rubbish_times"
					:style="{ width: '100%', height: '100%' }"
				></div>
			</div>

			<div class="chart_2">
				<div
					id="rubbish_week"
					:style="{ width: '100%', height: '100%' }"
				></div>
			</div>

			<div class="chart_3">
				<div
					id="rubbish_exam"
					:style="{ width: '100%', height: '100%' }"
				></div>
			</div>

			<div class="chart_4">
				<div
					id="rubbish_exam_last"
					:style="{ width: '100%', height: '100%' }"
				></div>
			</div>
		</div>
	</div>
</template>

<script>
/* eslint-disable no-unused-vars */
import { ref } from 'vue';
import header from '../components/header';
import http from './http';
import http2 from './http2';
import api from './_api';
import moment from 'moment';

import * as echarts from 'echarts';
// import { timeStamp } from 'console';

// import header from '../components/header'
export default {
	data() {
		return {
			user_number: null,
			search_number: null,
			test_number: null,
		};
	},
	mounted() {
		this.rubbish_search_times();
		this.rubbish_search_week();
		this.rubbish_search_exam();
		this.rubbish_search_exam_last();
		this.title_data();
	},
	methods: {
		//接口方法
		rubbish_search_times() {
			http.get(api.charts_rubbish_times, {}).then((res) => {
				var chartDom = document.getElementById('rubbish_times');
				var myChart = echarts.init(chartDom);
				var option;
				chartDom.setAttribute('_echarts_instance_', ''); // 防止切换页面后返回图表不显示
				console.log(res.list);
				option = {
					title: {
						text: '常见垃圾搜索频率分布饼图',
						// subtext: 'Fake Data',
						left: 'center',
					},
					tooltip: {
						trigger: 'item',
						formatter: '{a} <br/>{b} : {c} ({d}%)',
					},
					legend: {
						// orient: 'vertical',
						left: 'center',
						bottom: 10,
					},
					series: [
						{
							name: '垃圾名称和频率',
							type: 'pie',
							radius: '50%',
							data: res.list,
							emphasis: {
								itemStyle: {
									shadowBlur: 10,
									shadowOffsetX: 0,
									shadowColor: 'rgba(0, 0, 0, 0.5)',
								},
							},
						},
					],
				};
				myChart.setOption(option); //通过setOption()方法生成图表
				window.addEventListener('resize', function () {
					myChart.resize(); //图表自适应的一个方法
				});
			});
		},
		rubbish_search_week() {
			http.get(api.charts_rubbish_week, {}).then((res) => {
				var chartDom = document.getElementById('rubbish_week');
				var myChart = echarts.init(chartDom);
				var option;
				// chartDom.setAttribute('_echarts_instance_', '');
				option = {
					title: {
						text: '用户最近一周搜索和考试次数统计柱状图',
						// subtext: 'Fake Data',
						left: 'center',
					},
					tooltip: {
						trigger: 'axis',
						axisPointer: {
							type: 'cross',
							crossStyle: {
								color: '#999',
							},
						},
					},
					toolbox: {
						feature: {
							dataView: { show: true, readOnly: false },
							magicType: { show: true, type: ['line', 'bar'] },
							restore: { show: true },
							saveAsImage: { show: true },
						},
					},
					legend: {
						data: ['picture', 'voice', 'text', 'exam', 'total'],
						left: 'center',
						bottom: 10,
					},
					xAxis: [
						{
							name: '日期',
							type: 'category',
							data: res.date,
							axisPointer: {
								type: 'shadow',
							},
						},
					],
					yAxis: [
						{
							type: 'value',
							name: '次数',
							min: 0,
							max: 100,
							interval: 5,
							axisLabel: {
								formatter: '{value}',
							},
						},
					],
					series: [
						{
							name: 'picture',
							type: 'bar',
							tooltip: {
								valueFormatter: function (value) {
									return value;
								},
							},
							data: res.picture_times,
						},
						{
							name: 'voice',
							type: 'bar',
							tooltip: {
								valueFormatter: function (value) {
									return value;
								},
							},
							data: res.video_times,
						},
						{
							name: 'text',
							type: 'bar',
							tooltip: {
								valueFormatter: function (value) {
									return value;
								},
							},
							data: res.txt_times,
						},
						{
							name: 'exam',
							type: 'bar',
							tooltip: {
								valueFormatter: function (value) {
									return value;
								},
							},
							data: res.test_times,
						},
						{
							name: 'total',
							type: 'line',
							tooltip: {
								valueFormatter: function (value) {
									return value;
								},
							},
							data: res.total,
						},
					],
				};
				myChart.setOption(option); //通过setOption()方法生成图表
				window.addEventListener('resize', function () {
					myChart.resize(); //图表自适应的一个方法
				});
			});
		},
		rubbish_search_exam() {
			http.get(api.charts_rubbish_exam, {}).then((res) => {
				var chartDom = document.getElementById('rubbish_exam');
				var myChart = echarts.init(chartDom);
				var option;
				option = {
					title: {
						text: '用户答题正误率分析雷达图',
						left: 'center',
						top: -5.5,
					},
					legend: {
						data: ['该类别答题准确率', '该类别答题错误率'],
						itemGap: 20,
						textStyle: {
							fontSize: 12,
						},
						left: 'center',
						bottom: -5,
					},
					radar: {
						// shape: 'circle',
						indicator: [
							{ name: '可回收物', max: 1 },
							{ name: '有害垃圾', max: 1 },
							{ name: '厨余垃圾', max: 1 },
							{ name: '其他垃圾', max: 1 },
						],
					},
					series: [
						{
							type: 'radar',
							data: [
								{
									value: res.false_rate,
									name: '该类别答题准确率',
								},
							],
							color: '#FF9900',
						},
						{
							type: 'radar',
							data: [
								{
									value: res.right_rate,
									name: '该类别答题错误率',
								},
							],
							color: '#3366FF',
						},
					],
				};
				myChart.setOption(option); //通过setOption()方法生成图表
				window.addEventListener('resize', function () {
					myChart.resize(); //图表自适应的一个方法
				});
			});
		},
		rubbish_search_exam_last() {
			http.get(api.charts_rubbish_exam_last, {}).then((res) => {
				var chartDom = document.getElementById('rubbish_exam_last');
				var myChart = echarts.init(chartDom);
				var option;
				// chartDOM.setAttribute('_echarts_instance_', ''); // 防止切换页面后返回图表不显示
				option = {
					title: {
						text: '用户答题正误次数统计直方图',
						left: 'center',
						top: 8,
					},
					tooltip: {
						trigger: 'axis',
						axisPointer: {
							type: 'shadow',
						},
					},
					legend: { left: 'center', bottom: -5.2 },
					grid: {
						left: '3%',
						right: '4%',
						bottom: '3%',
						containLabel: true,
					},
					xAxis: {
						name: '题',
						type: 'value',
						boundaryGap: [0, 0.01],
						axisLabel: {
							formatter: '{value} ',
						},
					},
					yAxis: {
						name: '用户名',
						type: 'category',
						data: res.users_name,
					},
					series: [
						{
							name: '答题正确数量',
							type: 'bar',
							data: res.users_right,
							color: '#339966',
						},
						{
							name: '答题错误数量',
							type: 'bar',
							data: res.users_false,
							color: '#FF6666',
						},
					],
				};
				myChart.setOption(option); //通过setOption()方法生成图表
				window.addEventListener('resize', function () {
					myChart.resize(); //图表自适应的一个方法
				});
			});
		},
		title_data() {
			http.get(api.charts_title, {}).then((res) => {
				this.user_number = res.user_number;
				this.search_number = res.search_number;
				this.test_number = res.test_number;
			});
		},
	},
};
</script>

<style scoped>
.chart_1 {
	/* width: 100%; */
	height: 42vh;
}
.chart_2 {
	/* width: 100%; */
	height: 42vh;
}

.chart_3 {
	/* width: 100%; */
	height: 42vh;
}
.chart_4 {
	/* width: 100%; */
	height: 42vh;
}
</style>
