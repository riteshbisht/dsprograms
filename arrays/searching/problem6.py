"""
Find a Fixed Point (Value equal to index) in a given array
Given an array of n distinct integers sorted in ascending order,
write a function that returns a Fixed Point in the array,
if there is any Fixed Point present in array, else returns -1.

Fixed Point in an array is an index i such that arr[i] is equal to i
 Note that integers in array can be negative.

Examples:

  Input: arr[] = {-10, -5, 0, 3, 7}
  Output: 3  // arr[3] == 3 

  Input: arr[] = {0, 2, 5, 8, 17}
  Output: 0  // arr[0] == 0 


  Input: arr[] = {-10, -5, 3, 4, 7, 9}
  Output: -1  // No Fixed Point
"""

def findFixedPoint(arr, low, high):
	mid = (low + high) / 2
	print(low, mid, high)

	if mid == arr[mid]:
		return mid
	if low == high:
		return
	elif mid > arr[mid]:
		return findFixedPoint(arr, mid + 1, high)
	else:
		return findFixedPoint(arr, low, mid - 1)

arr = [0, 2, 3, 8, 7, 9, 11]

if __name__ == '__main__':
	point = findFixedPoint(arr, 0, len(arr))
	if point is None:
		print(-1)
	else:
	    print(point)

    