# -*- coding: utf-8 -*-

from _datetime import datetime

starttime = datetime.now()#程序的开始时间

def PrimForMSTWithHeap(G,s):#生成最小生成树的函数，输入图以及起始点
    WeighOfMST = 0
    Parent = {s:s}#对应父节点，用于输出边
    Distance = {-1:-1,s:0}#对应到树的距离
    V = set([s])#所有的点的集合
    for u in G:
        V.add(u)
    X = set([])#已覆盖的点集合
    T = set([(s,s)])#生成树，最后输出
    for u in V-set([s]):
        Distance[u] = 65535#相对于无穷
        Parent[u] = u#因为定义为null可能需要调用库，所以先赋值为自身
    
    Heap = [-1,s] #以下步骤为建堆，堆的第一个元素空出为-1
    HeapLocation = {-1:0,s:1}#这个字典记录的是堆内各个元素在堆数组的位置，为的是方便删除某一个特定元素的时候直接找到而不是遍历
    i=1#表示最后一个元素的位置，用于之后冒泡
    length = 2#表示堆的元素个数
    for u in V-set([s]):
        i = i+1
        Heap.append(u)#把一个元素插入最后
        while Distance[Heap[i]]<Distance[Heap[int(i/2)]]:#比父节点小
            temp = Heap[i]
            Heap[i] = Heap[int(i/2)]
            Heap[int(i/2)] = temp#交换节点位置即可，dict内无需交换
            i = int(i/2)
        HeapLocation[u] = i#记录此时u节点的位置
        length = length+1
        i = length-1#结束所有循环后lengh就是heap的长度
    
    while (V-X):
        point = Heap[1]#输出堆顶元素
        Heap[1] = Heap[length-1]
        HeapLocation[Heap[1]] = 1#将更新后的堆顶元素的位置参数更新
        length = length-1#将堆长度减一防止之后重复录入

        i = 1
        while 2*i<length:
            if (Distance[Heap[2*i]]<Distance[Heap[2*i+1]]):
                if (Distance[Heap[i]]>Distance[Heap[2*i]]):#这一步while循环的目的是去除堆顶元素并且将最后一个节点搬到顶端后维护堆
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


        T = T|set([(Parent[point],point)])#将边归入T
        if Parent[point] != point:
            WeighOfMST = WeighOfMST+G[Parent[point]][point]

        X = X|set([point])
        for v in G[point]:
            if G[point][v] < Distance[v]:
                Distance[v] = G[point][v]
                Parent[v] = point
                i = HeapLocation[v]#直接使用字典输出v的位置
                while Distance[Heap[i]]<Distance[Heap[int(i/2)]]:
                    temp = Heap[i]
                    Heap[i] = Heap[int(i/2)]
                    Heap[int(i/2)] = temp
                    HeapLocation[Heap[i]] = i
                    HeapLocation[Heap[int(i/2)]] = int(i/2)
                    i = int(i/2)
            else:
                continue
    print("最小生成树的边为：\n")
    print(T)
    print("权重之和为：\n")
    print(WeighOfMST)
    return 0
    

G = {'0':{}}#初始化图
with open('D:/1文件\通信网理论基础\Project/第二次project/workspace/testgraph/graph_12.txt','r') as f:
    LineOfInformation = f.readline()#表示点和边的一行
    Number = int(LineOfInformation.strip().split()[0])
    i = 0
    while i<Number:
        G[str(i)] = {}
        i = i+1
    line = f.readline()#表示信息的行（第一行）
    while line:
        point1 = line.strip().split()[0]
        point2 = line.strip().split()[1]
        value = int(line.strip().split()[2])
        G[point1][point2] = value
        G[point2][point1] = value
        line = f.readline()
PrimForMSTWithHeap(G, '0')

endtime = datetime.now()#程序结束时间
print("运行时间为：\n")
print(endtime-starttime)#输出程序执行的时间