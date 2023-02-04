import requests,time,json
import local_file as local
import Storage



# 获取所有监控类型下指标名称
def main(vulesa,Urli,url_addres):
    #接口get请求
    url = f'{url_addres}/api/v1/query'
    params = {
    'query': "",
    'time': '1672992970.651',
    '_': '1672992826455'
    }
    
    # 获取外部实参
    ucc = []
    #url = f"https://dba-monitor-prod.baozun.com/prometheus/api/v1/query?query={Urli}&time=1672824408.398&_=1672821536179"
    params["query"] = Urli
    print (Urli)
    # get请求获取监控指标名称
    data = requests.get(url=url,params=params)
    #json文件转成列表
    rejson = json.loads(data.text)
    for i in range(len(rejson["data"]['result'])):
        ui = rejson["data"]['result'][i]['metric']['__name__']
        #value 数量
        Utp = rejson["data"]["result"][i]["value"][1]
        #time.sleep(0.5)
        
       
        #将单个元素字符串存入列表
        ucc.append(ui)
    print("指标总个数",len(ucc))
    #print (list(set(ucc) - set(ll)))
    # 差值，单个监控类型下独有的指标名称
    int_relust = list(set(ucc) - set(local.ll))
    #print (ucc)
    print ("没能匹配到的个数-不符合存储条件（默认10个为起点）：",len(int_relust))
    if len(int_relust) > 10:   
        vulesa = (f"{vulesa}--指标类型数量为：:{len(int_relust)}个")
        Storage.index(vulesa)
        
        for j in int_relust:
            Storage.index(j)
            
        Storage.index("\n")
        print ("写入完成，本次共写入指标:",len(int_relust))
        int_relust.clear()
        print ("列表--(int_relust)--清空情况",len(int_relust))
