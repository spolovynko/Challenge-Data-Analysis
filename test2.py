import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


data = pd.read_csv('DataFinal5.csv', sep=',')

data = data.loc[(data['Province'] == "Flandre Occidental")]

plt.plot(data["Area"], data["Price"], 'ko')
plt.tick_params(axis='x', rotation=70,)
plt.title('price vs province')
plt.xlabel('Province')
plt.ylabel('Price')
plt.show()


print(data.iloc[(data["Price"]/data["Area"]).idxmax()])
