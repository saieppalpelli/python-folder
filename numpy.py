import numpy as np

# 1. Creating Arrays
# 1D Array
arr1D = np.array([1, 2, 3, 4, 5])
print("1D Array:")
print(arr1D)

# 2D Array
arr2D = np.array([[1, 2, 3],
                  [4, 5, 6]])
print("\n2D Array:")
print(arr2D)

# 3D Array
arr3D = np.array([[[1, 2, 3],
                   [4, 5, 6]],
                  [[7, 8, 9],      [10, 11, 12]]])
print("\n3D Array:")
print(arr3D)

# 2. Reshaping Arrays
reshaped = arr1D.reshape(5, 1)
print("\nReshaped 1D to 2D (5x1):")
print(reshaped)

# 3. Slicing
# 1D slicing
print("\n1D Slice (index 1 to 3):", arr1D[1:4])

# 2D slicing
print("\n2D Slice (first row):", arr2D[0, :])
print("2D Slice (second column):", arr2D[:, 1])

# 3D slicing
print("\n3D Slice (first 2D block):")
print(arr3D[0])

# 4. Indexing
# 1D indexing
print("\n1D Index [2]:", arr1D[2])

# 2D indexing
print("2D Index [1,2]:", arr2D[1, 2])

# 3D indexing
print("3D Index [1,1,2]:", arr3D[1, 1, 2])