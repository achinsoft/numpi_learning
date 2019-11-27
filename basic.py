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
