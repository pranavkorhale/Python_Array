"""
To join the array we will use
concatenate() and stack() functions

"""
import numpy as np

#1 using concatenate()

ar1=np.arange(20,40).reshape(2,5,2)
ar2=np.arange(20).reshape(2,5,2)
arr_c1=np.concatenate((ar1,ar2))
print("First array\n",ar1)
print("Second array\n",ar2)
print("-----------------------")
print("Concatenated array is\n",arr_c1)
arr_c2=np.concatenate((ar1,ar2),axis=1)
arr_c3=np.concatenate((ar1,ar2),axis=2)
print("-----------------------")
print("Concatenated array using axis 1\n",arr_c2)
print("-----------------------")
print("Concatenated array using axis 2\n",arr_c3)

#2 stacking
"""
In stacking we concatenate along the new axis rather the same axis.
like ex- we can concatenate the two 1-d array along the 2nd axis that would
         result in putting one over the another ie stacking. 
"""

ar1=np.arange(6).reshape(3,2)
ar2=np.arange(6,12).reshape(3,2)
arr_s1=np.stack((ar1,ar2),axis=1)
print("First array\n",ar1)
print("Second array\n",ar2)
print("-----------------------")
print("stacked array using axis 1 is\n",arr_s1)
arr_s2=np.stack((ar1,ar2),axis=2)
print("stacked array using axis 2 is\n",arr_s2)

# a)hstack()- stack along row

ar1 = np.array([1,2,3,4,5])

ar2 = np.array([6,7,8,9,10])

arr = np.hstack((ar1, ar2))

print("array stacked along the row\n",arr)



# b)vstack()- stack along column

ar1 = np.array([1,2,3,4,5])

ar2 = np.array([6,7,8,9,10])

arr = np.vstack((ar1, ar2))

print("array stacked along the column\n",arr)

# c)dstack()- stack along height

ar1 = np.array([1,2,3,4,5])

ar2 = np.array([6,7,8,9,10])

arr = np.dstack((ar1, ar2))

print("array stacked along the height\n",arr)










