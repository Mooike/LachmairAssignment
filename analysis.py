import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def convert_to_float(s):
    try:
        return float(s)
    except ValueError:
        return np.nan

df = pd.read_csv("test.csv",
                 converters = {'start_x': convert_to_float,
                              'start_y': convert_to_float,
                              'stop_x': convert_to_float,
                              'stop_y': convert_to_float,
                               'distance': convert_to_float,
                               'traveltime': convert_to_float})

sns.lmplot(x = "distance", y = "traveltime", data = df)
plt.show()