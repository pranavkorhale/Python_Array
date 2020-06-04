"""
Copy() and view()

view()-^This array is just the projection of the original array.
       ^If changes made to the original array the view array will also chnage and vice versa.
       ^So bascially view array points to the original array.
       
copy()-^This array is the new array and owns the data to itself means it does not point to the original array.
       ^If changes made to the orignal array then the copy array will not change.
       

"""
import numpy as np


arr=np.array([10,20,30,40,50])
arr_copy=arr.copy()
print("old arrray-:",arr,"\n copied array-:",arr_copy)
arr[1]=200
print("After changing the original array")
print(arr,arr_copy)


arr1=np.array([100,200,300,400,500])
arr1_view=arr1.view()
print("old arrray-:",arr,"\n view array-:",arr_copy)
arr1[1]=2000
print("After changing the original array")
print(arr1,arr1_view)

"""
To check array owns the data or not (base) is used
^It returns none when array owns it.
^ It the array if does not owns it.

"""


print(arr_copy.base)
print(arr1_view.base)
