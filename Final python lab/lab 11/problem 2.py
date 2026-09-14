import numpy as np

arr = np.array([10, 20, 30, 20, 40, 20, 50])
item = 20
n = 3

positions = np.where(arr == item)[0]

if len(positions) >= n:
    print(positions[n - 1])
else:
    print("Not enough repetitions")