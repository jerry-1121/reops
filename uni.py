
#获取数据源下所有job标签
import network_file as net
# 读取本地数据源已存在的指标
import local_file as local 
# 获取单个job标签下的所有指标
import contr
#获取单个job标签下分类的指标数量。
import Mains
#时间
import time





# # 入口函数 
# if __name__ == "__main__":

#请求域名地址：
Url_Add = "http://10.90.78.202:9090"

#被过滤的指标
Index_Type = ["etcd","jvm","mysql","apiservice"]

#查询的语句
Job_Name = """sum by (job)({job=~".+"})"""
#Job_Name = "123.txt"
net.job_alls(Job_Name,Url_Add)
print (net.job_all)

# time.sleep(2)
#读取所有比对指标名称的函数
local.files()
#所有job的监控类型 调用其他文件中函数结果。
for job_single in net.job_all:
    time.sleep(3)
    
#Var = "microsoft-hk-node"
    print("--------------------------------------",len(contr.auxf))
    Var = str(job_single)
    
    #单个监控类型下所有指标
    incommit= ("""count by (__name__)({job="%s"})""" %Var)
    print (incommit)

    """
    incommint: 查询的语句，
    Index_Type: 被过滤的指标
    Url_Add: 域名地址
    """
    contr.contr_type(incommit,Index_Type,Url_Add)
    auxf = list(set(contr.auxf))
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
        Urlis = ("""count by (__name__)({job="%s",__name__=~"%s.*"}) > 10 < 100""" %(boolsa,j))
        #Urlis = ("""count by (__name__)({job="%s",__name__=~"%s.*"}) > 100""" %(boolsa,j))

        print(Urlis)
        
        print("获取被查找的string")

        """
        interaction: 写入磁盘的提升语句
        Urlis: 查询语句
        Url_Add: 域名地址
        """
        Mains.main(interaction,Urlis,Url_Add)
        time.sleep(2)
    #清空列表中元素
    auxf.clear()