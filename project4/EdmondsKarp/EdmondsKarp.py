#coding:UTF-8

import datetime
#算法函数主体
def EdmondsKarp(Graph,s,t):
    FileResult = open('D:/1文件/通信网理论基础/Project/第四次project/所有路径/graph7.txt',mode = 'w')
    starttime = datetime.datetime.now()
    count = 1
    RemainGraph = {}#剩余网络图
    for u in Graph:
        RemainGraph[u] = Graph[u].copy()
    UsedGraph = {}#流量图
    for u in Graph:
        UsedGraph[u] = Graph[u].copy()
    for u in UsedGraph:
        for v in UsedGraph[u]:
            UsedGraph[u][v] = 0#将流量分别置为0
    #print(UsedGraph)
    
    Result = FindMinPath(RemainGraph,s,t)
    while(Result):
        Path = Result[0]
        Capacity = Result[1]
        FileResult.write("第")
        FileResult.write(str(count))
        FileResult.write("条路为：\n")
        for u in Path:
            FileResult.write(u)
            FileResult.write(',')
        FileResult.write('\n')
        count +=1
        
        #更新剩余网络与流量
        #print(Path)
        i = 0
        while(Path[i] != t):
            #更新剩余网络
            RemainGraph[Path[i]][Path[i+1]] -= Capacity
            if(RemainGraph[Path[i]][Path[i+1]] == 0):#容量减为0
                RemainGraph[Path[i]].pop(Path[i+1])#删除这条边
            #增加或改变反向边
            if(Path[i] in RemainGraph[Path[i+1]]):
                RemainGraph[Path[i+1]][Path[i]] += Capacity
            else:
                RemainGraph[Path[i+1]][Path[i]] = Capacity
            #更新流量
            if(Path[i+1] in UsedGraph[Path[i]]):#说明是增加的容量
                UsedGraph[Path[i]][Path[i+1]] += Capacity
            else:
                UsedGraph[Path[i]][Path[i+1]] -= Capacity
            
            i +=1
        
        Result = FindMinPath(RemainGraph,s,t)
    #输出结果
    flow = 0
    for u in UsedGraph[s]:
        flow += UsedGraph[s][u]
    print('流分布为：')
    print(UsedGraph)
    print('和为：',flow)
    print('总共路径数：',count-1)
    endtime = datetime.datetime.now()
    print('运行时间：',endtime-starttime)
    

#寻找最小路径的函数
def FindMinPath(RemainGraph,s,t):
    Path = []#输出最终的最小路径，用于返回
    Capacity = 65535#记录路径上的最小容量，用于返回
    
    LayeredGraph = {s:{}}#分层图
    Visited = {s:0}#记录已访问的点
    for u in RemainGraph:
        Visited[u] = 0 #0表示未被访问
    Parent = {s:s}#记录父节点
    
    #下面正式生成子图
    BFSList = [s]#用于BFS使用
    Visited[s] = 1
    while BFSList:
        v = BFSList.pop(0)
        LayeredGraph[v] = {}
        for u in RemainGraph[v]:
            if(Visited[u] == 0):#如果是未被访问的点
                BFSList.append(u)#加入这个点
                Visited[u] = 1
                LayeredGraph[v][u] = RemainGraph[v][u]#在分层图中加入这个点
                Parent[u] = v
    
    #下面开始产生路径
    if(t not in Parent):#说明遍历没有遍历到t，没有路径了
        return False
    u = t
    Path = [u]
    while u != s:#等于说明找到了起点
        Path.insert(0, Parent[u])
        if(LayeredGraph[Parent[u]][u]<Capacity):
            Capacity = LayeredGraph[Parent[u]][u]
        u = Parent[u]
    
    #返回值
    return Path,Capacity

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
EdmondsKarp(Graph,s,t)