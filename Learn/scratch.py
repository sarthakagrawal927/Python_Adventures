import numpy as np
import matplotlib.pyplot as plt
np_array = np.array([1, 2, 3, 4, 5, 6])

personal_github_token = "570c93e665e2c2eb52efb16ec032ec11dc212d02"

np_2D_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

reshape_np_array = np_array.reshape(-1, 2)
reshape_np_2D_array = np_2D_array.reshape(-1, 1)

greater_than5 = np_2D_array > 5
print(np_2D_array[greater_than5])
print(reshape_np_array.ndim)
print(reshape_np_2D_array.ndim)
print(np.arange(2, 12, 4))
print(np.linspace(0, 20, num=5, dtype=np.int64))

plt.plot(greater_than5)
plt.show()
