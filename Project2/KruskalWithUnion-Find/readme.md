#�ڶ���project֮��

##��Ŀ
- ����ʵ��Kruskalʵ��#2������UNION-FIND��

##˼·
- ���������������һ��
- ����������������Ϊͼ�Լ�������Ϊ�˷��㽨��union
- ����ͼ֮�󣬰���keyΪ�ߵ��ֵ���棬valueΪlist����Ҫ�����point1��point2�Լ�valueֵ
- �������ֱ��ʹ��python��sort��������Ϊ�������������ص㣩�����巽���ǽ��ߺ���valueתΪһ��tuple�����������һ��EdgeWithWeight��Ȼ��ʹ��sort(key = lambda x:(x[1]))��������edgewithweight�ĵ�һ�����Ҫ�Ĵ�С����

##�洢
- ��ʹ����ͬ���룬����˼·������ֱ�Ӵ洢

### union
- leader��size:����һ��dict��keyΪ�㣬valueΪ�����list�����ڵļ��ϵı�ţ����ϵĴ�С
- union��list�ڵĲ�ͬ��list