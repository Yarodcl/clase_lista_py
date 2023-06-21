import numpy as np

arr = np.arange(0,11)
print(arr)
arr_copy = arr.copy()

piece_of_arr = arr[0:6]

piece_of_arr = arr[:] = 0

print(piece_of_arr)
print(arr)


print(arr_copy)