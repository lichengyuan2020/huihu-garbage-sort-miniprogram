// pages/user/user.js
// 获取应用单例
const app = getApp()
import { formatTime } from './../../utils/util.js';
// 默认头像
const defaultAvatarUrl = 'https://mmbiz.qpic.cn/mmbiz/icTdbqWNOwNRna42FI242Lcia07jQodd2FJGIYQfG0LAJGFxM4FbnQP6yfMxBgJ0F3YRqJCJ1aPAK2dQagdusBZg/0'

Page({
    /**
     * 页面的初始数据
     */
    data: {
        h_list: [
          {
            id: 'rank',
            name: '答题排行榜',
            topage:'exam-ranking',
            img:'../../images/rank.png'
          },{
            id: 'e-his',
            name: '答题历史',
            topage:'exam-history',
            img:'../../images/exam_selected.png'
          }, {
            id: 't-his',
            name: '文本搜索历史',
            topage:'text-history',
            img:'../../images/search-text.png'
          }, {
            id: 'v-his',
            name: '语音搜索历史',
            topage:'voice-history',
            img:'../../images/speech.png'
          }, {
            id: 'i-his',
            name: '拍照搜索历史',
            topage:'image-history',
            img:'../../images/paizhao.png'
          }, 
        ],
        avatarUrl: defaultAvatarUrl,
        Nickname: '微信用户A',
        userInfo: {},
        userProfileConfig: [
        // { text: '创作', key: 'articlesCount' },
        { text: '答题次数', key: 'examCount' },
        { text: '答题积分', key: 'examPoints' },
        { text: '答题排名', key: 'examRank' },
        ],
        // navHeight: 0,
        // visible: false,
      },
    // onChooseAvatar(e) {
    //   const { avatarUrl } = e.detail 
    //   this.setData({
    //     avatarUrl: avatarUrl
    //   })
    // },
    onSetNickname(e){
        console.log(e.detail.value)
    },
    getUserInfo: function () {
      this.setData({
        userInfo: {
          // id: 1,
          // articlesCount: 2,
          examCount: app.globalData.examCount,
          examPoints: app.globalData.examPoints,
          // examRank: app,
        }
      })
    },
  toRank(){
    wx.navigateTo({
      url: './exam-ranking/exam-ranking',
    })
  },
  toHistory(){
    wx.navigateTo({
      url: './exam-history/exam-history',
    })
  },
    //获取排名
  getRanking() {
    let that = this;
    // wx.showLoading({
    //   title: '加载中...',
    // })
    wx.request({
      url: app.globalData.web_server_base_url+'/user_rank',
      data: {
        "code": "1",
        "openid":app.globalData.openid
      },
      header: {
          'Content-Type': 'application/json'
      },
      method: "POST",
      //请求成功
      success: function (res) {
        if(res.data!=null){
          console.log(res.data);
          let resData = res.data.me.rank;
          console.log(resData);
          // that.rankListReform(resData);
          that.setData({
            userInfo:{
              examCount: app.globalData.examCount,
              examPoints: app.globalData.examPoints,
              examRank: resData,}
          });
          // wx.hideLoading()
        }
      }
    })

  },
    handleBack: function () {
      this.pageRouter.switchTab({
        url: '../list/list'
      })
    },
    /**
     * 生命周期函数--监听页面加载
     */
    onLoad: function (options) {
        console.log('00000000000')
    //   this.applogin();
    //   this.getUserInfo();
      this.setData({
        avatarUrl:app.globalData.avatarUrl,
        Nickname:app.globalData.Nickname
      })
    },
    handleOpen: function () {
        this.setData({
            visible: true
        })
    },
    handleClose: function () {
      this.setData({
        visible: false
      })
    },
    pagetochange(e){
          app.$util.navigateTo(`/pages/me/changeAvaNick/changeAvaNick`)
    },
    pagetoHistory(e) {
        let {
          page
        } = e.currentTarget.dataset
        app.$util.navigateTo(`/pages/me/${page}/${page}`)//app.$util
      },

    onShow(){
        console.log('99999999999')
        // this.getUserInfo();
        this.getRanking();
        this.setData({
            avatarUrl:app.globalData.avatarUrl,
            Nickname: app.globalData.Nickname,
            examCount:app.globalData.examCount,
            examPoints:app.globalData.examPoints
        })
    }
  })