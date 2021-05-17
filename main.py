import pandas as pd
from utils.utils import *
import numpy as np


data = pd.read_csv('databasetest.csv', sep=',')
data = data.loc[(data['Area'] < 4001)]
"""Delete rows without prices"""
drop_row_without_value("Price", data)
data["PriceperMeter"] = data["Price"]//data["Area"]


#data['Surface of the land'] = data['Area'] + data['Terrace Area'] + data['Garden Area']


""" put region column """

data["Province"] = data.apply(lambda x: change_to_province(x["Locality"])[0], axis=1)
data["Region"] = data.apply(lambda x: change_to_province(x["Locality"])[1], axis=1)
data["Prov_num"] = data.apply(lambda x: change_to_province(x["Locality"])[2], axis=1)
data["Region_num"] = data.apply(lambda x: change_to_province(x["Locality"])[3], axis=1)

data = data.drop(data.index[np.where(data["Subtype of property"] == "building")[0]])
del data['Surface area of the plot of land']
del data['Unnamed: 0']
del data['Url']
del data['Source']
del data['Garden Area']
del data['Surface of the land']
#del data['Type of property']
#del data['Subtype of property']
#del data['Type of sale']
#del data['State of the building']
#del data['Province']
#del data['Region']
#data = data.drop(data.index[np.where(data["Subtype of property"] == "building")[0]])


#data['Surface of the land'] = data['Area'] + data['Terrace Area'] + data['Garden Area']


""" put region column """

# data["Province"] = data.apply(lambda x: change_to_province(x["Locality"])[0], axis=1)
# data["Region"] = data.apply(lambda x: change_to_province(x["Locality"])[1], axis=1)
# data["Prov_num"] = data.apply(lambda x: change_to_province(x["Locality"])[2], axis=1)
# data["Region_num"] = data.apply(lambda x: change_to_province(x["Locality"])[3], axis=1)
data_final = data.reset_index()

print(data.info())
data_final.to_csv("DataFinal8.csv")



