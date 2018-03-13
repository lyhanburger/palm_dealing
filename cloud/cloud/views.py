from django.http import HttpResponse
from django.shortcuts import render
import os
from django.views.decorators.csrf import csrf_exempt
import cv2
import opencv.cutout.cutout as cutout
import opencv.roi.roi as roi
import opencv.feature.seven.feature_7 as feature_7
@csrf_exempt
def upload(request):
	print("hh")
	if request.method == "POST":
		obj = request.FILES.get("file")
		obj_path = os.path.join('static', obj.name)
		obj_path_prefix = obj_path.rstrip(".jpg").rstrip(".jpeg").rstrip(".png")
		f = open(obj_path, 'wb')
		for line in obj.chunks():
			f.write(line)
		f.close()
#		img = cv2.imread(obj_path)
#		img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#		cv2.imwrite(obj_path_prefix+"_out.jpeg", img)
		cutout.cutout(obj_path)
		print(obj_path)
		return HttpResponse("https://www.lihao7086.com/"+obj_path_prefix+"_contour.jpg")
