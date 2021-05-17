import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


data = pd.read_csv('DataFinal5.csv', sep=',')
data = data.loc[(data['Area'] < 4001)]
data = data.loc[(data['Number of rooms'] == 1)]
# data = data.loc[(data['Locality'] > 8000)]
# data = data.loc[(data['Price'] < 1000000)]

plt.plot(data["Area"], data["Price"], 'ko')
plt.tick_params(axis='x', rotation=70,)
plt.title('price vs province')
plt.xlabel('Province')
plt.ylabel('Price')
plt.show()

print(data.loc[data["Area"].idxmax()])
