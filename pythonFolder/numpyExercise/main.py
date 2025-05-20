import numpy as np


arr = np.array([1, 2, 3, 4, 5])

print("a: ", arr)
print("type of a: ", type(arr))

b = [1, 2, 3, 4, 5]

print("and for normal arrays, b: ", b)
print("type of b: ", type(b))

print("Shape:", arr.shape)      # Output: (4,)
print("Dimensions:", arr.ndim)  # Output: 1
print("Size:", arr.size)        # Output: 4
print("Data type:", arr.dtype)  # Output: int64 (or another integer type depending on your system)
print("Item size:", arr.itemsize)  # Output: 8 (for 64-bit integers)
