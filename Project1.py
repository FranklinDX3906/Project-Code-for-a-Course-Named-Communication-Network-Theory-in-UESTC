# -*- coding: utf-8 -*-
def PrintAllTheRoute (graph,s,d): #s表示初始点，d表示终结点
    stack = [s] #用于DFS之中存储路径点
    HasBeenConsideredByItsFather = {s:set([])} #用于判断是否已被父节点考虑
    i=0
    while stack: #栈空则表明结束
        OldLength = len(stack)
        for u in graph[stack[-1]]:
            if not (u in stack):
                if not (u in HasBeenConsideredByItsFather[stack[-1]]): #既没有被父节点考虑过，也不在栈内，可以入栈
                    stack.append(u)
                    HasBeenConsideredByItsFather[u] = set([])
                    if stack[-1] == d: #栈顶是终点，输出
                        i = i+1
                        print('第',i,'种路径')
                        print(stack)
                    else:
                            pass
                    break #防止多入，每个点最多考虑一个邻接点
                else:
                    continue
            else:
                continue
        if len(stack) == OldLength: #说明没有点入栈，应该采取出栈，此时，直接将它从“考虑”dict内remove
            if i==0:#说明起始点与终点不连通
                print("没有找到路径！")
                return 0
            PointOut = stack.pop()
            HasBeenConsideredByItsFather.pop(PointOut)
            if stack:
                HasBeenConsideredByItsFather[stack[-1]].add(PointOut)#将刚刚出栈的点计入栈顶元素的“考虑”的dict内
        else:
            pass
    return 0

'''
graph = {'A':['B','G'],
            'B':['A','G','C'],
            'C':['B','F','D','E'],
            'D':['C','E'],
            'E':['D','C','F'],
            'F':['C','E','G'],
            'G':['A','B','F']}#用于验证，图见文件夹
PrintAllTheRoute(graph, 'A', 'E')
'''