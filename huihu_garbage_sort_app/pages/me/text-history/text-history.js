// pages/me/text-history/text-history.js
const app = getApp()
Page({
    // 存储请求结果
    data: {
      history_list: [], // 用户的当前答题历史

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
        url: app.globalData.web_server_base_url + '/rubbish_search_txt_history',
        data: {
            "code": "1",
            "openid":app.globalData.openid,
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
              // resData = that.history_reform(resData);
              that.setData({
                history_list: resData,
              });
              
            }
            wx.hideLoading();
        }
      });
    },
    
    // tomore:function(event){
    //     console.log(event.currentTarget.dataset.time)
    //     wx.setStorageSync('exam_time', exam_time)
    //     wx.navigateTo({
    //       url: 'more/more',
    //     })
    // },

    history_reform:function(h_list){

        // this.setData({
        //     history_list[0].c_id:2
        // })
        h_list.forEach(function(value,index){
            switch (value.c_id){
                case 1:
                  value.c_id = '可回收物';
                  break;
                case 2:
                  value.c_id = '有害垃圾';
                  break;
                case 3:
                  value.c_id = '厨余垃圾';
                  break;
                case 4:
                  value.c_id = '其他垃圾';
                  break;
              }
        });
        h_list.forEach(function(value,index){
            switch (value.u_id){
                case 1:
                  value.u_id = '可回收物';
                  break;
                case 2:
                  value.u_id = '有害垃圾';
                  break;
                case 3:
                  value.u_id = '厨余垃圾';
                  break;
                case 4:
                  value.u_id = '其他垃圾';
                  break;
              }
        });
        return h_list;
    },

    onLoad(lastpage){
        this.getHistory();
    },
    onShow() {
    }
})