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

# convert list, tuple  to ndarray
x = [1, 2, 3]
a = np.asarray(x)
print(a)
x = (1, 2, 3)
a = np.asarray(x)
print(a)
'''
========= THIS CODE SEGMENT DOESN'T WORK====
========= NEED DEEP UNDERSTANDING ==========
# convert string or any object with buffer capabilities to array
s = 'Hello World'
a = np.frombuffer(s, dtype='int32')
print(a)

'''
# create list object using range function
list1 = range(5)
print(list1)
it = iter(list1)

# use iterator to create ndarray
a = np.fromiter(it, dtype=float)
print(a)

# start and stop parameters set
#numpy.arange(start, stop, step, dtype)
a = np.arange(10, 20, 2)
print(a)

# linespace function to determine the difference between the elements
# numpy.linspace(start, stop, num, endpoint, retstep, dtype)
a = np.linspace(1, 2, 3, 4, retstep=True)
print(a)

# set base of log space to 2
# numpy.logspace(start, stop, num, endpoint, base, dtype)
a = np.logspace(1, 10, num=10, base=2)
print(a)

a = np.arange(10)
s = slice(2, 7, 2)
print(a[s])
b = a[2:7:2]
print(b)

# slice items starting from index
print(a)
print('Now we will slice the array from the index a[1:]')
print(a[1:])
# selecting data from array based on type
a = np.array([np.nan, 1, 2, np.nan, 3, 4, 5])
print(a)
print(a[~np.isnan(a)])
a = np.array([1, 2+6j, 5, 3.5+5j])
print(a[np.iscomplex(a)])
