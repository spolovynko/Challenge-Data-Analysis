import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn
''' regression lineaire '''
data = pd.read_csv('DataFinal5.csv', sep=',')

data = data[data["Area"] < 1000]
data = data[(data["Price"] < 1000000) & (data["Price"] > 200000)]

price_m = (data["Price"]/data["Area"]).round()
reg_bxl = data.loc[(data['Locality'] == 1000)]


plt.tick_params(axis='x', rotation=70)
plt.title('Brussel : Price vs Terrace')
coef = np.polyfit(reg_bxl["Area"], reg_bxl["Price"], 1)
poly1d_fn = np.poly1d(coef)
plt.plot(reg_bxl["Area"],reg_bxl["Price"], 'mo', reg_bxl["Area"], poly1d_fn(reg_bxl["Area"]), '--k')
plt.xlabel('Terrace')
plt.ylabel('Price')

# = np.rad2deg(np.arctan2(reg_bxl["Price"][-1] - reg_bxl["Price"][0],
                              #reg_bxl["Area"][-1] - reg_bxl["Terrace Area"][0]))
#print(angle)
#plt.savefig("Brussel_Garden Vs Price.png")
#plt.savefig("PriceTerraceBrusselsqmetter.png")
plt.show()
#angle = np.rad2deg(np.arctan2(y[-1] - y[0], x[-1] - x[0])

# mean_pr = reg_grp["Price"].mean().round(0)
# plt.bar(mean_pr.index, mean_pr.values)
# plt.tick_params(axis='x', rotation=70)
# plt.title('price vs province')
# plt.xlabel('Province')
# plt.ylabel('Price')
# plt.show()
