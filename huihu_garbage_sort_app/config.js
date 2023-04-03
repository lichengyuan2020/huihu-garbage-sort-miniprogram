const config={
  dev:{//开发环境
    domain:"http://10.6.12.101/api/wechat",
    qiniuDomain:"https://image.qiuhuiyi.cn",
  },
  prod:{//生产环境
    domain: "http://heping.qiuhuiyi.cn/api/wechat",
    qiniuDomain: "https://image.qiuhuiyi.cn"
  }
}

//const domain = config.prod.domain;
const domain = config.dev.domain;

const qiniuDomain = config.prod.qiniuDomain;

module.exports = {
  domain, qiniuDomain
}