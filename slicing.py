"""
Slicing of array means cutting of the numbers that we don't need.
we can do slicing by passing this[syntax]: variable_of_array[startIndex:ndIndex]
if we want To give step then: variable_of_array[startIndex:ndIndex:step]
Default:
        start=0
        End=length of the string
        step=1

"""

import numpy as np

"""
Slicing in 1-d array

"""
one_darray=np.array([1,2,3,4,5])
print("Array:-",one_darray)
print("Sliced array is:-",one_darray[0:4])

"""
Slicing in 2-d array

"""

two_darray=np.array([[0,2,4,6,8,10],[1,3,5,7,9,11],[12,13,14,15,16,17]])
print("Array:-",two_darray)
print("1st Sliced array is:-",two_darray[0,0:3]) #To slice the 0 position element of 2-d array
print("2nd Sliced array is:-",two_darray[0:3,3]) #From every element return index 3
print("3rd Sliced array is:-",two_darray[0:2,0:4])#TO slice a part from every element(here 0:4 sliced from 2 elements ) 

"""
Slicing in 3-d array

"""
three_darray=np.array([[[0,4,1],[12,16,18],[20,30,40]],[[2,6,8],[14,18,19],[40,50,60]],[[1,5,7],[13,17,18],[60,70,90]]])
print("Array:-",three_darray)
print("1st Sliced array is:-",three_darray[0,1,0:2]) #sliced the 2nd element of 1 position index
print("2nd Sliced array is:-",three_darray[0:3,1]) #From every element return array on 2nd position
print("3rd Sliced array is:-",three_darray[0:3,0:2])#TO slice a part from every element 












