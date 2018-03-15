# -*- coding: utf-8 -*-
import os
from PIL import Image, ImageFont, ImageDraw
def fill(str_in, width):
    i = 0
    str_out = ""
    for char in str_in:
        str_out+=char
        i = (i+1)%width
        if i==0:str_out+="\n"
    return str_out


        
db = {
        "feature_7":["7线[太阳线]", "主要反映血压的高低异常，临床大量病例统计显示，7线形成，但未切过1线， 多提示低血压， 若切过2线， 多提示高血压。还可反映血压异常，高血脂，心机缺血"],
        "feature_9":["9线[过敏线]","起于食指与中指指缝之间， 以弧形延伸到无名指与小指指缝间","有这条线的人多为过敏体质。如果长时间在电脑前工作，23天这个线就会出现， 当接触辐射频繁时， 就会发现这条线变深","在不孕不育夫妻双方手上均有这条线时，需要检查精液或卵子是否有抗体产生而引起不孕症","还可反映过敏，不孕症"],
		"feature_10":["10线［土星线", "在中指掌指褶纹下，为一弧形半月圆","此线和视力密切相关，是近视眼的特征性表现．如果土星线上有米字纹，　免疫线上有岛纹，　预示患有严重的眼病","有这条线的人一般性格孤僻，　情绪抑郁，易肝气不舒，容易患肝病，且心胸比较狭窄，容易嫉妒．","还可反映视力异常，肝脏疾病，性功能障碍,抑郁症，自闭症"]
        }



def report(img_name, report_list):
    IMAGE_USER = img_name.rstrip(".jpg").rstrip(".jpeg").rstrip(".png")
    #select
    report = []
    for key in report_list:
        if report_list[key] == True:
            report.append(db[key])
   #draw 
  
    size_x = 400 
    size_y = 800
    im = Image.new("RGB", (size_x, size_y), (255, 255, 255))
    dr = ImageDraw.Draw(im)
    font_size = 14
    print(os.path.join("fonts","msyh.ttf"))
    font = ImageFont.truetype(os.path.join("fonts", "msyh.ttf"), font_size)
    pos = 0
    fill_width = int(size_x/font_size) - 1
    for repo in report:
        for nu,line in enumerate(repo):
            tstr = fill(line, fill_width)
            if nu!=0:
                tstr = "    "+tstr
            dr.text((0,pos), tstr, font=font, fill="#444444")
            pos += (tstr.count("\n")+2)*font_size
    im.save("{0}_report.jpg".format(IMAGE_USER))
if __name__ == '__main__':
    report_list = {"feature_7":True,"feature_9":True}
    report("./t.png",report_list)
