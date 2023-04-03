var md5 = require('md5.js')
const formatTime = date => {
  const year = date.getFullYear()
  const month = date.getMonth() + 1
  const day = date.getDate()
  const hour = date.getHours()
  const minute = date.getMinutes()
  const second = date.getSeconds()

  return [year, month, day].map(formatNumber).join('/') + ' ' + [hour, minute, second].map(formatNumber).join(':')
}

const formatNumber = n => {
  n = n.toString()
  return n[1] ? n : '0' + n
}
/** 生成随机字符串*/
function generateRandomString(n){
  var chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];
  var res = "";
  for (var i = 0; i < n; i++) {
    var id = Math.ceil(Math.random() * 35);
    res += chars[id];
  }
  return res;
}
/** 腾讯AI 签名*/ 
function signTengxunAI(map,key){
  var mapKeys = map.keys;
  var keysArr = []
  for (let key of map.keys()) {
    keysArr.push(key);
  }
  console.log("sort", keysArr.sort())
  var param = '';
  for (var i = 0; i < keysArr.length; i++) {
    param = param + keysArr[i] + "=" + map.get(keysArr[i]) + "&"
  }
  param = param + "app_key="+key
  var md5Param = md5.hexMD5(param).toUpperCase()
  // console.log("param============", param)
  console.log("md5Param=========", md5Param)
  return md5Param
}


function Base64() {

  // private property  
  var _keyStr = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=";

  // public method for encoding  
  this.encode = function (input) {
    var output = "";
    var chr1, chr2, chr3, enc1, enc2, enc3, enc4;
    var i = 0;
    input = _utf8_encode(input);
    while (i < input.length) {
      chr1 = input.charCodeAt(i++);
      chr2 = input.charCodeAt(i++);
      chr3 = input.charCodeAt(i++);
      enc1 = chr1 >> 2;
      enc2 = ((chr1 & 3) << 4) | (chr2 >> 4);
      enc3 = ((chr2 & 15) << 2) | (chr3 >> 6);
      enc4 = chr3 & 63;
      if (isNaN(chr2)) {
        enc3 = enc4 = 64;
      } else if (isNaN(chr3)) {
        enc4 = 64;
      }
      output = output +
        _keyStr.charAt(enc1) + _keyStr.charAt(enc2) +
        _keyStr.charAt(enc3) + _keyStr.charAt(enc4);
    }
    return output;
  }

  // public method for decoding  
  this.decode = function (input) {
    var output = "";
    var chr1, chr2, chr3;
    var enc1, enc2, enc3, enc4;
    var i = 0;
    input = input.replace(/[^A-Za-z0-9\+\/\=]/g, "");
    while (i < input.length) {
      enc1 = _keyStr.indexOf(input.charAt(i++));
      enc2 = _keyStr.indexOf(input.charAt(i++));
      enc3 = _keyStr.indexOf(input.charAt(i++));
      enc4 = _keyStr.indexOf(input.charAt(i++));
      chr1 = (enc1 << 2) | (enc2 >> 4);
      chr2 = ((enc2 & 15) << 4) | (enc3 >> 2);
      chr3 = ((enc3 & 3) << 6) | enc4;
      output = output + String.fromCharCode(chr1);
      if (enc3 != 64) {
        output = output + String.fromCharCode(chr2);
      }
      if (enc4 != 64) {
        output = output + String.fromCharCode(chr3);
      }
    }
    output = _utf8_decode(output);
    return output;
  }

  // private method for UTF-8 encoding  
  _utf8_encode = function (string) {
    string = string.replace(/\r\n/g, "\n");
    var utftext = "";
    for (var n = 0; n < string.length; n++) {
      var c = string.charCodeAt(n);
      if (c < 128) {
        utftext += String.fromCharCode(c);
      } else if ((c > 127) && (c < 2048)) {
        utftext += String.fromCharCode((c >> 6) | 192);
        utftext += String.fromCharCode((c & 63) | 128);
      } else {
        utftext += String.fromCharCode((c >> 12) | 224);
        utftext += String.fromCharCode(((c >> 6) & 63) | 128);
        utftext += String.fromCharCode((c & 63) | 128);
      }

    }
    return utftext;
  }

  // private method for UTF-8 decoding  
  _utf8_decode = function (utftext) {
    var string = "";
    var i = 0;
    var c = c1 = c2 = 0;
    while (i < utftext.length) {
      c = utftext.charCodeAt(i);
      if (c < 128) {
        string += String.fromCharCode(c);
        i++;
      } else if ((c > 191) && (c < 224)) {
        c2 = utftext.charCodeAt(i + 1);
        string += String.fromCharCode(((c & 31) << 6) | (c2 & 63));
        i += 2;
      } else {
        c2 = utftext.charCodeAt(i + 1);
        c3 = utftext.charCodeAt(i + 2);
        string += String.fromCharCode(((c & 15) << 12) | ((c2 & 63) << 6) | (c3 & 63));
        i += 3;
      }
    }
    return string;
  }
}

