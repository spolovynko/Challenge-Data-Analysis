import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
"""HeatMap function"""
data = pd.read_csv('DataFinal5.csv', sep=',')
#data = data[(data["Price"] < 1000000) & (data["Price"] > 200000)]
data = data.loc[(data['Province'] == "Flandre Occidental")]
#print(data.info())
#data_sns = sns.load_dataset(data)
#sns.pairplot(data, height=2.5)
#plt.show()

plt.figure(figsize=(16,9))
sns.heatmap(data.corr(), annot=True, cmap="coolwarm")
plt.show()
print(data["Price"].value_counts())

