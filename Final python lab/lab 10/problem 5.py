import numpy as np

arr = np.array([-5, 10, -2, 8, -1, 20])
arr[arr < 0] = 0
print(arr)