"""
There are some extra data type in NumPy
and here we refer to the data types with one character like i for integer

Here is the list for it-:
'i'-integer
'u'-unsigned integer 
'f'-float
'c'-complex float
'S','a'-string
'U'-unicode string
'b'-boolean
'm'-timedelta
'M'-dateTime
'O'-object
'V'-(void)

"""

import numpy as np

"""
To check the data type of array


"""
arr=np.array([1,2,3,4,5,6])
print("Data type is-:",arr.dtype,arr)

"""
Creating array with predefined data type

"""
arr1=np.array([1,2,3,4,5],dtype='i')
print(arr1)

"""
Converting data type to existing data type
astype()-:It creates the copy of the existing data types and let us  specify the new data type
syntan-:array_variable.astype('new_parameter')
"""
arr=np.array([1,2,3,4,5])
new_arr=arr.astype('a')
print(arr)
print(new_arr)
