import numpy as np
# 1、先定义一个人物类
persontype = np.dtype({
    'names':['name','chinese','english','math'],
    'formats':['S32','i','i','i']
})
# 2、将数据加载
peoples = np.array([("ZhangFei",68,65,30),("GuanYu",95,76,98),("LiuBei",98,86,88),("DianWei",90,88,77),("XuChu",80,90,90),],dtype=persontype)
# 3、统计单科成绩
chineses = peoples[:]['chinese']
englishs = peoples[:]['english']
maths = peoples[:]['math']
# 平均成绩
print(np.mean(chineses))
print(np.mean(englishs))
print(np.mean(maths))
# 输出最小值和最大值
print(np.amin(chineses))
print(np.amin(englishs))
print(np.amin(maths))
print(np.amax(chineses))
print(np.amax(englishs))
print(np.amax(maths))
# 计算方差和标准差
print(np.std(chineses))
print(np.var(chineses))
print(np.std(englishs))
print(np.var(englishs))
print(np.std(maths))
print(np.var(maths))
# 排序
# ①所有成绩
a = np.array([chineses,englishs,maths])
print(np.sort(a))
# ②按照三科成绩之和降序排列
#用sorted函数进行排序
ranking = sorted(peoples,key=lambda x:x[1]+x[2]+x[3], reverse=True)
print(ranking)