//操作失败的提示信息
function errorToShow(msg = '操作失败', callback = function () {}) {
  wx.showToast({
    title: msg,
    icon: 'none',
    duration: 1500
  })
  setTimeout(function () {
    callback()
  }, 1500)
}
//操作成功后，的提示信息
function successToShow(msg = '保存成功', callback = function () {}) {
  wx.showToast({
    title: msg,
    icon: 'success',
    duration: 1000
  })
  setTimeout(function () {
    callback()
  }, 500)
}

//处理性别
function isgender(gender) {
  if (gender == 0) {
    return "男"
  } else if (gender == 1) {
    return "女"
  } else {
    return "未知"
  }
}

function throttle(fn, gapTime) {
  if (gapTime == null || gapTime == undefined) {
    gapTime = 1500
  }

  let _lastTime = null

  // 返回新的函数
  return function () {
    let _nowTime = +new Date()
    if (_nowTime - _lastTime > gapTime || !_lastTime) {
      fn.apply(this, arguments) //将this和参数传给原函数
      _lastTime = _nowTime
    }
  }
}


/**
 * 授权请求
 * @export
 * @param {*} authorizeScope 更多scope参考
 * @param {*} modal modal弹窗参数信息
 */

function setScope(authorizeScope, modal) {
  return new Promise((resolve, reject) => {
    if (!modal) {
      modal = {
        title: '授权',
        content: '需要您设置授权已使用相应功能',
        confirmText: '设置'
      }
    }
    wx.getSetting({
      success(res) {
        // hasAuthor === undefined  表示 初始化进入，从未授权
        // hasAuthor === true       表示 已授权
        // hasAuthor === false      表示 授权拒绝
        const hasAuthor = res.authSetting[authorizeScope]
        switch (hasAuthor) {
          case undefined:
            wx.authorize({
              scope: authorizeScope,
              success: res => {
                resolve(res)
              },
              fail: err => {
                wx.showToast({
                  title: '授权失败',
                  icon: 'none',
                  duration: 3000
                })
                reject(err)
              }
            })
            break
          case true:
            resolve()
            break
          case false:
            //bug 在电脑模拟器会报错，手机不会
            wx.showModal({
              ...modal,
              success: res => {
                if (res.confirm) {
                  wx.openSetting({
                    success: res => {
                      if (res.authSetting[authorizeScope]) {
                        resolve(res)
                      } else {
                        reject(res)
                        wx.showToast({
                          title: '授权失败',
                          icon: 'none',
                          duration: 3000
                        })
                      }
                    },
                    fail: err => {
                      console.log(err)
                      reject(err)
                      wx.showToast({
                        title: '打开设置异常',
                        icon: 'none',
                        duration: 3000
                      })
                    }
                  })
                } else {
                  reject(res)
                  wx.showToast({
                    title: '授权失败',
                    icon: 'none',
                    duration: 3000
                  })
                }
              },
              fail: err => {
                reject(err)
                wx.showToast({
                  title: '弹窗异常',
                  icon: 'none',
                  duration: 3000
                })
              }
            })
            break
        }
      },
      fail: err => {
        reject(err)
        wx.showToast({
          title: '获取当前设置异常',
          icon: 'none',
          duration: 3000
        })
      }
    })
  })
}

//限制字数，超出部分以省略号...显示
function LimitNumber(txt, len = 10) {
  var str = txt;
  str = str.substr(0, len) + '...';
  return str
}

/**
 * 统一跳转
 */
function navigateTo(url, callback) {
  wx.navigateTo({
    url: url,
    animationType: 'pop-in',
    animationDuration: 300,
    success: callback
  })
}
/**
 * 关闭当前页面统一跳转
 */
function redirectTo(url, callback) {
  wx.redirectTo({
    url: url,
    animationType: 'pop-in',
    animationDuration: 300,
    success: callback
  })
}
/**
 * 关闭所有的页面打开一个页面
 */
function reLaunch(url, callback) {
  wx.reLaunch({
    url: url,
    animationType: 'pop-in',
    animationDuration: 300,
    success: callback
  })
}
/**
 * tabber跳转
 */
function switchTabTo(url, callback) {
  wx.switchTab({
    url: url,
    animationType: 'pop-in',
    animationDuration: 300,
    success: callback
  })
}
/**
 * 跳转的上一级页面
 */
function navigateBack(delta = 1, callback) {
  wx.navigateBack({
    delta,
    animationType: 'pop-in',
    animationDuration: 300,
    success: callback
  })
}

module.exports = {
  formatTime: formatTime,
  generateRandomString: generateRandomString,
  signTengxunAI: signTengxunAI,
  Base64: Base64,
  //
  errorToShow,
  successToShow,
  throttle,
  setScope,
  isgender,
  LimitNumber,
  navigateTo,
  redirectTo,
  reLaunch,
  switchTabTo,
  navigateBack
}
