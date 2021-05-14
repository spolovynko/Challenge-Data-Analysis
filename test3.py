import pandas as pd
import matplotlib.pyplot as plt


"""Mean by Region"""
data = pd.read_csv('DataFinal5.csv', sep=',')

reg_grp = data.groupby("Province")
mean_pr = reg_grp["Price"].mean().round(0)
plt.bar(mean_pr.index, mean_pr.values)
plt.tick_params(axis='x', rotation=70)
plt.title('price vs province')
plt.xlabel('Province')
plt.ylabel('Price')
plt.show()


print(data.iloc[(data["Price"]/data["Area"]).idxmax()])
