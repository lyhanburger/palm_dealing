//index.js  
//获取应用实例  
var app = getApp()
Page({
  data: {
    tempFilePaths: '',
    content:"https://www.lihao7086.com/download",
	
  },
onLoad: function(){},
upLoad: function () {
	wx.chooseImage({
			count:1,
			sizeType:['original'],
	  success: function(res) {
	    var tempFilePaths = res.tempFilePaths
	    wx.uploadFile({
	      url: 'https://www.lihao7086.com/upload', //仅为示例，非真实的接口地址
	      filePath: tempFilePaths[0],
	      name: 'file',
	      formData:{
	        'user': 'test'
	      },
	      success: function(res){
	        var data = res.data
			var murls = data.split(",")
			console.log(res.data)
			console.log("murls is "+murls)
			console.log("murls[0] is "+murls[0])
			wx.previewImage({
			  current: murls[0], // 当前显示图片的http链接
			  urls:[murls[0],murls[1]] // 需要预览的图片http链接列表
			})
			
	      }
	    })
	  }
	})
  },
	downLoad: function(){
			wx.downloadFile({
					url: 'https://www.lihao7086.com/download', //仅为示例，并非真实的资源
	  				success: function(res) {
					    if (res.statusCode === 200) {
							wx.previewImage({
							  current: res.tempFilePath, // 当前显示图片的http链接
							  urls: [res.tempFilePath] // 需要预览的图片http链接列表
							})
	   					 }
	  				}
			})
	},

  chooseimage: function () {
    var _this = this;
    wx.chooseImage({
      count: 1, // 默认9  
      sizeType: ['original', 'compressed'], // 可以指定是原图还是压缩图，默认二者都有  
      sourceType: ['album', 'camera'], // 可以指定来源是相册还是相机，默认二者都有  
      success: function (res) {
        // 返回选定照片的本地文件路径列表，tempFilePath可以作为img标签的src属性显示图片  
        _this.setData({
          tempFilePaths: res.tempFilePaths,
          content:"success"
        })
      },
      fail:function(res){
        content:"fails"
      }
    })
  }
})  
