
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig = plt.figure()
data = pd.read_csv('https://bit.ly/2WcsJE7', index_col=0, parse_dates=True)

ts = pd.Series(np.random.normal(size=50),index=pd.date_range(start='1/1/2019', periods=50))
data.Volume.iloc[:100].plot(color='green')


plt.show()