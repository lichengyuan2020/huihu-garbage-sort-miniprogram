const app = getApp()
import { formatTime } from './../../utils/util.js';
Page({
 data: {
     rubbish_name:'铁',
     resList: [
        { code: 1, rubbish_name: 'MySQL HeatWave', rubbish_class: 'MySQL数据库服务' },
        { code: 2, rubbish_name: 'MySQL Cluster CGE', rubbish_class: '凭借无可比拟的扩展能' },
      ],
      isScroll:false,
      more_text:''

 },
//  onfocus: function() {
//   this.setData({isScroll: true})
//   },
//   onblur: function () {
//     this.setData({isScroll: true})
//  },
 
 onLoad(lastpage){
  this.setData({more_text: lastpage.more_text});
 },

 redirectToHome: function() {
    this.pageRouter.switchTab({
      url: '../exam/exam'
    })
  },
  redirectToBack: function() {
    this.pageRouter.navigateBack()
    {
        url: '../exam/exam'
    }
  },
 
 //执行点击事件
 formSubmit: function (e) {
 
  //声明当天执行的
  var that = this;
 
  //获取表单所有name=keyword的值
  console.log(e.detail.value.keyword.length)
  var formData = (e.detail.value.keyword.length==0?that.data.more_text:e.detail.value.keyword);
  console.log(!formData==undefined)
 
  //显示搜索中的提示
  wx.showLoading({
   title: '搜索中',
   icon: 'loading'
  })
 if(formData!=undefined){
  //向搜索后端服务器发起请求
  wx.request({
 
   //URL
   url: app.globalData.web_server_base_url + '/rubbish_search_txt',
   //发送的数据
   data: {rubbish_name:formData,openid:app.globalData.openid,search_time:formatTime(new Date())},
 
   //请求的数据时JSON格式
   header: {
    'Content-Type':'application/json'
   },
   method:"POST",
   //请求成功
   success: function (res) {
 
    //控制台打印（开发调试用）
    console.log(res.data)
 
    //把所有结果存进一个名为re的数组
    that.setData({
        re:res.data,
    })
    //搜索成功后，隐藏搜索中的提示
    wx.hideLoading();
   }
  })
  }
  else{wx.hideLoading();}
 },
})