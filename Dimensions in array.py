import numpy as np   #created alias name for numpy
"""
0-dimension array-:
Every single element in array is of 0-d

"""
a=np.array(42)
print(a,"Dimension is:",a.ndim)

"""
1-d array-:Having 0-d elements 

"""
b=np.array([1,2,3,4,5])
print(b,"Dimension is:",b.ndim)
"""
2-d array-:Having 1-d elements in array 

"""
c=np.array([[0,2,4,6,8,10],[1,3,5,7,9,11],[12,13,14,15,16,17]])
print(c,"Dimension is:",c.ndim)

"""
3-d array-:Having 2-d elements in array 

"""
d=np.array([[[0,4],[12,16],[20,30]],[[2,6],[14,18],[40,50]],[[1,5],[13,17],[60,70]]])
print(d,"Dimension is:",d.ndim)

"""
To create higher dimension array provide the ndmin attribute

"""
e=np.array(([1,2,3,4,5],[6,7,8,9,10]),ndmin=5)
print(e,"Dimension is:",e.ndim)



