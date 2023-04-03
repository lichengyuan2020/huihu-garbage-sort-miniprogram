// app.js
import * as db from './utils/db.js';
import * as util from './utils/util.js';
import { formatTime } from 'utils/util.js';
const defaultAvatarUrl = 'https://mmbiz.qpic.cn/mmbiz/icTdbqWNOwNRna42FI242Lcia07jQodd2FJGIYQfG0LAJGFxM4FbnQP6yfMxBgJ0F3YRqJCJ1aPAK2dQagdusBZg/0'
// let userInfo = db.get("userInfo") || {}
App({
    globalData: {
        opedid:null,
        //web_server_base_url: 'http://192.168.137.54:5000',//
        web_server_base_url:'http://garbage1234.nat300.top',
        avatarUrl: defaultAvatarUrl,
        Nickname:'微信用户',
        isLogin:false,
        examCount:0,
        examPoints:0
    },
  
  applogin:function(){
    /*获取openid、头像、昵称*/
    let that=this;
    wx.login({
      success:(res)=>{
        console.log("用户code:"+res.code);
        wx.request({
          url: this.globalData.web_server_base_url+'/login',
          header:{
            'content-type': 'application/json'
          },
          method:'POST',
          data:{
            "code":res.code,
            "log_time":formatTime(new Date())
          },
          success:function(res1){
            //const result=JSON.stringify(res1.data)
            //const {code,opedid}=result;
            console.log(res1.data);
            that.globalData.openid=res1.data.openid;
            console.log(that.globalData.openid);
            that.globalData.isLogin = true;
            that.globalData.avatarUrl = that.globalData.web_server_base_url + res1.data.avatar;
            that.globalData.Nickname = res1.data.name;
            that.globalData.examCount = res1.data.times;
            that.globalData.examPoints = res1.data.score;
          }
        }) 
      }
    })
    /*获取openidd、头像、昵称结束*/
  },
  
  onLaunch() {
    this.applogin();
    // wx.checkSession({
    //     success: res => {
    //       console.log('success: checkSession ----> ')
    //     },
    //     fail: res => {
    //         // 登录
    //         console.log('fail: login ----> ')
    //         wx.login({
    //             success: res => {
    //                 console.log(res)  // 获取code
    //                 // 发送 res.code 到后台获取openId
    //                 if (res.code) {
    //                     // 发起网络请求
    //                     wx.request({
    //                         url: web_server_base_url + '/login',
    //                         data: { code: res.code },
    //                         header: {'content-type': 'application/json'},
    //                         success: res => {
    //                             console.log('------', res.data)
    //                             console.log('--&&&&&----', res)
    //                             // 缓存open_id小程序本地
    //                             // wx.setStorageSync('open_id', res.data.open_id); //把名字存到缓存
    //                             wx.navigateTo({
    //                                 url: '/pages/index/index',
    //                             })
    //                         }
    //                     })
    //                 } else {
    //                     console.log('登录失败！' + res.errMsg)
    //                 }
    //             }
    //         })
    //     }
    //   })
  },
  $db: db,
  $util: util,
})
