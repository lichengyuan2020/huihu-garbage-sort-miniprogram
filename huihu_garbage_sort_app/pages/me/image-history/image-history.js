// pages/me/image-history/image-history.js
const app = getApp()
Page({
    // 存储请求结果
    data: {
      history_list: [], // 用户的所有答题历史
    },

    /*获取用户答题历史*/
    getHistory:function(){
      let that = this;
      wx.showLoading({
        title: '正在获取历史',
        icon: 'loading'
      }),
      wx.request({
        //URL
        url: app.globalData.web_server_base_url + '/rubbish_search_picture_history',
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
              resData = that.history_reform(resData);
              that.setData({
                history_list: resData,
              });
            }
            
            
        }
      });
      wx.hideLoading();
    },
    
    // tomore:function(event){
    //     console.log(event.currentTarget.dataset.time)
    //     wx.navigateTo({
    //       url: 'more/more?exam_time='+event.currentTarget.dataset.time,
    //     })
    // },

    history_reform:function(h_list){
        h_list.forEach(function(value,index){
            value.input = app.globalData.web_server_base_url + value.input;
            console.log(value.input);
        });
        return h_list;
    },

    onLoad(){
        this.getHistory();
    },
    onShow() {
    }
})