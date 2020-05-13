"""
Given an array A[] and a number x, check for pair in A[] with sum as x
Write a program that, given an array A[] of n numbers and another number x,
determines whether or not there exist two elements in S whose sum is exactly x.

"""

arr = [1, 2, 3, 4, 5, 6, 7, 8]
if __name__ == '__main__':
    k = 7
    myset = set()
    for i in arr:
    	if k-i not in myset:
    	   myset.add(i)
    	else:
    	    print((i, (k-i)))

























	# k = {}
	# sum1 = 7
	# for i in arr:
	# 	if (sum1-i) in k:
	# 		print(sum1-i, i)
	# 		break
	# 	else:
	# 		k[i] = 1



