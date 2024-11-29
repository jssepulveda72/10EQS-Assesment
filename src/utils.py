import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
import numpy as np




dataC = pd.read_excel("comparative_data.xlsx")
dataC["Average"] = dataC.mean(axis=1, numeric_only = True)
dataC = dataC.round(2)
dataC["Max"] = dataC.max(axis = 1, numeric_only = True)
dataC["Min"] = dataC.min(axis = 1, numeric_only = True)
dataC = dataC.drop(columns = [f"price{i}" for i in range(1,5)])



def barplot(data):
    plt.figure(figsize=(16,6))
    bar_colors = ["cyan","magenta","orange"]
    x = 0
    width =0.25
    mutiplier = 0
    for i in range(len(data.index)):
        offset = width*3*mutiplier
        plt.bar(x = [x + offset,
                     x + 2*offset,
                     x + 3* offset], 
                height = [dataC["Max"][i],
                          dataC["Average"][i],
                          data["our_price"][i]],
                color = bar_colors,
                label = ["Max","Average","Our"],
                width = [0.5,0.5,0.5])
        
        plt.xticks(x+2*offset,data.index[i])