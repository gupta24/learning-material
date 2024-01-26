import numpy as np

# it's using for multiple mathemetical calculation and data processing.

# create the numpy array with list iterable
arr = np.array([2,3,4,5,6,7,8,9], np.int32)
print(arr)
"""
for i in np.arange(0, arr.size):
    print(arr[i])
"""
# for check the type of numpy array
print(arr.dtype)
# for check the size of array
print(arr.size)

# or use set, tuple or dict 

# here tuple is object and given number of item as count, give by-default type int64
arr = np.array((2,3,4,5,6,7,8,9))
print(arr)
print(arr.dtype)
print(arr.size)

# here set is object and count 1
arr = np.array({2,3,4,5,6,7,8,9})
print(arr)
print(arr.dtype)
print(arr.size)

# here dict is object and count 1
arr = np.array({2:1, 3:4, 5:6})
print(arr)
print(arr.dtype)
print(arr.size)

# get the shape of array with dimension and item in each dimension
arr = np.array([[1,2,4,5],[3,4,5,6]])
print("shape of tuple : ", arr.shape)
print("type of arr ", arr.dtype)
# array are indexing
print(arr[0, 3])
# slicing of array
print(arr[:,1])