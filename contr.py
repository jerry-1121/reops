import requests,re,sys,json
#import uni
#单个监控类型下 指标名称


# url = 'https://dba-monitor-prod.baozun.com/prometheus/api/v1/query'
# params = {
#     'query': "",
#     'time': '1672992970.651',
#     '_': '1672992826455'
# }


auxf = []
def contr_type(Urlisa,Index_Type,url_addres):
    #接口get请求
    url = f'{url_addres}/api/v1/query'
    params = {
    'query': "",
    'time': '1672992970.651',
    '_': '1672992826455'
    }

    
    params["query"] = Urlisa
    print(url)
    print(params["query"])
    data = requests.get(url=url,params=params)
    #json文件转成列表
    rejson = json.loads(data.text)
    
    
    for i in range(len(rejson["data"]['result'])):
        ui = rejson["data"]['result'][i]['metric']['__name__']
        #value 数量
        Utp = rejson["data"]["result"][i]["value"][1]
        
        
        #单个job下的value个数
        #dict_vules = rejson["data"]['result'][i]['value'][1]
        
        #判断符合条件跳过本次循环，继续循环下一次。
        if ui == "up":
            continue
        elif ui == "ALERTS":
            continue
        #单指标已下划线结尾之前的字_符串类_型值
        konga = re.findall("(.*?)_.*?",ui)[0]
       # if konga in Index_Type:
        if konga in Index_Type:
            del konga
            continue
        del konga
        acc = re.findall("(.*?)_.*?",ui)[0]
        #print (acc)
        auxf.append(acc)
    print (len(set(auxf)))