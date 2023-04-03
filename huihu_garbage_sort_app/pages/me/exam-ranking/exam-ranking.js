let app=getApp()
Page({
  data: {
    userRankList: [],
    myrank:{}
  },
  onLoad() {
    this.getRankList()
  },
  getRankList(){
    let that = this;
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
          let resData = res.data.list;
          console.log(resData);
          that.rankListReform(resData);
          let mydata = res.data.me;
          mydata.avatar = app.globalData.web_server_base_url +  mydata.avatar;
          console.log(mydata);
          that.setData({
            userRankList: resData,
            myrank: mydata
          });
          
        }
      }
    })
  },
  rankListReform(list){
    list.forEach(function(value,index){
      value.avatar = app.globalData.web_server_base_url + value.avatar;
      console.log(value.avatar);
  });
  return list;
  }
  // getAnswerList() {
  //   wx.showLoading({
  //     title: '获取信息',
  //   })
  //   wx.cloud.callFunction({
  //     name: "db",
  //     data: {
  //       $url: 'getUserAnswerlist'
  //     }
  //   }).then(res => {
  //     wx.hideLoading()
  //     let result = res.result
  //     if (result.code) {
  //       this.setData({
  //         userAnswerList: result.data
  //       })
  //     }
  //   })
  // }
})