"""
Find all triplets with zero sum
Given an array of distinct elements.
The task is to find triplets in array whose sum is zero.

Examples :

Input : arr[] = {0, 1, 2, -3, -1}
Output : 0 1 -1
         2 -3 1

Input : arr[] = {1, -2, 1, 0, 5}
Output : 1 -2  1
"""

arr =  [0, -1, 2, -3, 1]

if __name__ == '__main__':
    for i in range(len(arr)):
    	hashmap = set()
    	for j in range(i+1, len(arr)):
    		# adding negative assuming subtracting from zero
    	    first_sum = -(arr[i] + arr[j]) 
    	    if arr[j] in hashmap:
    	    	print(arr[i] , arr[j], first_sum)
    	    else:
    	    	hashmap.add(first_sum)
    		