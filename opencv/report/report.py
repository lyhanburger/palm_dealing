# -*- coding: utf-8 -*-
import os
import markdown
import sys
import os
        
db = {
        "feature_7":["7线[太阳线]","特诊描述","主要反映血压的高低异常，临床大量病例统计显示，7线形成，但未切过1线， 多提示低血压， 若切过2线， 多提示高血压。还可反映血压异常，高血脂，心机缺血"],
        "feature_9":["9线[过敏线]","起于食指与中指指缝之间， 以弧形延伸到无名指与小指指缝间",
            "有这条线的人多为过敏体质。如果长时间在电脑前工作，23天这个线就会出现， 当接触辐射频繁时， 就会发现这条线变深.\n在不孕不育夫妻双方手上均有这条线时，需要检查精液或卵子是否有抗体产生而引起不孕症\n还可反映过敏，不孕症"],
		"feature_10":["10线［土星线]", "在中指掌指褶纹下，为一弧形半月圆","此线和视力密切相关，是近视眼的特征性表现．如果土星线上有米字纹，　免疫线上有岛纹，　预示患有严重的眼病","有这条线的人一般性格孤僻，　情绪抑郁，易肝气不舒，容易患肝病，且心胸比较狭窄，容易嫉妒．\n还可反映视力异常，肝脏疾病，性功能障碍,抑郁症，自闭症"]
        }



def report(img_name, report_list):
    IMAGE_USER = img_name.replace(".jpg","").replace(".jpeg","").replace(".png","")
    #select
    report = []
    for key in report_list:
        if report_list[key] == True:
            report.append(db[key])
    mdstr = ""
    mdstr += "# 诊断报告  \n"
    mdstr += "**掌纹一览**  \n"
    mdstr += "------ \n"
    mdstr += "![showall](http://localhost:8000/{0}_showall.jpg)  \n".format(IMAGE_USER)
    for feature in ["feature_7","feature_9","feature_10"]:
        mdstr += \
    '''
**{0}**
------
特征描述
> {1}

生理意义
> {2}

诊断结果&建议
> {3}
    '''.format(db[feature][0],db[feature][1],db[feature][2],"技术原因,暂时不能自动诊断,请根据上述资料和预处理图片自行判断")
    print(IMAGE_USER)
    with open("{0}_report.md".format(IMAGE_USER),"w") as  file:
        file.write(mdstr)

    os.system("md2pdf --theme=github --output "+IMAGE_USER+"_report.pdf "+IMAGE_USER+"_report.md ")
if __name__ == '__main__':
    report_list = {"feature_7":True,"feature_9":True}
    report("../image/yangxuanyue/yangxuanyue.jpg",report_list)
