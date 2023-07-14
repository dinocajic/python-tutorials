import pandas as pd
import numpy as np

print("Here's a Pandas Example")
df = pd.read_csv('testfile.csv')

print(df.to_string())

print("\nHere's a Numpy Example")
arr = np.array([1, 2, 3, 5, 5, 5, 4])

x = np.where(arr == 5)

print(x)
