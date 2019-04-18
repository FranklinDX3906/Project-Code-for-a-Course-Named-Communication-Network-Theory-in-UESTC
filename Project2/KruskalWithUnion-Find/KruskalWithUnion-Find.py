# -*- coding: utf-8 -*-

from _datetime import datetime

starttime = datetime.now()#程序的开始时间

def KruskalWithUnion_Find(G,n,m):#最小生成树函数，输入图以及点，边的个数，为了方便建立union
    LeaderandSize = {'0':[0,1]}#先建立union，含义为：{点的标号：[点所在的集合在union的标号，集合的元素个数]}
    Union = []
    i = 0
    while i<n:
        LeaderandSize[str(i)] = [i,1]#刚开始union的leader都是自身标号的位置
        Union.append([str(i)])
        i = i+1
    EdgeWithWeight = []#将边及其权重转为tuple然后存入一个list内
    for u in G:
        EdgeWithWeight.append((u,G[u][2]))
        
    EdgeWithWeight.sort(key=lambda x: x[1])#因为排序不是重点，所以直接调用sort，结果是按照第二项即weight排好的边
    '''
            下面开始最小生成树
    '''
    T = set(())#生成树
    Weight = 0
    i = 0
    while i<m:
        point1 = G[EdgeWithWeight[i][0]][0]#为了防止看花眼睛先把点抽出来
        point2 = G[EdgeWithWeight[i][0]][1]
        if LeaderandSize[point1][0] != LeaderandSize[point2][0]:#这条边的两个点的leader不一样
            T = T|set([(point1,point2)])#将边加入T
            Weight = Weight+EdgeWithWeight[i][1]#将权重计入总权重
            if LeaderandSize[point1][1]<LeaderandSize[point2][1]:#一号点所在的集合比较小
                Union[LeaderandSize[point2][0]] = Union[LeaderandSize[point2][0]]+Union[LeaderandSize[point1][0]]#将两个集合合并
                Union[LeaderandSize[point1][0]] = []#将小的那个集合置空以节省空间，但是不删除以防止位置变化
                for point in Union[LeaderandSize[point2][0]]:#一号点所在的集合更新leader以及size
                    LeaderandSize[point] = [LeaderandSize[point2][0],LeaderandSize[point1][1]+LeaderandSize[point2][1]]
            else:
                Union[LeaderandSize[point1][0]] = Union[LeaderandSize[point1][0]]+Union[LeaderandSize[point2][0]]#将两个集合合并
                Union[LeaderandSize[point2][0]] = []#将小的那个集合置空以节省空间，但是不删除以防止位置变化
                for point in Union[LeaderandSize[point1][0]]:#二号点所在的集合更新leader以及size
                    LeaderandSize[point] = [LeaderandSize[point1][0],LeaderandSize[point1][1]+LeaderandSize[point2][1]]

        i = i+1
    
    
    print("最小生成树为：\n")
    print(T)
    print("权重之和为：\n")
    print(Weight)
    return 0
    
    
    


G = {'0':['0','0',0]}#初始化图，含义是，边：[一个点，另一个点，边权值]
with open('D:/1文件\通信网理论基础\Project/第二次project/workspace/testgraph/graph_12.txt','r') as f:
    LineOfInformation = f.readline()#表示点和边的一行
    NumberofPoint = int(LineOfInformation.strip().split()[0])#读入点的个数
    NumberofEdge = int(LineOfInformation.strip().split()[1])#读到的是边的个数
    i = 0
    while i<NumberofEdge:
        G[str(i)] = ['0','0',0]#直接按照边为key的字典存储
        i = i+1
    i = 0
    line = f.readline()#表示信息的行（第一行）
    while line:
        point1 = line.strip().split()[0]
        point2 = line.strip().split()[1]
        value = int(line.strip().split()[2])
        G[str(i)][0] = point1
        G[str(i)][1] = point2
        G[str(i)][2] = value
        line = f.readline()
        i = i+1
KruskalWithUnion_Find(G,NumberofPoint,NumberofEdge)#调用生成树函数


endtime = datetime.now()#程序结束时间
print("运行时间为：\n")
print(endtime-starttime)#输出程序执行的时间