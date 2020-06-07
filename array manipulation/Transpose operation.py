"""
Transpose Operation

1)transpose()  -:permutates the dimensions of an array.
2)ndarray.T    -:It is same as self.transpose().
3)rollaxis()   -:Specified axis will be rolled backward.
4)swapaxis()   -:will swap(interchange) the two specified axis

Do run few times by changing the values to understand.
"""
import numpy as np

#1 ndarray.transpose(axes) by default it reverses the dimensions
a=np.arange(12).reshape(3,4)
b=a.transpose()
print("original array\n",a)
print("transposed array\n",b)


#2 ndarray.T
a=np.arange(20,32).reshape(3,4)
b=a.T
print("original array\n",a)
print("transposed array\n",b)

#3 numpy.rollaxis(array,axis)
"""
   for exaple if 3d array(2,3,4) is there then 2= axis0(actual array)
                                               3= axis1
                                               4= axis2
"""
a=np.arange(8).reshape(2,2,2)
b=np.rollaxis(a,1)
print("original array\n",a)
print("array rolled around the specified axis\n",b)

#4 numpy.swapaxes(arr,axis1,axis2)

a=np.arange(8).reshape(2,2,2)
b=np.rollaxis(a,2,0)
print("original array\n",a)
print("array after swping axeses\n",b)

