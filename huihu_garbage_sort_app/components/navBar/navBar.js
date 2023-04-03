// components/navBar/navBar.js
Component({
    /**
     * 组件的属性列表
     */
    properties: {
  
    },
  
    /**
     * 组件的初始数据
     */
    data: {
      navBarStyles: '',
    },
    lifetimes: {
      // 生命周期函数，可以为函数，或一个在methods段中定义的方法名
      attached: function () {
        this.setStyle();
      },
      
    },
    /**
     * 组件的方法列表
     */
    methods: {
      setStyle: function() {
        const {
          screenWidth,
        } = wx.getSystemInfoSync();
        const {
          top, width, right, bottom
        } = wx.getMenuButtonBoundingClientRect();
        console.log(wx.getSystemInfoSync())
        console.log(wx.getMenuButtonBoundingClientRect())
        const padding = screenWidth - right; 
        this.setData({
          navBarStyles: [
            `padding-top: ${top}px`,
            `padding-left: ${padding}px`,
            `padding-right: ${padding + width}px`,
            `padding-bottom: ${padding}px`,
            `height: ${bottom + padding}px`,
          ].join(';'),
        });
      }
    }
  })
  