
"""
Find a peak element
Given an array of integers. Find a peak element in it.
An array element is peak if it is NOT smaller than its neighbors.
For corner elements, we need to consider only one neighbor.
For example, for input array {5, 10, 20, 15}, 20 is the only peak element.

For input array {10, 20, 15, 2, 23, 90, 67}, there are two peak elements: 20 and 90.

Note that we need to return any one peak element.

Following corner cases give better idea about the problem.
1) If input array is sorted in strictly increasing order,
the last element is always a peak element.
For example, 50 is peak element in {10, 20, 30, 40, 50}.
2) If input array is sorted in strictly decreasing order,
the first element is always a peak element. 100 is the peak element in {100, 80, 60, 50, 20}.
3) If all elements of input array are same,
every element is a peak element.

"""

k = [10, 13,  14, 15, 16, 19, 19, 1]

def findPeak(arr, low, high):
	mid = (low + high) / 2
	print(low, mid, high)
	print(arr) 
	if (mid==0 or arr[mid-1] <= arr[mid]) and (mid==len(arr)-1 or arr[mid] >= arr[mid+1]):
		return mid
	elif (arr[mid] > arr[mid-1]):
		return findPeak(arr, mid+1, high)
	else:
		return findPeak(arr , low, mid-1)

if __name__ == '__main__':
	peak = findPeak(k, 0, len(k)-1)
	print(k[peak])