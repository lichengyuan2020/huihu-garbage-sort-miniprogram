// pages/me/voice-history/voice-history.js
const app = getApp()
Page({
    // 存储请求结果
    data: {
      history_list: [], // 用户的所有语音搜索历史
    },

    /*获取用户答题历史*/
    getHistory:function(){
      let that = this;
      wx.showLoading({
        title: '正在获取历史',
        icon: 'loading'
      });
      if(app.globalData.isLogin){
        wx.request({
            //URL
            url: app.globalData.web_server_base_url + '/rubbish_search_video_history',
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
                if(!res.data.hasOwnProperty("openid")){
                  let resData = res.data;
                  console.log(resData);
                  that.setData({
                    history_list: res.data,
                  })
                }
                wx.hideLoading();
            }
          });
      }
      
    },
    
    // tomore:function(event){
    //     console.log(event.currentTarget.dataset.time)
    //     wx.navigateTo({
    //       url: 'more/more?exam_time='+event.currentTarget.dataset.time,
    //     })
    // },

    onLoad(){
        this.getHistory();
    },
    onShow() {
    }
})