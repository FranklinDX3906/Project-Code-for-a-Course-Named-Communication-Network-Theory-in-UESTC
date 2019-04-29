#coding:UTF-8

#使用桶实现迪杰斯特拉
#coder：张毅恒 信息与通信工程学院物联网工程

import datetime

def DijkstraWithBucket(Graph,MaxValue):
    FileResult = open("D:/1文件/通信网理论基础/Project/第三次project/proj3/resultBucket_4.txt", mode = 'w')#用于存储结果
    starttime = datetime.datetime.now()#开始时间
    for s in Graph:#对于每一个起始点
        WeightOfAll = 0#到达所有点的权重之和（其实只是方便判断准确性）
        Parent = {s:s}#父节点，用于输出边最后输出前再搞
        Distance = {s:0}#到初始点的距离
        V = set([s])#一个包含所有点的集合
        for u in Graph:
            V.add(u)#录入所有的点
        X = set([])#已覆盖的点的集合
        Path = {s:[]}#用于存储s到其他点的路径
        for u in V-set([s]):
            Distance[u] = 65535#初值尽量大，同等于无穷
            Parent[u] = u#父节点设置为自己
        
        #下面开始建桶，用list内的set实现，一共maxvalue+1个桶
        Buckets = [set([])]
        i = 1
        while i<=MaxValue:
            Buckets.append(set([]))
            i = i+1
        Buckets[0].add(s)#将s放入0号桶
        
        #正式开始
        i = 0#桶指针初值桶指针始终小于maxvalue+1
        while V-X:
            #寻找最小值并维护
            count = 0#用于判断是不是桶空
            BreakTwo = False#跳出两层循环的标志
            while len(Buckets[i]) == 0:
                i =(i+1)%(MaxValue+1)
                count = (count+1)%(MaxValue+1)
                if count == 0:#说明循环一周也没有找到元素，说明桶是空的，为了防止死循环，需要结束两层循环了
                    BreakTwo = True#跳出两层循环的标志
                    break
            if BreakTwo:#跳出两层循环
                break
            BreakTwo = False
            count = 0
            point = Buckets[i].pop()
            
            #维护X
            X = X|set([point])
            
            #更新邻接点并维护桶
            for u in Graph[point]:
                if Distance[u] == 65535:#说明一定会更新并且原来不在桶内
                    Distance[u] = Distance[point]+Graph[point][u]#更新值
                    
                    #维护桶
                    Buckets[(Distance[u])%(MaxValue+1)].add(u)
                    Parent[u] = point
                else:#不是65535，原来在桶里面
                    if Distance[u] > Distance[point]+Graph[point][u]:
                        Buckets[Distance[u]%(MaxValue+1)].remove(u)#原来桶里面删掉
                        Distance[u] = Distance[point]+Graph[point][u]#更新值
                        Buckets[Distance[u]%(MaxValue+1)].add(u)#新的桶增加
                        Parent[u] = point
                    else:
                        continue
                    
        #计算路径
        for u in V-set([s]):
            parent = Parent[u]
            Path[u] = [u]#先给path初值
            if parent == u:#没有路径
                Path[u] = 'NoPath'
            else: 
                while parent != s:
                    Path[u].insert(0,parent)
                    parent = Parent[parent]#继续找
                Path[u].insert(0,s)
        
        #输出屏幕和文件输出均有
        print("从",s,"出发到达其他点的路径以及距离为：")
        FileResult.write("从")
        FileResult.write(s)
        FileResult.write("出发到达其他点的路径以及距离为：\n")
        for u in V-set([s]):
            print(u,"：\n路径：",Path[u],"\n距离：",Distance[u])
            FileResult.write(u)
            FileResult.write("：\n路径：")
            for v in Path[u]:
                FileResult.write(v)
                FileResult.write("，")
            FileResult.write("\n距离：")
            FileResult.write(str(Distance[u]))
            FileResult.write("\n")
            WeightOfAll = Distance[u]*(1-(Distance[u] == 65535)) + WeightOfAll
        print("距离之和为：",WeightOfAll)
        FileResult.write("距离之和为：")
        FileResult.write(str(WeightOfAll))
        print("\n")
        FileResult.write("\n\n")
        
    #执行时间
    endtime = datetime.datetime.now()
    print("总执行时间（读取文件不计入）为：")
    FileResult.write("总执行时间（读取文件不计入）为：\n")
    print(endtime-starttime)
    FileResult.write(str(endtime-starttime))
 
        


#读入图
Graph = {'1':{}}#初始化图（按照给定的图，是从1开始标号的）
with open('D:/1文件\通信网理论基础\Project/第三次project/proj3/graph_4.txt','r') as f:
    LineOfInformation = f.readline()#表示点和边的一行
    NumberOfPoint = int(LineOfInformation.strip().split()[0])#将点的个数读出
    NumberOfEdge = int(LineOfInformation.strip().split()[1])#将边的个数读出
    i = 1
    while i<=NumberOfPoint:
        Graph[str(i)] = {}
        i = i+1
    line = f.readline()#表示信息的行（第一行）
    MaxValue = 0#所有边权中的最大值，用于建桶
    while line:
        point1 = line.strip().split()[0]
        point2 = line.strip().split()[1]
        value = int(line.strip().split()[2])
        if point2 in Graph[point1]:
            Graph[point1][point2] = min(value,Graph[point1][point2])#有向图
        else:
            Graph[point1][point2] = value
        if value > MaxValue:
            MaxValue = value
        line = f.readline()
DijkstraWithBucket(Graph,MaxValue)
