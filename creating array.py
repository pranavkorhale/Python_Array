import numpy as np

"""
ndarray can be created by low-level ndarray constructor or by array creation routines
They tale three parameters-:
1)shape-:It could be list of int or any other data type or tuple.
2)dtype-:IT is the desired output data type.
3)order-:'F' is for FORTRAN style column-major
         'C' is for C-style row-major

"""

#1)Most basic creation 
"""
creating the array from the list

"""
Array1=np.array([1,2,3,4,5,6])

"""
creating the array from the tuple

"""
Array2=np.array((10,11,12,13,14,15))

print(Array1)
print(Array2)

"""
To check whether array is created or list

"""
print("Type of data of array1",type(Array1))
print("Type of data array2",type(Array2))


#2)numpy.empty
"""
Creates an uninitialized array of specified data type 

"""
x=np.empty([3,2],dtype=float,order='c')
print(x)

#3)numpy.zeros
"""
Initialises the empty array

"""
y=np.zeros((2,5),dtype=int)
print(y)

#4)numpy.ones
"""
Initialises the array with ones

"""

z=np.ones((10,3),dtype=int)
print(z)


#5)numpy.asarray

"""
Converts the python sequence to the array.
numpy.asarray(a,dtype,order)
a-Data in and form of list or tuples

"""
li=[1,2,3,4,5,6,7,8,9,10]
ar=np.asarray(li)
ar1=np.asarray(li,dtype=float)
print(ar,'\n',ar1)

#6)numpy.fromiter
"""
Creates an ndarray from any iterable object.
numpy.fromiter(i,dtype,count)
i-:is any iterable object
"""
it=[i for i in range(0,15)] 
auto= np.fromiter(it, dtype = int) 
auto1= np.fromiter(it, dtype = float,count=8) 
print(auto,'\n',auto1)



