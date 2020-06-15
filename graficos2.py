import requests
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
"""
download_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data"
target_csv_path = "wineData.csv"
response = requests.get(download_url)
response.raise_for_status()
with open(target_csv_path, "wb") as f:
    f.write(response.content)


df = pd.read_csv("wineData.csv")
print(type(df))
print(df.shape)
print(df.head)

#plt.plot(df["Alcohol"][0:20])
plt.subplot(211, title="Alcohol")
plt.plot(df["Alcohol"][0:100], "ro")
plt.subplot(212, yscale="log")
plt.plot(df["Magnesium"][0:100])

plt.show()
"""

l1 = range(5)
l2 = range(5)

result = [(x+y) for x,y in zip(l1,l2)]
print(result)

a1=np.arange(5)
a2=np.arange(5)
result =a1 + a2
