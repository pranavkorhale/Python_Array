"""
Changing shapes

1)reshape()  -:gives a new shape without changing its data.
2)flat()     -:return the element given in the flat index
3)flatten()  -:return the copied array in 1-d.
4)ravel()    -:returns a contiguous flatten array.
"""
import numpy as np

#1 array_variable.reshape(newshape)
a=np.arange(8)
b=a.reshape(2,2,2)
print("The original array-:",a)
print("Chnaged array-:",b)


#2 array_variable.flat(int)

a=np.arange(8)
b=a.flat[3]
print("The original array-:",a)
print("Element of the flat index is",b)


#3 array_variable.flatten()

a=np.arange(8).reshape(2,2,2)
b=a.flatten()
print("The original array-:",a)
print("Flatten array in 1-d -:",b)


#4
"""
array_variable.ravel(order)
order can be-'F' fortran style
             'K' flatten as elemnets occure in the memory"""

a=np.array([[7,8,9,2,3],[1,5,0,4,6]])
b=a.ravel()
c=a.ravel(order='F')
print("The original array-:",a)
print("Array after ravel -:",b)
print("Array returned in fortran style-:",c)

