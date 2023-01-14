#读取本地文件中所有指标名称
ll = []
def files ():
    with open("D:/Python/python_file_demo/index.txt","r",encoding="utf-8") as f:
        for i in f.readlines():
            opc = i.strip()        
            ll.append(opc)
        print("总个数",len(ll))