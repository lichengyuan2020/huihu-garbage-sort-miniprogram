/*
 * @Description: baidu_sound_api
 * @Version: 
 * @Author: Dengchao
 * @Date: 2021-02-13 22:51:32
 * @LastEditors: Dengchao
 * @LastEditTime: 2021-02-14 11:23:26
 */
const ACCESS_KEY = "AkrkqFSrp8PuGUSd59u0Ba57";
const ACCESS_SECRET = "7IVg2HHeBtxqzvnNSiHxT0u9IIf7dYXr";
export function getToken(){
  return new Promise((resolve,reject)=>{
    wx.request({
      url: `https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=${ACCESS_KEY}&client_secret=${ACCESS_SECRET}`,
      method: "POST",
      success: (res)=>{
        // console.log(res);
        wx.setStorage({
          data: res.data.refresh_token,
          key: "user-token",
        })
      }
    });
  });
}

export function soundReco(data){
    console.log("发送给服务器数据：",data)
  let token = wx.getStorageSync("user-token");
  if(!token){
    console.log("reget token");
    getToken();
  }
  return new Promise((resolve, regest)=>{
    wx.request({
      url: `https://vop.baidu.com/server_api?dev_pid=1537&cuid=123456789miniapp&token=${token}`,
      method: "POST",
      data: data,
      header: {"Content-Type": "audio/pcm;rate=16000"},
    //   header: {"Content-Type": "application/json"},
      success: (res)=>{
        console.log("请求后的结果",res)
        resolve(res.data.result[0]);
      },
      fail: regest
    })
  });
}
