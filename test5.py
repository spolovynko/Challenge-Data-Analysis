import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
data = pd.read_csv('DataFinal8.csv', sep=',')

#sns.swarmplot(data = data,x="Area", y="Price",
              #hue='Type of property')
plt.figure(figsize=(16, 9))
sns.boxplot(data=data, x="Region", y="Price",)
           #order=['Anvers','Brabant Flamand',"Limbourg","Flandre Occidental","Flandre Oriental","Brussel",
                     #"Brabant Wallon","Liège","Namur","Hainaut","Luxembourg"])
#sns.barplot(x='Dim', y='Count', data=pd_df, order=pd_df['Dim'])`

plt.tick_params(axis='x', rotation=30)
plt.grid(True)
plt.ylim(00, 1200000)
plt.show()
plt.savefig("QuartileRegion.png")