import numpy as np

# The term broadcasting refers to the ability of NumPy to treat arrays of different shapes
# during arithmetic operations. Arithmetic operations on arrays are usually done on corresponding
# elements. If two arrays are of exactly the same shape, then these operations are smoothly performed.
a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])
c = a * b
print(c)

a = np.array([[0.0, 0.0, 0.0], [10.0, 10.0, 10.0], [20.0, 20.0, 20.0], [30.0, 30.0, 30.0]])
b = np.array([1.0, 2.0, 3.0])

print('First array:')
print(a)
print('Second array:')
print(b)
print('First Array + Second Array')
print(a + b)

# complex exmaple
a = np.arange(0, 60, 5)
a = a.reshape(3, 4)
print('Original array is:')
print(a)
print('Transpose of the original array is:')
b = a.T
print(b)

print("Simple copy")
c = b.copy()
print(c)
print('Sorted in C-style order:')
c = b.copy(order='C')
print(c)
for x in np.nditer(c):
    print(x, end=' ')
print('\nSorted in F-style order:')
c = b.copy(order='F')
print(c)
for x in np.nditer(c):
    print(x, end=' ')
