//取值
function get(key, sync = true) {
  try {
    if (sync) {
      return wx.getStorageSync(key);
    } else {
      let data = '';
      wx.getStorage({
        key: key,
        success: function (res) {
          data = res.data;
        }
      });
      return data;
    }
  } catch (e) {
    return false;
  }
}

//赋值
function set(key, value, sync = true) {
  try {
    if (sync) {
      return wx.setStorageSync(key, value);
    } else {
      wx.setStorage({
        key: key,
        data: value
      });
    }
  } catch (e) {

  }
}

//移除
function del(key, sync = true) {
  try {
    if (sync) {
      return wx.removeStorageSync(key);
    } else {
      wx.removeStorage({
        key: key
      });
    }
  } catch (e) {
    return false;
  }
}

//清空
function clear(sync = true) {
  try {
    if (sync) {
      return wx.clearStorageSync();
    } else {
      wx.clearStorage();
    }
  } catch (e) {
    return false;
  }
}

export {
  get,
  set,
  del,
  clear
}