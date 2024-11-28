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
    
    
    for i in range(len(data.index)):
        plt.figure(figsize=(16,6))
        plt.bar(x = range(3), 
                height = [dataC["Max"][i],
                          dataC["Min"][i],
                          data["our_price"][i]])