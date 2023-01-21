import pandas as pd

data = {
    "exercise": ["running", "Hiit", "weight traning", "Skipping", "rowing"],
    "calaories": [200, 400, 600, 800, 1000],
    "time": [20, 40, 60, 80, 100]

}
pd_data_frame = pd.DataFrame(data)
print(pd_data_frame)

arr1 = ([1, 2, 3, 4])
print("Original array:", arr1)

import numpy as np

arr1 = np.array([1, 2, 3, 4])
print("Original array:", arr1)

a = [True, False, False, True]
b = arr1[a]

print(b)

s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
print(s["a"])


a = np.array([1,2,3])
print(a)
