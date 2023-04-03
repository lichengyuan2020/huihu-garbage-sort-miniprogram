const http = require("./../../utils/http.js");
const util = require("./../../utils/util.js");
import Poster from '../../components/canves/poster/poster';
import { formatTime } from './../../utils/util.js';
const app = getApp();

Page({
  data: {
    // questions:[],
    questions:[
      {
        name:'电池',
        id:1,
        show:false,
        category_grandpa_id:1,
        result:-1,
      },
      {
        name:'瓶子',
        id:2,
        show:false,
        category_grandpa_id:1,
        result:-1,
      },
      {
        name:'纸张',
        id:3,
        show:false,
        category_grandpa_id:1,
        result:-1,
      },
      {
        show:false,
        name:'手机',
        id:4,
        category_grandpa_id:1,
        result:-1,
      },
      {
        show:false,
        name:'电脑',
        id:5,
        category_grandpa_id:1,
        result:-1,
      },
      {
        name:'电池电池电池电池电池电池电池电池电池',
        id:6,
        show:true,
        category_grandpa_id:1,
        result:-1,
      },
      {
        name:'瓶子',
        id:7,
        show:false,
        category_grandpa_id:1,
        result:-1,
      },
      {
        name:'纸张',
        id:8,
        show:false,
        category_grandpa_id:1,
        result:-1,
      },
      {
        show:false,
        name:'手机',
        id:9,
        category_grandpa_id:1,
        result:-1,
      },
      {
        show:false,
        name:'电脑',
        id:10,
        category_grandpa_id:1,
        result:-1,
      },
    ],//题目
    showIndex:0,
    answerData:[],//答题结果
    answerData1:[],
    answerResult:'',
    showAnswerResult:false,
    currentSelect:'',
    theRightResult:'',
    showTest:false,
    showResult:false, 
    current_time:null,
    testCount:{
      total_count:0,
      right:0,
      error:0,
      score:0,
      rate:0
    },
    showRestar:false,
    isAnswer:true,
    show_auth:false,
    avatarUrl:'',
    avatar:'',
    bg:'',
    poster:''
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    // this.auth();
    this.getQuestions();
  },

  onReady:function(){
    this.downLoadBg();
  },

  onSwiperChange: function (e) {
    let current = e.detail.current;
    let images = this.data.questions;
    images.map((item, index) => {
      if ((index) == current) {
        item.show = true;
      } else {
        item.show = false;
      }
    })
    this.setData({ questions: images })
  },

  starTest:function(){
    wx.showLoading({
      title: '试题加载中...',
    })
    this.getQuestions();
  },

  //从数据库获取10道题目
  getQuestions: function () {
    var that = this;
    //显示搜索中的提示
    wx.showLoading({
      title: '正在获取题库',
      icon: 'loading'
    }),

    wx.request({
      //URL
      url: app.globalData.web_server_base_url + '/rubbish_test_new',
      data: {
        "code": "1"
      },
      header: {
        'Content-Type': 'application/json'
      },
      method: "POST",
      //请求成功
      success: function (res) {

        wx.hideLoading();
        let resData = res.data;
        console.log(resData);
        that.setData({
          questions: res.data,
          showTest: true,
          isAnswer: false
        })
      }

    });
    // wx.hideLoading();
    // this.setData({showTest: true, isAnswer:false})
  },

//   /**
//  * 监听用户点击授权按钮
//  */
//   getAuthUserInfo: function (data) {
//     this.setData({ avatarUrl: data.detail.userInfo.avatarUrl});
//     this.setData({
//       show_auth: false,
//     });
//     this.downLoadAvatar();
//   },

//   auth:function(){
//     let that = this;
//     wx.getSetting({
//       success(res) {
//         if (!res.authSetting['scope.userInfo']) {
//           that.setData({
//             show_auth: true
//           });
//         } else {
//           wx.getUserInfo({
//             success: res => {
//               that.setData({
//                  avatarUrl: res.userInfo.avatarUrl, 
//               })
//               that.downLoadAvatar();
//             }
//           })
//         }
//       }
//     })
//   },

  /**
   * 下一题
   */
  showNext:function(){

    let questions = this.data.questions;
    let showIndex = this.data.showIndex;
    if(showIndex == 9){
      wx.showToast({
        title: '没有下一题了',
        icon:'none'
      })
      return false;
    }

    if (!this.data.isAnswer){
      wx.showToast({
        title: '当前题目未作答',
        icon: 'none'
      })
      return false;
    }

    questions.map((item,index)=>{
      if (index == (showIndex + 1)){
        item.show = true;
      }else{
        item.show = false;
      }
      return item;
    });

    this.setData({
      questions: questions,
      showIndex: showIndex+1,
      showAnswerResult:false,
      currentSelect:'',
      isAnswer:false
    })
  },

/**
   * 上一题
   */
  // showLast:function(){

  //   let questions = this.data.questions;
  //   let showIndex = this.data.showIndex;
  //   if(showIndex == 0){
  //     wx.showToast({
  //       title: '没有上一题了',
  //       icon:'none'
  //     })
  //     return false;
  //   }

  //   // if (!this.data.isAnswer){
  //   //   wx.showToast({
  //   //     title: '当前题目未作答',
  //   //     icon: 'none'
  //   //   })
  //   //   return false;
  //   // }

  //   questions.map((item,index)=>{
  //     if (index == (showIndex - 1)){
  //       item.show = true;
  //     }else{
  //       item.show = false;
  //     }
  //     return item;
  //   });

  //   this.setData({
  //     questions: questions,
  //     showIndex: showIndex-1,
  //     showAnswerResult:false,
  //     currentSelect:'',
  //     isAnswer:true
  //   })
  // },

  /**
   * 用户答题
   */
  answer:function(e){
    let id = e.currentTarget.dataset.id;
    let qId = e.currentTarget.dataset.q_id;
    let currentQuestion = '';
    let answerResult = '';

    let hadAnswer = false;
    this.data.answerData.map(item=>{
      if (item.questions == qId){
        hadAnswer = true;
      }
      return item;
    })
    if(hadAnswer == true){
      return false;
    }

    this.data.questions.map(item=>{
      if(item.id == qId){
        currentQuestion = item;
      }
      return item;
    })
    //currentQuestion.result=id;
    let theRightResult = '';
    if (currentQuestion.category_grandpa_id == id){
      //答对了
      answerResult = true;
      //currentQuestion.result=1;
      console.log(currentQuestion);
    }else{
      //答错
      console.log(id);
      answerResult = false;
      switch (parseInt(currentQuestion.category_grandpa_id)){
        case 1:
          theRightResult = '可回收物';
          break;
        case 2:
          theRightResult = '有害垃圾';
          break;
        case 3:
          theRightResult = '厨余垃圾';
          break;
        case 4:
          theRightResult = '其他垃圾';
          break;
      }
      //currentQuestion.result=0;
      //console.log(currentQuestion);
    }

    let answerData = this.data.answerData;
    let answerData1 = this.data.answerData1;
    answerData.push({
      questions: currentQuestion.id,
      //name: currentQuestion.name,
      //c_id: currentQuestion.category_grandpa_id,
      user_answer: id,
      result: answerResult
    });
    answerData1.push({
        //question_id: currentQuestion.id,
        name: currentQuestion.name,
        c_id: currentQuestion.category_grandpa_id,
        u_id: id,
        //result: answerResult
      });
    // console.log(this.data.answerData);
    // console.log(new Date());

    this.setData({
      answerResult: answerResult,
      showAnswerResult: true,
      answerData: answerData,
      answerData1:answerData1,
      currentSelect:id,
      theRightResult: theRightResult,
      isAnswer:true
    })

    //判断是否已经答题结束
    setTimeout(res=>{
      if (answerData.length == this.data.questions.length){
        wx.showLoading({
          title: '正在生成报告',
        })
        //正在生成测试报告
        //计算答题结果
        let count = this.data.testCount;
        count.total_count = answerData.length;
        answerData.map(item=>{
          if (item.result == true){
            count.right += 1;
          }else{
            count.error += 1;
          }
          return item;
        })
        count.score = 10 * count.right;

        //保存数据
        // http.post(`/rubbish/examination`, {
        //   answer: answerData
        // }, res => {
        //   wx.hideLoading();
        //   let resData = res.data;
        //   if (resData.code != 0) {
        //     wx.showToast({
        //       title: '保存错误',
        //       icon: 'none'
        //     })
        //     return false;
        //   }

        //   count.rate = resData.data;

        //   this.setData({ testCount: count, showResult: true, showRestar: true })
        // });
        wx.hideLoading();
        this.setData({ testCount: count, showResult: true, showRestar: true, current_time: formatTime(new Date()) })
        this.send();
      }
    },1000)
  },

  /**
   * 关闭报告页面
   */
  closeResult: function () {
    this.setData({
      showResult: false
    });
  },

  saveTobutton:function(){
    //this.createPoster();
    //this.send();
  },

  doNotThing: function () {

  },

  /**
   * 重新测试
   */
  restar:function(){
    this.setData({
      //questions: [],
      questions:[
        {
          name:'电池',
          id:1,
          show:false,
          category_grandpa_id:1,
          result:-1,
        },
        {
          name:'瓶子',
          id:2,
          show:false,
          category_grandpa_id:1,
          result:-1,
        },
        {
          name:'纸张',
          id:3,
          show:false,
          category_grandpa_id:1,
          result:-1,
        },
        {
          show:false,
          name:'手机',
          id:4,
          category_grandpa_id:1,
          result:-1,
        },
        {
          show:false,
          name:'电脑',
          id:5,
          category_grandpa_id:1,
          result:-1,
        },
        {
          name:'电池电池电池电池电池电池电池电池电池',
          id:6,
          show:true,
          category_grandpa_id:1,
          result:-1,
        },
        {
          name:'瓶子',
          id:7,
          show:false,
          category_grandpa_id:1,
          result:-1,
        },
        {
          name:'纸张',
          id:8,
          show:false,
          category_grandpa_id:1,
          result:-1,
        },
        {
          show:false,
          name:'手机',
          id:9,
          category_grandpa_id:1,
          result:-1,
        },
        {
          show:false,
          name:'电脑',
          id:10,
          category_grandpa_id:1,
          result:-1,
        },
      ],
      showIndex: 0,
      answerData: [],
      answerResult: '',
      showAnswerResult: false,
      currentSelect: '',
      theRightResult: '',
      showTest: false,
      showResult: false,
      testCount: {
        total_count: 0,
        right: 0,
        error: 0,
        score: 0,
        rate: 0
      },
      showRestar: false,
      isAnswer:true
    });

    wx.showLoading({
      title: '试题加载中...',
    });
    this.getQuestions();
  },
  
  /**
  * 分享
  */
  onShareAppMessage: function (res) {
    return {
      title: '垃圾分类，守护地球',
      path: '/pages/home/index/index',
      imageUrl: '/images/share.jpg',
      success: function (res) {
        // 转发成功
      },
      fail: function (res) {
        // 转发失败
      }
    }
  },

  createPoster:function(){
    console.log(this.data.avatarUrl)
    let testCount = this.data.testCount;
    let posterConfig = {
      defaultConfig: {
        width: 375,
        height: 667,
        debug: false,
        images: [
          {
            width: 375,
            height: 667,
            x: 0,
            y: 0,
            url: this.data.bg,
          },
          // {
          //   width: 60,
          //   height: 20,
          //   x: 270,
          //   y: 170,
          //   url: '/images/score-bg.png',
          //   zIndex: 99
          // },
          // {
          //   width: 80,
          //   height: 80,
          //   x: 160,
          //   y: 140,
          //   url: '/images/qr-code.jpg',
          //   zIndex: 100
          // },
          {
            width: 50,
            height: 50,
            borderRadius: 10,
            x: 35,
            y: 40,
            url: this.data.avatar,
          }
        ],
        texts: [
          {
            x: 100,
            y: 70,
            text: '垃圾分类答题报告',
            fontSize: 22,
            color: '#EE2C2C',
            zIndex: 100
          },
          {
            x: 50,
            y: 160,
            text: `共` + testCount.total_count+'题',
            fontSize: 18,
            color: 'gray',
            zIndex: 100
          },
          {
            x: 50,
            y: 190,
            text: `答错：` + testCount.error,
            fontSize: 18,
            color: 'gray',
            zIndex: 100
          },
          {
            x: 50,
            y: 220,
            text: `答对：` + testCount.right,
            fontSize: 18,
            color: 'gray',
            zIndex: 100
          },
          {
            x: 50,
            y: 250,
            text: `答题得分：` + testCount.score,
            fontSize: 18,
            color: 'gray',
            zIndex: 100
          },
          // {
          //   x: 50,
          //   y: 300,
          //   text: `垃圾分类熟练度超过,全国${testCount.rate}%的用户`,
          //   fontSize: 18,
          //   color: '#EE2C2C',
          //   zIndex: 100
          // },
          {
            x: 290,
            y: 170,
            text: testCount.score,
            fontSize: 22,
            color: '#EE2C2C',
            zIndex: 100
          },

        ],
        blocks: [
          {
            width: 310,
            height: 667 / 2.7,
            x: 32,
            y: 120,
            backgroundColor: 'white',
            borderRadius: 20,
            zIndex: 90
          }
        ]
      }
    }

    this.setData({ posterConfig: posterConfig.defaultConfig }, () => {
      Poster.create(true);    // 入参：true为抹掉重新生成 
    });
  },

  downLoadAvatar: function () {
    let avatar = this.data.avatarUrl;
    console.log("头像")
    console.log(avatar)
    wx.downloadFile({
      url: avatar,
      success: res => {
        console.log('头像下载');
        console.log(res)
        this.setData({
          avatar: res.tempFilePath
        })
      }
    })
  },

  onPosterSuccess(e) {
    const { detail } = e;
    let that = this;
    wx.saveImageToPhotosAlbum({
      filePath: detail,
      success(res) {
        console.log(res);
      }
    })
  },
  onPosterFail(err) {
    console.log("出错了");
    console.error(err);
  },

  //背景图片，从网页下载
  downLoadBg: function () {
    let bg = 'https://image.qiuhuiyi.cn/tmp/wx18ac06afc8eaed33.o6zAJs3oh85Zb1lJE8oWix57vny0.XCu0lmzRHYP53b7dcd6e5aaaae15a74c1fbd0916708b.jpg';
    wx.downloadFile({
      url: bg,
      success: res => {
        if (true/*res.statusCode === 200*/) {
          this.setData({
            bg: res.tempFilePath
          })
        }
      }
    })
  },

  /*向服务器发送答题结果*/
  send:function(){
    var that = this;
    //显示搜索中的提示
    //that.data.result.setData({openid:app.globalData.openid})
    console.log(app.globalData.openid)
    wx.request({
      //URL
      url: app.globalData.web_server_base_url + '/rubbish_test_result',
      data: {
        result:{
            openid:app.globalData.openid,
            exam_time:this.data.current_time,
            score:this.data.testCount.score,
            questions:this.data.answerData1
        }
        // result:{
        //   openid:app.globalData.openid,
        //   exam_time:"2023-03-21 11:19:17",
        //   score:90,
        //   questions:[{name:'电池',c_id:1,u_id:1},{name:'瓶子',c_id:1,u_id:1},{name:'纸张',c_id:1,u_id:1},
        //             {name:'手机',c_id:1,u_id:1},{name:'电脑',c_id:1,u_id:1},
        //             {name:'电池',c_id:1,u_id:1},{name:'瓶子',c_id:1,u_id:1},{name:'纸张',c_id:1,u_id:1},
        //             {name:'手机',c_id:1,u_id:1},{name:'电脑',c_id:1,u_id:1},],
        // }
      },
      header: {
        'Content-Type': 'application/json'
      },
      method: "POST",
      //请求成功
      success: function (res) {

        let resData = res.data;
        console.log(resData);
        app.globalData.examCount += 1;
        app.globalData.examPoints += that.data.testCount.score;
        console.log('changed',app.globalData.examCount,app.globalData.examPoints)
        that.setData({
          
        })
      }

    });
  },

  /*获取当前时间*/
  getNowDate: function () {
 
 
    var date = new Date();
    var year = date.getFullYear() //年
    var month = date.getMonth() + 1//月
    var day = date.getDate()//日

    var hour = date.getHours()//时
    var minute = date.getMinutes()//分
    var second = date.getSeconds()//秒

    var xiaoshi = "";
    if (hour < 10) {
        xiaoshi = "0" + hour;
    } else {
        xiaoshi = hour + "";
    }

    var fenzhong = "";
    if (minute < 10) {
        fenzhong = "0" + minute;
    } else {
        fenzhong = minute + "";
    }

    var miao = "";
    if (second < 10) {
        miao = "0" + second;
    } else {
        miao = second + "";
    }
    console.log(year + '-' + month + '-' + day + ' ' + xiaoshi + ':' + fenzhong + ':' + miao);
    this.setData({
        current_time: year + '-' + month + '-' + day + ' ' + xiaoshi + ':' + fenzhong + ':' + miao
    })

},


})