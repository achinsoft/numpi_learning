import numpy as np

# creates empty array with dimension. Data is filled as garbage values.
# useful when empty array needs to declare without values
# numpy.empty(shape, dtype = float, order = 'C')
a = np.empty([3, 2], dtype=int)
print(a)

# numpy.zeros(shape, dtype = float, order = 'C') makes empty array but fills it with zero
# Order 'C' for C-style row-major array, 'F' for FORTRAN style column-major array
a = np.zeros([5, 4], dtype=np.int)  # "np.zeros((5, 4), dtype = np.int)" this notation is also legal
print(a)
a = np.zeros((5, 2), dtype=np.int)
print(a)

# more examples for Structure data type
a = np.zeros((2, 2), dtype=[('x', 'i4'), ('y', 'i4')])
print(a)

# To fill with 1s use ones instead of zeros :)
a = np.ones(5)
print(a)
