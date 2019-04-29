#coding:UTF-8

#用堆实现迪杰斯特拉
#coder：张毅恒 电子科技大学信息与通信工程学院 物联网工程
import datetime

def DijkstraWithHeap(Graph):##函数只输入图，因为结果上要求所有点
    FileResult = open("D:/1文件/通信网理论基础/Project/第三次project/proj3/resultHeap_4.txt", mode = 'w')#用于存储结果
    starttime = datetime.datetime.now()#开始时间
    for s in Graph:#对于每一个起始点
        WeightOfAll = 0#到达所有点的权重之和（其实只是方便判断准确性）
        Parent = {s:s}#父节点，用于输出边最后输出前再搞
        Distance = {-1:-1,s:0}#到初始点的距离
        V = set([s])#一个包含所有点的集合
        for u in Graph:
            V.add(u)#录入所有的点
        X = set([])#已覆盖的点的集合
        Path = {s:[]}#用于存储s到其他点的路径
        for u in V-set([s]):
            Distance[u] = 65535#初值尽量大，同等于无穷
            Parent[u] = u#父节点设置为自己
        
        #建堆
        Heap = [-1,s]#第一个值空出为0
        HeapLocation = {-1:0,s:1}#用于快速查询对应元素的位置
        i = 1#堆内最后一个元素的位置
        length = 2#堆的元素个数
        for u in V-set([s]):
            i = i+1
            Heap.append(u)#把点加入最后一个元素，此时i即为位置
            HeapLocation[u] = i
            length = length+1#因为刚开始建堆的时候所有的距离都是无穷，所以不需要维护
            
        while V-X:#未覆盖所有点
            #输出最小元素
            point = Heap[1]#输出堆顶元素
            Heap[1] = Heap[length-1]#将堆最后一个元素补上
            HeapLocation[Heap[1]] = 1#同时更新位置
            length = length-1#堆内元素个数减一
            
            #维护堆
            i = 1
            while 2*i<length:
                if (Distance[Heap[2*i]]<Distance[Heap[2*i+1]]):
                    if (Distance[Heap[i]]>Distance[Heap[2*i]]):
                        temp = Heap[i]
                        Heap[i] = Heap[2*i]
                        Heap[2*i] = temp#交换两个节点的位置
                    
                        templocation = HeapLocation[Heap[i]]
                        HeapLocation[Heap[i]] = HeapLocation[Heap[2*i]]
                        HeapLocation[Heap[2*i]] = templocation#交换同时在字典内更新两个节点的位置
                        i = 2*i
                    else:
                        break
                
                else:
                    if (Distance[Heap[i]]>Distance[Heap[2*i+1]]):
                        temp = Heap[i]
                        Heap[i] = Heap[2*i+1]
                        Heap[2*i+1] = temp#交换两个节点的位置
                    
                        templocation = HeapLocation[Heap[i]]
                        HeapLocation[Heap[i]] = HeapLocation[Heap[2*i+1]]
                        HeapLocation[Heap[2*i+1]] = templocation#交换同时在字典内更新两个节点的位置
                        i = 2*i+1
                    else:
                        break
            
            #维护一下集合
            X = X|set([point])
            
            #根据这个点维护其他边
            for u in Graph[point]:
                if Graph[point][u]+Distance[point] <Distance[u]:
                    Distance[u] = Graph[point][u]+Distance[point]
                    Parent[u] = point
                    
                    #维护堆
                    i = HeapLocation[u]
                    while Distance[Heap[i]]<Distance[Heap[int(i/2)]]:
                        temp = Heap[i]
                        Heap[i] = Heap[int(i/2)]
                        Heap[int(i/2)] = temp
                        
                        HeapLocation[Heap[i]] = i
                        HeapLocation[Heap[int(i/2)]] = int(i/2)
                        i = int(i/2)
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
    while line:
        point1 = line.strip().split()[0]
        point2 = line.strip().split()[1]
        value = int(line.strip().split()[2])
        if point2 in Graph[point1]:#已有值，取最小者
            Graph[point1][point2] = min(value,Graph[point1][point2])#有向图
        else:
            Graph[point1][point2] = value
        line = f.readline()
DijkstraWithHeap(Graph)

    