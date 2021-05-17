import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
data = pd.read_csv('DataFinal8.csv', sep=',')

#data_per = data.groupby('Province').agg(percentage =('Price', lambda p: p.sum() / data.sum() * 100)).round(2)

#Data to plot
labels = ['Brussel', 'Flanders', 'Wallonia']
labels_pro =['Brussel',
            'Anvers',
            'Brabant Flamand',
            'Flandre Occidental',
            'Flandre Oriental',
            'Limbourg',
            'Brabant Wallon',
            'Hainaut',
            'Liège',
            'Luxembourg',
            'Namur']
sizes = [504, 337, 415, 280]
labels_gender = ['Man', 'Woman', 'Man', 'Woman', 'Man', 'Woman', 'Man', 'Woman']
sizes_gender = [315, 189, 125, 212, 270, 145, 190, 90]
colors = ['#FFEBCD', '#FFB6C1', '#BC8F8F', '#66b3ff']
colors_gender = ["#20B2AA","#AFEEEE","#7FFFD4", "#5F9EA0", "#4682B4", "#6495ED", "#ADD8E6","#00008B" , "#8A2BE2", "#4B0082","#7B68EE"]
#data_pro = data.groupby(['Region',"Province"]).size()
# Plot
plt.pie(data.groupby("Region").size(), labels=labels, colors=colors, startangle=90, frame=True)
plt.pie(data.groupby("Province").size(),labels=labels_pro,colors=colors_gender, radius=0.75, startangle=90)
centre_circle = plt.Circle((0, 0), 0.5, color='black', fc='white', linewidth=0)
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.axis('equal')
plt.tight_layout()
plt.show()
plt.savefig("StateMarketby.png")

#print(data_pro.index)
#print(data_pro["Province"])