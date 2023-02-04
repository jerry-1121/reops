import re,requests,json,time,re


job_all = []
def job_alls (Job_name):
    
    #用于读取本地文件内容到内存中
    with open(f"./{Job_name}","r",encoding="utf-8") as f:
        for i in f.readlines():
            opc = i.strip()        
            job_all.append(opc)
        print("总个数",len(job_all))
    
    
    
    #GET请求所有监控类型的job
    #url = 'https://dba-monitor-prod.baozun.com/prometheus/api/v1/query?query=sum%20by%20(job)(%7Bjob%3D~%22.%2B%22%7D)&time=1672908733.471&_=1672884801374'
    """params["query"] = Job_name
    Date = requests.get(url=url,params=params)
    #print (Date)
    #json文件转成列表
    rejson = json.loads(Date.text)
    for i in range(len(rejson["data"]['result'])):
        ui = rejson["data"]['result'][i]['metric']['job']
        job_all.append(ui)
        time.sleep(1)
        print(ui)"""

#读取本地文件中所有指标名称
ll = []
def files ():
    with open("D:/Python/python_file_demo/index.txt","r",encoding="utf-8") as f:
        for i in f.readlines():
            opc = i.strip()        
            ll.append(opc)
        print("总个数",len(ll))

# 获取所有监控类型下指标名称
def main(vulesa,Urli):
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
    int_relust = list(set(ucc) - set(ll))
    #print (ucc)
    print ("没能匹配到的个数-不符合存储条件（默认10个为起点）：",len(int_relust))
    if len(int_relust) > 10:   
        vulesa = (f"{vulesa}--指标类型数量为：:{len(int_relust)}个")
        index(vulesa)
        
        for j in int_relust:
            index(j)
            
        index("\n")
        print ("写入完成，本次共写入指标:",len(int_relust))
        int_relust.clear()
        print ("列表--(int_relust)--清空情况",len(int_relust))

#单个监控类型下 指标名称
auxf = []
def contr_type(Urlisa):
    
    params["query"] = Urlisa
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

#接口get请求
url = 'http://thanos-query.cloud.bz/api/v1/query'
params = {
    'query': "",
    'time': '1672992970.651',
    '_': '1672992826455'
}

def index(indexs):
    with open("./prometheus_file/thanos-query.cloud.bz_100.txt","a+",encoding="utf-8") as sa:
        sa.write(str(indexs) + "\n")

# 入口函数 
if __name__ == "__main__":

    #被过滤的指标
    Index_Type = ["etcd","jvm","mysql","apiservice"]

    #查询的语句
   # Job_Name = """sum by (job)({job=~".+"})"""
    Job_Name = "123.txt"
    job_alls(Job_Name)
    print (job_all)
    
   # time.sleep(2)
    #读取所有比对指标名称的函数
    files()
    #所有job的监控类型
    for job_single in job_all:
        
    #Var = "microsoft-hk-node"
        print("--------------------------------------",len(auxf))
        Var = str(job_single)
        
        #单个监控类型下所有指标
        incommit= ("""count by (__name__)({job="%s"})""" %Var)
        print (incommit)
        contr_type(incommit)
        auxf = list(set(auxf))
        #print(type(list_set))
        print(auxf)
       # time.sleep(2)
        #auxf.clear()

        #单个类型下所有指标名称
        for j in auxf:
            print ("开始执行查找-------- 开始获取文件")
            
            boolsa = Var
            interaction = f"监控类型为----------------------------{boolsa}"    
            #单个类型下指定名称开头的指标
            # 判断指标vules 大于10 并且小于100的指标
            #Urlis = ("""count by (__name__)({job="%s",__name__=~"%s.*"}) > 10 < 100""" %(boolsa,j))
            Urlis = ("""count by (__name__)({job="%s",__name__=~"%s.*"}) > 100""" %(boolsa,j))

            print(Urlis)
            
            print("获取被查找的string")
            main(interaction,Urlis)
           # time.sleep(2)
        #清空列表中元素
        auxf.clear()


