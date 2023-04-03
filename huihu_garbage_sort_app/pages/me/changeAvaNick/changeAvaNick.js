// pages/me/changeAvaNick/changeAvaNick.js
let app = getApp();
var avatarUrl = app.globalData.avatarUrl;
console.log(avatarUrl)
Page({
    data: {
        avatarUrl : '',//app.globalData.avatarUrl,
        Nickname : "",//app.globalData.Nickname,
        avatar_is_shown : false
    },
    onChooseAvatar(e) {
        const { avatarUrl } = e.detail
        console.log(avatarUrl) 
        var value2 = wx.getStorageSync(avatarUrl)
        console.log(value2)
        this.setData({
          avatarUrl: avatarUrl,
          avatar_is_shown:true
        })
        console.log(this.data.avatarUrl)
    },
    onSetNickname(e){
        console.log(e.detail.value) 
        if(e.detail.value!=null){
          console.log('changed')
          this.setData({
            Nickname: e.detail.value
          })
        }
    },
    formSubmit: function (e) {
        var that = this;
        var formData = e.detail.value.keyword;
        // wx.request({
        //  url: app.globalData.web_server_base_url + '/user_change',
        //  data: {
        //      avatarUrl:that.data.avatarUrl
        // },
        //  header: {
        //   'Content-Type':'application/json',
        //   "openid":app.globalData.openid,
        //   "name":that.data.Nickname
        //  },
        //  method:"POST",
        //  success: function (res) {
        //   console.log(res.data)
        // //   that.setData({
        // //       re:res.data,
        // //   })
        //  }
        // })
        var value2 = wx.getStorageSync(that.data.avatarUrl)
        if(that.data.avatar_is_shown){
           wx.uploadFile({
            url: app.globalData.web_server_base_url + '/user_change',
            scriptCharset:'utf-8',
            filePath: that.data.avatarUrl,
            name: "avatar",
            header: {
              "content-type": "multipart/form-data",
              "openid":app.globalData.openid,
              "name":that.data.Nickname
            },
            success: function (res) {
              if (res.statusCode == 200) {
                wx.showToast({
                  title: "上传成功",
                  icon: "none",
                  duration: 1500,
                  success:function(){
                    setTimeout(function () {
                        app.globalData.Nickname = that.data.Nickname;
                        app.globalData.avatarUrl = that.data.avatarUrl;
                        console.log('changed',app.globalData.Nickname)
                        wx.navigateBack();
                      }, 1000) 
                    
                  }
                })
                // that.data.imgs.push(JSON.parse(res.data).data)
                // console.log(that.data.imgs);
                // console.log(JSON.parse(res.data).rubbish_name);
                // that.setData({
                //   imgs: that.data.imgs,
                //   result_img: [JSON.parse(res.data)],
                //   image_hidden:false

                // })
                // app.globalData.Nickname = that.data.Nickname;
                // app.globalData.avatarUrl = that.data.avatarUrl;
                // console.log('changed',app.globalData.Nickname)
                // wx.navigateBack();

              }
            },
            fail: function (err) {
              wx.showToast({
                title: "上传失败",
                icon: "none",
                duration: 2000
              })
            },
            complete: function (result) {
              console.log(result.errMsg)
            }
          })
        }
        else{
          wx.uploadFile({
            url: app.globalData.web_server_base_url + '/user_change',
            scriptCharset:'utf-8',
            filePath: that.data.avatarUrl,
            name: "avatar",
            header: {
              "content-type": "multipart/form-data",
              "openid":app.globalData.openid,
              "name":that.data.Nickname
            },
            success: function (res) {
              if (res.statusCode == 200) {
                wx.showToast({
                  title: "上传成功",
                  icon: "none",
                  duration: 1500,
                  success:function(){
                    setTimeout(function () {
                        app.globalData.Nickname = that.data.Nickname;
                        app.globalData.avatarUrl = that.data.avatarUrl;
                        console.log('changed',app.globalData.Nickname)
                        wx.navigateBack();
                      }, 1000) 
                    
                  }
                })
                // that.data.imgs.push(JSON.parse(res.data).data)
                // console.log(that.data.imgs);
                // console.log(JSON.parse(res.data).rubbish_name);
                // that.setData({
                //   imgs: that.data.imgs,
                //   result_img: [JSON.parse(res.data)],
                //   image_hidden:false

                // })
                // app.globalData.Nickname = that.data.Nickname;
                // app.globalData.avatarUrl = that.data.avatarUrl;
                // console.log('changed',app.globalData.Nickname)
                // wx.navigateBack();

              }
            },
            fail: function (err) {
              wx.showToast({
                title: "上传失败，头像为必填项",
                icon: "none",
                duration: 2000
              })
            },
            complete: function (result) {
              console.log(result.errMsg)
            }
          })
        }
       
    },
    onLoad() {
      this.setData({
        avatarUrl:app.globalData.avatarUrl,
        Nickname:app.globalData.Nickname
      })
    },
    onReady() {

    },
    onShow() {

    },
    onHide() {

    },

    /**
     * 生命周期函数--监听页面卸载
     */
    onUnload() {

    },

    /**
     * 页面相关事件处理函数--监听用户下拉动作
     */
    onPullDownRefresh() {

    },

    /**
     * 页面上拉触底事件的处理函数
     */
    onReachBottom() {

    },

    /**
     * 用户点击右上角分享
     */
    onShareAppMessage() {

    }
})