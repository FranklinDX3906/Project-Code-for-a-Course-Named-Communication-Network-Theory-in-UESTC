# 第三次project之一
## 题目
- 代码实现Dijkstra #3（基于堆）

## 思路
- 照搬上一个代码（无向图变有向图）
- 函数只输入图
- 输出所有结果（所有点到点的路径加值，没有路径则输出无）

## 存储（数据结构）
- 图：字典套字典
- 父节点（parent）：字典
- 距离：字典
- 堆：list，但是维护一个字典用于存位置
- 路径：字典套list

## 其他
- 用了一个文件来存储结果
