from efficient_apriori import apriori
import pandas as pd

data = pd.read_csv('./Market_Basket_Optimisation.csv', header = None)
print(data.head())
transactions = []
for i in range(0,data.shape[0]):
    temp = []
    for j in range(0,data.shape[1]):
        if str(data.values[i,j]) != 'nan':
            temp.append(data.values[i,j])
    transactions.append(temp)
itemsets,rules = apriori(transactions,min_support = 0.05, min_confidence = 0.2)
print("频繁项集：",itemsets)
print("关联规则：",rules)