"""
Reorder an array according to given indexes
Given two integer arrays of same size, "arr[]" and "index[]",
reorder elements in "arr[]" according to given index array.
It is not allowed to given array arr's length.

Example:

Input:  arr[]   = [10, 11, 12];
        index[] = [1, 0, 2];
Output: arr[]   = [11, 10, 12]
        index[] = [0,  1,  2] 

Input:  arr[]   = [50, 40, 70, 60, 90]
        index[] = [3,  0,  4,  1,  2]
Output: arr[]   = [40, 60, 90, 50, 70]
        index[] = [0,  1,  2,  3,   4] 

"""


arr = [50, 40, 70, 60, 90]
index  = [3,  0,  4,  1,  2]
if __name__ == '__main__':
    for i in range(len(index)):

    	while(i!=index[i]):
    		oldindex = index[index[i]]
    		oldelement = arr[index[i]]

    		index[index[i]] = index[i]
    		arr[index[i]] = arr[i]

    		index[i] = oldindex
    		arr[i] = oldelement
    print(arr)
    print(index)

