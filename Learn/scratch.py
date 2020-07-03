import numpy as np

np_array = np.array([1, 2, 3, 4, 5, 6])

np_2D_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

reshape_np_array = np_array.reshape(-1, 2)
reshape_np_2D_array = np_2D_array.reshape(-1, 1)


print(reshape_np_array)
print(reshape_np_2D_array)
print(np.arange(2, 12, 4))
print(np.linspace(0, 20, num=5, dtype=np.int64))
