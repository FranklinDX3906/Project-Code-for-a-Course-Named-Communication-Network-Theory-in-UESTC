# 第二次project之一

## 题目
- 代码实现Prim实现#4（基于堆）

## 思路
- 整个文件结构：
- 主体：读入数据输出数据;
- 生成树函数：输入图加权重，输出最小生成树的边以及权重和

## 存储方式
- 图：邻接链表，字典套字典
- 堆：堆的标号用list存，堆的值直接拿dict存，堆的位置另外拿一个dict存储,以方便修改元素时快速找到元素的位置，同时，堆具有长度length参数
- X,V,T均使用set
- p也用字典存

## 伪代码（与实现3的区别）
- 输出最小值使用heap[1],heap[0]永远空出
- 最开始就建好堆
- 点进入X之后将其从堆内删除（即删除堆顶的点）
- 点的d更新后将dict更新，并且在堆的list内删除，在尾部添加，最后维护，