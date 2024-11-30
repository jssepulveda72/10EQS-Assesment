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
    plt.figure(figsize=(20,8), layout = "constrained")
    bar_colors = ["blue","green","orange"]
    x = np.arange(len(data.index))
    width = 0.25
    
    
    for i in range(len(data.index)):
        
        bars = plt.bar(x = [x[i] + width,
                     x[i] + 2*width,
                     x[i] + 3*width], 
                height = [dataC["Max"][i],
                          dataC["Average"][i],
                          data["our_price"][i]],
                color = bar_colors,
                #label = ["Max","Average","Our"],
                width = width)
        
        plt.bar_label(bars, padding=3,rotation=0)
        
        
    plt.xticks(x,data.index,rotation = 15,minor = False)
    plt.legend(bars,["Max","Average","Our"],
               ncols = 3,
               loc = "upper left",
               fontsize = 15)
    plt.title("Price comparative", fontsize = 15)
    plt.savefig("Price comparision.png",dpi = 1200)
