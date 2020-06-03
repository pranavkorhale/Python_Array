import numpy as np
"""
Array indexing:-Means to access the specific element by giving the index to it
By default ini arrays index starts from 0 and ends at length-1

"""
"""
Indexing in 1-d array

"""
one_darray=np.array([1,2,3,4,5])
print("Array-:",one_darray)
print("Fisrt element-:",one_darray[0],"\nFourth element:-",one_darray[3])
print("-----------------------------------")
"""
Indexing in 2-d array

"""
two_darray=np.array([[0,2,4,6,8,10],[1,3,5,7,9,11],[12,13,14,15,16,17]])
print("Array:-",two_darray)
print("Last element of the 2-d array is-:",two_darray[2])
print("3rd element of middle array element",two_darray[1,2])
print("-----------------------------------")

"""
Indexing in 3-d array

"""
three_darray=np.array([[[0,4],[12,16],[20,30]],[[2,6],[14,18],[40,50]],[[1,5],[13,17],[60,70]]])
print("Array:-",three_darray)
print("Middle element of the 3-d array is(ie 2-d array)-:",three_darray[len(three_darray)//2])
print("last element of last array in 2 position of 3-d array(ie single element)",three_darray[1,2,1])
print("-----------------------------------")

"""

Indexing in higher dimension array
nth dimension will have its innermost dimension at the n-1 index
Ex- to access 5th dimension array([[[[[1 2 3 4 5],[6 7 8 9 10]]]]]) element we will give[0,0,0,0]ie[1 2 3 4 5]
    to access the element of last that is 5th -d array [0,0,0,1,4] wil, give 10

"""
higher_darray=np.array(([1,2,3,4,5],[6,7,8,9,10]),ndmin=8)
print("Last element of the 5th dimesion array element(ie 0-d element)",higher_darray[0,0,0,0,0,0,1,3])

"""
Negative indexing-:It means to start with the end of the array and the last element of the array is -1

"""
print("3rd elemnt of 1-d array by negative indexing",one_darray[-3])
print("Middle element of last array in 2-d is",two_darray[-1,-4])























