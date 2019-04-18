#第二次project之二

##题目
- 代码实现Kruskal实现#2（基于UNION-FIND）

##思路
- 生成树函数的输出一样
- 生成树函数的输入为图以及点数，为了方便建立union
- 读入图之后，按照key为边的字典另存，value为list，主要是三项：point1，point2以及value值
- 排序可以直接使用python的sort函数（因为本题中排序不是重点），具体方法是将边号与value转为一个tuple，合起来变成一个EdgeWithWeight，然后使用sort(key = lambda x:(x[1]))，排序后的edgewithweight的第一项就是要的从小到大

##存储
- 不使用相同代码，按照思路第三条直接存储

### union
- leader与size:单独一个dict，key为点，value为两项的list：所在的集合的标号，集合的大小
- union：list内的不同的list