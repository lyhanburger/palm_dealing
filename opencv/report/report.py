# -*- coding: utf-8 -*-
import os
import sys
import os
from weasyprint import HTML
from opencv.report.getMdstr import mdstr_wangchengxia, mdstr_NN,mdstr_head,mdstr_image
def report(img_name, report_list):
    IMAGE_USER = img_name.replace(".jpg","").replace(".jpeg","").replace(".png","")
    #select
    mdstr = ""
    mdstr += mdstr_head()
    #mdstr += '''<img src={0}_showall.jpg alt="手掌图片">'''.format(IMAGE_USER)
    mdstr += "<body>"
    img_src = "http://localhost:8000/{0}_showall.jpg".format(IMAGE_USER)
    mdstr += mdstr_image(img_src)
    mdstr += mdstr_wangchengxia(report_list)
    mdstr += mdstr_NN(report_list)
    mdstr += "</body>"
    HTML(string=mdstr).write_pdf(IMAGE_USER+"_report.pdf",presentational_hints=True)

#    with open("{0}_report.md".format(IMAGE_USER),"w") as  file:
#        file.write(mdstr)

#    os.system("md2pdf --theme=github --output "+IMAGE_USER+"_report.pdf "+IMAGE_USER+"_report.md;sleep 3 ")
if __name__ == '__main__':
    pass
#    report_list = {"feature_7":True,"feature_9":True}
#    report("../image/yangxuanyue/yangxuanyue.jpg",report_list)

