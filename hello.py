import pandas as pd

data = {'Subject': ['KOR','MATH','ENG'], 'Grade':[100,90,90] }

dataframe = pd.DataFrame(data)

print(dataframe)
print(dataframe.index)
print(dataframe.columns)
print(dataframe['Grade'])
print(dataframe.iloc[:2])
print(dataframe[dataframe['Grade']==100])
