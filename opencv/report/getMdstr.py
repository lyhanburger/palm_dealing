from NN import NN
def mdstr_image(img_src):
    mdstr = "<h1>诊断报告</h1>  \n"
    mdstr += "<h3>掌纹一览</h3>  \n"
    mdstr += '''<img src={0} width="500",height="1000" alt="手掌图片">'''.format(img_src)
    return mdstr
def mdstr_wangchengxia(feature_map):
    db = {
            "7线":["位于无名指下方的竖线","高血压或者低血压"],
            "9线":["起于食指与中指指缝之间,以弧形延伸到无名指与小指指缝之间","过敏体质,接触电脑频繁,不孕症"],
            "10线":["中指掌指褶纹下一弧形半月圆","近视眼"]
            }

    #mdstr = "###王晨霞图典  \n "
    #mdstr += "#####特征提取  \n "
    #mdstr += "|   名称        |     描述      |    结果       |  \n"
    #mdstr += "| ------------- | --------------| --------------|  \n"
    mdstr = "<hr><h3>王晨霞图典</h3>"
    mdstr += "<h5>特征提取</h5>"
    mdstr += "<table>"
    mdstr += "<tr><th>名称</th><th>描述</th><th>结果</th></tr>"
    for feature in db:
        mdstr += "<tr> <td>{0}</td><td>{1}</td><td> {2} </td></tr>  \n".format(feature, db[feature][0], feature in feature_map)
    mdstr += "</table>\n"

    mdstr += "<h5>诊断结果</h5>  \n"
    mdstr += "<ul>"
    for feature in db:
        if feature in feature_map:
            
            mdstr += "<li> {0}</li> \n".format(db[feature][1])
    mdstr += "</ul>\n"

    return mdstr

def mdstr_NN(feature_map):
    db = {
            "7线":["位于无名指下方的竖线","高血压或者低血压"],
            "9线":["起于食指与中指指缝之间,以弧形延伸到无名指与小指指缝之间","过敏体质,接触电脑频繁,不孕症"],
            "10线":["中指掌指褶纹下一弧形半月圆","近视眼"]
            }
    illness_map = NN.NN(feature_map)
    mdstr = "<hr><h3>神经网络预测</h3>"
    mdstr += "<h5>特征提取</h5>"
    mdstr += "<table>"
    mdstr += "<tr><th>名称</th><th>描述</th><th>结果</th></tr>"
    for feature in db:
        mdstr += "<tr> <td>{0}</td><td>{1}</td><td> {2} </td></tr>  \n".format(feature, db[feature][0], feature in feature_map)
    mdstr += "</table>\n"

    mdstr += "<h5>诊断结果</h5>  \n"
    mdstr += "<table>"
    mdstr += "<tr><th>名称</th><th>概率</th></tr>"
    for illness in illness_map:
        mdstr += "<tr><td> {0} </td><td> {1} </td></tr> \n".format(illness,illness_map[illness])
    mdstr += "</table>\n"

    return mdstr
def mdstr_head():
    mdstr = '''
<head>
<style>
table {
    font-family: arial, sans-serif;
    border-collapse: collapse;
    width: 100%;
}

td, th {
    border: 1px solid #dddddd;
    text-align: left;
    padding: 8px;
}

tr:nth-child(even) {
    background-color: #dddddd;
}
</style>
</head>
    '''
    return mdstr
