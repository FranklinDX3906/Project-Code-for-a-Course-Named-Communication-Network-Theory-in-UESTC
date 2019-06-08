#coding:UTF-8

import datetime

#函数主体
def PushRelabel(Graph,s,t,PointNumber):
    starttime = datetime.datetime.now()
    #初始化
    RelabelNumber = 0
    PushNumber = 0
    Result = Initialize(Graph,s,t,PointNumber)
    RemainGraph = Result[0]
    UsedGraph = Result[1]
    Height = Result[2]#将结果作为本函数初始化
    
    #建立盈余点
    SurplusPoint = set([])
    Surplus = {}#盈余量
    for u in Graph[s]:
        if(u != t):
            SurplusPoint.add(u)
            Surplus[u] = UsedGraph[s][u]
    
    #下面造桶并将元素放入桶内
    HeightBuckets = [set([])]
    i = 1
    while(i != 2*PointNumber):
        HeightBuckets.append(set([]))
        i +=1
    for u in SurplusPoint:
        HeightBuckets[Height[u]].add(u)
    
    #正式开始
    location = 2*PointNumber-1#开始为最后一个桶
    while SurplusPoint:#当还剩盈余点的时候
        if(location > 2*PointNumber-1):
            location = 2*PointNumber-1
        point = FindMax(HeightBuckets,location)[0]
        location = FindMax(HeightBuckets,location)[1]#得到点缓和位置
        
        #找高度小一的点
        w = '-1'
        for u in RemainGraph[point]:
            if(Height[u] == Height[point]-1):
                w = u
                break
        if(w != '-1'):#说明找到了
            #推送
            PushNumber += 1
            if(RemainGraph[point][w] >= Surplus[point]):#剩余容量大于盈余
                flow = Surplus[point]
                #更新剩余网络
                RemainGraph[point][w] -= flow
                if(RemainGraph[point][w] == 0):
                    RemainGraph[point].pop(w)#减为0 删掉
                if(point in RemainGraph[w]):#反向边已有
                    RemainGraph[w][point] += flow
                else:
                    RemainGraph[w][point] = flow
                #更新流量网络
                if(w in UsedGraph[point]):
                    UsedGraph[point][w] += flow
                else:
                    UsedGraph[w][point] -= flow
                #更新盈余
                Surplus.pop(point)
                SurplusPoint.remove(point)
                #更新桶
                HeightBuckets[location-1].remove(point)
            else:#剩余容量小于盈余
                flow = RemainGraph[point][w]
                #更新剩余网络
                RemainGraph[point].pop(w)#直接删边
                if(point in RemainGraph[w]):
                    RemainGraph[w][point] += flow
                else:
                    RemainGraph[w][point] = flow
                #更新流量网络
                if(w in UsedGraph[point]):
                    UsedGraph[point][w] += flow
                else:
                    UsedGraph[w][point] -= flow
                #更新盈余
                Surplus[point] -= flow
                #更新桶无
            #更新被推送的点的盈余并入桶
            if((w != s)&(w != t)):#不是起点或终点
                if(w in SurplusPoint):
                    Surplus[w] += flow
                else:
                    Surplus[w] = flow
                    SurplusPoint.add(w)
                    HeightBuckets[Height[w]].add(w)
            
        else:#没找到，更新高度
            RelabelNumber += 1
            #只需更新桶
            Height[point] +=1
            HeightBuckets[Height[point]-1].remove(point)
            HeightBuckets[Height[point]].add(point)
    
    #输出
    flow = 0
    for u in UsedGraph[s]:
        flow += UsedGraph[s][u]
    print('流分布为：')
    print(UsedGraph)
    inflow = 0
    for u in UsedGraph:
        for v in UsedGraph[u]:
            if(v == s):
                inflow += UsedGraph[u][v]
    print('和为：',flow-inflow) 
    print('relabel次数：',RelabelNumber)
    print('push次数：',PushNumber)
    endtime = datetime.datetime.now()
    print('运行时间为',endtime-starttime)
    
#寻找最大高度盈余点
def FindMax(HeightBuckets,location):
    #print(HeightBuckets,location)
    i = location
    while(len(HeightBuckets[i]) == 0):
        i -=1
    point = HeightBuckets[i].pop()
    HeightBuckets[i].add(point)#还到set里面
    return point,i+1

#初始化函数
def Initialize(Graph,s,t,PointNumber):
    RemainGraph = {}#剩余网络图，初始化为原图
    for u in Graph:
        RemainGraph[u] = Graph[u].copy()
    UsedGraph = {}#流量图，初始化为0
    for u in Graph:
        UsedGraph[u] = Graph[u].copy()
    for u in UsedGraph:
        for v in UsedGraph[u]:
            UsedGraph[u][v] = 0#将流量分别置为0
    
    #反向设置高度值
    Height = {}
    for u in Graph:
        Height[u] = 0#先都初始化为0为了之后方便
    ReverseGraph = {}#先将图反向
    for u in Graph:
        ReverseGraph[u] = {}
    for u in Graph:
        for v in Graph[u]:
            ReverseGraph[v][u] = Graph[u][v]
    #开始反向BFS
    BFSList = [t]
    while BFSList:
        v = BFSList.pop(0)
        for u in ReverseGraph[v]:
            if(Height[u] == 0):#说明还未访问到
                BFSList.append(u)
                Height[u] = Height[v]+1
    
    Height[s] = PointNumber#起点高度设置为n
    
    #饱和推送
    for u in UsedGraph[s]:
        UsedGraph[s][u] = RemainGraph[s][u]#饱和推送
        if(s in RemainGraph[u]):
            RemainGraph[u][s] += UsedGraph[s][u]
        else:
            RemainGraph[u][s] = UsedGraph[s][u]
        RemainGraph[s].pop(u)#更新剩余网络
    
    return RemainGraph,UsedGraph,Height
    


#主体，读入图，存储
Graph = {'0':{}}#初始化图文件
with open('D:/1文件/通信网理论基础/Project/第四次project/project4_graph/outgraph_7.txt') as f:
    LineOfInformation = f.readline()#读入第一行
    PointNumber = int(LineOfInformation.strip().split()[0])
    EdgeNumber = int(LineOfInformation.strip().split()[1])
    s = LineOfInformation.strip().split()[2]
    t = LineOfInformation.strip().split()[3]#读入起点终点
    i = 1
    while i!= PointNumber:
        Graph[str(i)] = {}#初始化图
        i = i+1
    line = f.readline()
    while line:
        Point1 = line.strip().split()[0]
        Point2 = line.strip().split()[1]
        Capacity = int(line.strip().split()[2])#容量
        Graph[Point1][Point2] = Capacity
        line = f.readline()
PushRelabel(Graph,s,t,PointNumber)