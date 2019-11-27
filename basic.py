import numpy as np

# numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)

# single dimension array
print("single dimension array")
a = np.array([1, 2, 3])
print(a)

# more than one dimensions if same elements are there
print("multi dimension array")
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)

# if elements in dimensions are not same it will convert to list
print("multi dimension array with different sizes")
a = np.array([[1, 2, 3], [4, 5]])
print(a)

# more than one dimensions if same elements are there complex
print("multi dimension array complex")
a = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(a[1][1][2])  # prints the last digit

# minimum dimensions
a = np.array([1, 2, 3, 4, 5], ndmin=4)
print(a)

# dtype parameter
a = np.array([1, 2, 3], dtype=complex)
print(a)

# structure data type in array
student = np.dtype([('name', 'S20'), ('age', 'i1'), ('marks', 'f4')])
a = np.array([('abc', 21, 50), ('xyz', 18, 75)], dtype=student)
print(a['name'])

# get the size information of the array
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.shape)
a.shape = (3, 2)  # this changes the shape on the same object
print(a)
a = a.reshape(1, 6)  # this needs to be saved on another object or assign to itself to reflect
print(a.shape)
print(a)

# create an array of sequential numbers
a = np.arange(24)
print(a)
print(a.ndim)  # returns the dimension
a = a.reshape(2, 12)  # reshape to check the new dimension
print(a.ndim)

# use itemsize to get the size of the element in array
a = np.array([1, 2, 3, 4, 5], dtype=np.int32)  # try using int8, int 16 or float32 and see the value
print(a.itemsize)

# flags are the options that can be set and have different controls on the array
print(a.flags)  # ====HOW TO SET THESE PARAMETERS NEED TO EXPLORE===
