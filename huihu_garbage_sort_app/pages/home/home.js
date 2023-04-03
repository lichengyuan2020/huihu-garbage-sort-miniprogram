import {
  getToken,
  soundReco
} from "../../apis/baidu_ai"
const recorder = wx.getRecorderManager();
import { formatTime } from './../../utils/util.js';
let index = 0;
//获取应用实例
var app = getApp();

Page({
  data: {
    canRecordStart:false,
    j:0,
    isShow:false,
    audio_path: "",
    audio_data: undefined,
    recognize_result: "",
    timer: null,
    imgs: [],
    count: 3,
    re: [],
    results: [],
    visible3:false,
    rubbish_class:"",
    hidden:false,
    image_hidden:false,
    actions3:[
        {
            name: '返回',
            color: '#2d8cf0',
        },
        {
            name: '相关垃圾',
            color: '#19be6b'
        }
    ],
  },
  
  cancel:function(){
      this.setData({
          hidden:true,
          image_hidden:true,
      });

  },
  
  confirm:function(e){
        this.setData({
            hidden:true,
            image_hidden:true,

        });
        wx.navigateTo({
            url: '/pages/search/search?more_text=' + e.currentTarget.dataset.more_text
          });
        
  },


  onLoad: function (options) {
    this.applogin();
    console.log("onLoad！");
    this.setData({
      msgList: [{
          url: "url",
          title: "认清四色垃圾桶，垃圾分类要清楚"
        },
        {
          url: "url",
          title: "人人都出一份力，明天东大更美丽"
        },
        {
          url: "url",
          title: "垃圾分类就是好，蓝红黄绿干湿分"
        },
        {
          url: "url",
          title: "蓝色回收又能卖，红色有毒又有害"
        },
        {
          url: "url",
          title: "绿色剩菜瓜果皮，黄灰桶里放其他"
        }
      ]
    });
  },

  bindUpload: function (e) {
    switch (this.data.imgs.length) {
      case 0:
        this.data.count = 3
        break
      case 1:
        this.data.count = 2
        break
      case 2:
        this.data.count = 1
        break
    }
    var that = this
    wx.chooseImage({
      count: that.data.count, // 默认3
      sizeType: ["original", "compressed"], // 可以指定是原图还是压缩图，默认二者都有
      sourceType: ["album", "camera"], // 可以指定来源是相册还是相机，默认二者都有
      success: function (res) {
        // 返回选定照片的本地文件路径列表，tempFilePath可以作为img标签的src属性显示图片
        var tempFilePaths = res.tempFilePaths
        for (var i = 0; i < tempFilePaths.length; i++) {
          wx.uploadFile({
            url: app.globalData.web_server_base_url + '/rubbish_search_picture',
            filePath: tempFilePaths[i],
            name: "picture",
            header: {
              "content-type": "multipart/form-data",
              "openid":app.globalData.openid,
              "search_time":formatTime(new Date())
            },
            success: function (res) {
              if (res.statusCode == 200) {
                wx.showToast({
                  title: "上传成功",
                  icon: "none",
                  duration: 1500
                })
                that.data.imgs.push(JSON.parse(res.data).data)
                console.log(that.data.imgs);
                console.log(JSON.parse(res.data).rubbish_name);
                that.setData({
                  imgs: that.data.imgs,
                  result_img: [JSON.parse(res.data)],
                  image_hidden:false

                })


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
      }
    })
  },
  // 删除图片
  deleteImg: function (e) {
    var that = this
    wx.showModal({
      title: "提示",
      content: "是否删除",
      success: function (res) {
        if (res.confirm) {
          for (var i = 0; i < that.data.imgs.length; i++) {
            if (i == e.currentTarget.dataset.index) that.data.imgs.splice(i, 1)
          }
          that.setData({
            imgs: that.data.imgs,
          })
        } else if (res.cancel) {
          console.log("用户点击取消")
        }
      }
    })
  },

  soundRecognize() {
    //声明当天执行的
    soundReco(this.audio_data).then(res => {
      console.log("识别结果：", res);
      
    
      this.setData({
        recognize_result: res
      })
      var results = res;
      wx.setStorageSync('audio_results', results);
      //将声音识别结果发送给后端
      this.reqs();
    //   this.to_search_and_show();
    })
  },
  reqs() {
      var that = this;
      console.log("发送过去得数据：",that.data.recognize_result)
      wx.request({
        url: app.globalData.web_server_base_url+'/rubbish_search_video',
        data:{
            rubbish_name: that.data.recognize_result,
            openid:app.globalData.openid,
            search_time:formatTime(new Date())
          },
        header: {
            "content-type": "application/json",
        },
        method:'POST',
        success:function(res){
            console.log("服务器端返回结果：",res.data)
            that.setData({
                re: [res.data],
                visible3:true,
                rubbish_res:res.data,
                isShow:true,
                hidden:false
            })
        }
      })
  },
  to_search_and_show() {
    var that = this;
    //显示搜索中的提示
    wx.showLoading({
      title: '语音搜索中',
      icon: 'loading'
    })
    wx.request({
      url: app.globalData.web_server_base_url + '/rubbish_search_video',
      data: {
        rubbish_name: that.data.recognize_result,
        openid:app.globalData.openid,
        search_time:formatTime(new Date())
      },
      header: {
        'Content-Type': 'application/json'
      },
      method: "POST",
      success: function (res) {
        console.log(res.data)
        that.setData({
          re: [res.data],
        })
        wx.hideLoading();
      }
    })
  },
  start() {
    const options = {
      sampleRate: 16000,
      numberOfChannels: 1,
      format: "PCM"
    };
    //开始录音
    speaking.call(this);
    this.setData({
        canRecordStart: true
    });
    console.log("开始正式录音前，canRecordStart:"+this.data.canRecordStart);
    recorder.start(options);
    recorder.onStart(() => {
      console.log("Recording!~~~");
    });
    
    recorder.onError(err => {
      console.log(err);
    });
  },
  goSearch: function () {
    wx.navigateTo({
      url: '/pages/search/search'
    });
  },
  stop() {
    //结束录音
    clearInterval(this.timer);
    this.setData({
        canRecordStart: false
    });
    recorder.stop();
    recorder.onStop(res => {  
      console.log("录音结果", res);
      if(res && res.duration<1000){
          wx.showToast({
            title: '说话时间太短了',
            icon:'none'
          })
          return;
      }
      if(res && res.duration>8000){
          wx.showToast({
            title: '说得太长了,请简单一点',
            icon :'none'
          })
          return;
      }
      this.audio_path = res.tempFilePath; //获取录音文件的临时路径 (本地路径)
      const fs = wx.getFileSystemManager();
      fs.readFile({ //读取本地文件内容。单个文件大小上限为100M。
        filePath: this.audio_path, //要读取的文件的路径 (本地路径)
        success: (res) => {
          this.audio_data = res.data; //录音文件内容，类型ArrayBuffer 
          console.log("录音文件内容：", res.data)
          this.soundRecognize();
        }
      });
    });
  },

  hideModal:function(){
      this.setData({
          isShow:false
      })
  },

  applogin:function(){
    /*获取openid、头像、昵称*/
    let that=getApp();
    wx.login({
      success:(res)=>{
        console.log("用户code:"+res.code);
        wx.request({
          url: that.globalData.web_server_base_url+'/login',
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
  }
})

//麦克风帧动画
function speaking() {
    var _this = this;
    //话筒帧动画
    var i = 1;
    this.timer = setInterval(function () {
        i++;
        i = i % 5;
        _this.setData({
            j: i
        })
    }, 200);
}