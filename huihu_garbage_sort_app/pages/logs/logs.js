// logs.js
const util = require('../../utils/util.js')

Page({
  data: {
    name: ''
  },
  onLoad(options) {
      console.log(options)
      this.setData({
          name: options.name
      })
    // this.setData({
    //   logs: (wx.getStorageSync('logs') || []).map(log => {
    //     return {
    //       date: util.formatTime(new Date(log)),
    //       timeStamp: log
    //     }
    //   })
    // })
  }
})
