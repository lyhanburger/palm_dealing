from django.http import HttpResponse
from django.shortcuts import render
import os
from django.views.decorators.csrf import csrf_exempt
import cv2
import opencv.cutout.cutout as cutout
import opencv.roi.roi as roi
import opencv.feature.seven.feature_7 as feature_7
import opencv.feature.nine.feature_9 as feature_9
import opencv.feature.ten.feature_10 as feature_10
import opencv.report.report as report
import opencv.report.showall as showall
import time
@csrf_exempt
def upload(request):
	if request.method == "POST":
		print("comes a post")
		obj = request.FILES.get("file")
		obj_path = os.path.join('static', obj.name)
		obj_path_prefix = obj_path.replace(".jpg","").replace(".jpeg","").replace(".png","")

		f = open(obj_path, 'wb')
		for line in obj.chunks():
			f.write(line)
		f.close()

		report_list = []
		cutout.cutout(obj_path)#提取手掌
		center_points = roi.roi(obj_path)#提取感兴趣区域,返回中心点

                # 提取特征
		report_list.extend(feature_7.feature_7(obj_path))#
		report_list.extend(feature_9.feature_9(obj_path))
		report_list.extend(feature_10.feature_10(obj_path))

		time.sleep(1)
		showall.showall(obj_path,center_points)#拼接图片,需要不同区域的中心点
		report.report(obj_path,report_list)#合成报告
		
		print(obj_path)
		return HttpResponse(
		"https://www.lihao7086.com/"+obj_path_prefix+"_report.pdf"
		)
