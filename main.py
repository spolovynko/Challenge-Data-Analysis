import pandas as pd
from utils.utils import *
import numpy as np
data = pd.read_csv('databasetest.csv', sep=',')

"""Delete rows without prices"""
drop_row_without_value("Price",data)

del data['Surface area of the plot of land']
del data['Unnamed: 0']
del data['Url']
data = data.drop(data.index[np.where(data["Subtype of property"] == "building")[0]])


data['Surface of the land'] = data['Area'] + data['Terrace Area'] + data['Garden Area']


""" put region column """

data["Province"] = data.apply(lambda x: change_to_province(x["Locality"])[0], axis=1)
data["Region"] = data.apply(lambda x: change_to_province(x["Locality"])[1], axis=1)

data_final = data.reset_index()

print(data.info())
data_final.to_csv("DataFinal5.csv")



