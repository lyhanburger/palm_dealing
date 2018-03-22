//index.js  
//获取应用实例  
var app = getApp()
App({
  onLaunch: function() {
    wx.login({
		success:function(res){
			console.log("ok")	
			wx.getSetting({
			    success(res) {
			        if (!res.authSetting['scope.record']) {
			            wx.authorize({
			                scope: 'scope.record',
			                success() {
			                    // 用户已经同意小程序使用录音功能，后续调用 wx.startRecord 接口不会弹窗询问
			                    wx.startRecord()
			                }
			            })
			        }
			    }
			})
			wx.getUserInfo({
			  success: function(res) {
			    var userInfo = res.userInfo
			    var nickName = userInfo.nickName
			    var avatarUrl = userInfo.avatarUrl
			    var gender = userInfo.gender //性别 0：未知、1：男、2：女
			    var province = userInfo.province
			    var city = userInfo.city
			    var country = userInfo.country
				console.log(userInfo)
			  }
			})
		}	
	});
  }
})
Page({
  data: {
    tempFilePaths: '',
	
  },
onLoad: function(){},
upLoad: function () {
	var _this = this
	wx.chooseImage({
			count:1,
			sizeType:['original'],
	  success: function(res) {
	    var tempFilePaths = res.tempFilePaths
		_this.setData({content:"正在上传,大约需要30s,请不要操作其他"})
	    wx.uploadFile({
	      url: 'https://www.lihao7086.com/upload', //仅为示例，非真实的接口地址
	      filePath: tempFilePaths[0],
	      name: 'file',
	      formData:{
	        'user': 'test'
	      },
//--------------upload success
	      success: function(res){
	        var data = res.data//get url
//			-------download pdf by url
					wx.downloadFile({
					  url: data,
					  success: function (res) {
					    var filePath = res.tempFilePath
						_this.setData({content:""})
					    wx.openDocument({
					      filePath: filePath,
					      success: function (res) {
					        console.log('打开文档成功')
					      }
					    })
					  }
					})
			
	      }
	    })
	  }
	})
  },
upLoadDemo_fast:function(){
	var _this = this
	var tempcontent = "正在上传示例图片,大约需要30s,请不要操作其他"
	this.setData({content:tempcontent})
	wx.downloadFile({url:'https://www.lihao7086.com/static/demo/yangxuanyue_report.pdf',
		success:function(res){
			var filePath = res.tempFilePath
			_this.setData({content:""})
			wx.openDocument({filePath:filePath,success:function(res){console.log('open success')}})
		}})	
},
upLoadDemo: function(){
	wx.downloadFile({url:'https://www.lihao7086.com/static/demo/yangxuanyue.jpg',
		success:function(res){
			var imgpath = res.tempFilePath
			wx.uploadFile({url:'https://www.lihao7086.com/upload',filePath:imgpath,name:'file',formData:{'user':'test'},
				success:function(res){
					var data = res.data
					wx.downloadFile({url:data,
						success:function(res){
							var filePath = res.tempFilePath
									wx.openDocument({filePath:filePath,success:function(res){console.log('打开文档成功')}})
							}})
				}})
		}})
}
})  
