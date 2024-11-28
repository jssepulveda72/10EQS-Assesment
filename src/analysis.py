import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
import numpy as np
import os
import re
from utils import dataC,barplot


data = pd.read_csv("products.csv")
data.reset_index
data.columns = ["our_price",
                "category",
                "stock",
                "stock_treshold",
                "date",
                "nan"]

data["our_price"] = data["our_price"].apply(lambda x: float(re.findall("[0-9].*", x)[0]))
data = data.drop(["date","nan"], axis = 1)


barplot(data)

