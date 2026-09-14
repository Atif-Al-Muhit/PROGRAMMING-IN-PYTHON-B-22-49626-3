import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([5, 2, 8, 4, 1])

result = np.where(arr1 == arr2)
print(result)