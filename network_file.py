import requests,json,time
job_all = []
def job_alls (Job_name,url_addres):
    
    #用于读取本地文件内容到内存中
    '''with open(f"./{Job_name}","r",encoding="utf-8") as f:
        for i in f.readlines():
            opc = i.strip()        
            job_all.append(opc)
        print("总个数",len(job_all))'''
    
    
    
    #GET请求所有监控类型的job
    #url = 'https://dba-monitor-prod.baozun.com/prometheus/api/v1/query?query=sum%20by%20(job)(%7Bjob%3D~%22.%2B%22%7D)&time=1672908733.471&_=1672884801374'
    #接口get请求
    url = f'{url_addres}/api/v1/query'
    params = {
    'query': "",
    'time': '1672992970.651',
    '_': '1672992826455'
    }
    params["query"] = Job_name
    Date = requests.get(url=url,params=params)
    #print (Date)
    #json文件转成列表
    rejson = json.loads(Date.text)
    for i in range(len(rejson["data"]['result'])):
        ui = rejson["data"]['result'][i]['metric']['job']
        job_all.append(ui)
        time.sleep(1)
        print(ui)