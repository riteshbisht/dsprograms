"""
Given an array that is sorted and then rotated around an unknown point.
Find if the array has a pair with a given sum x.
It may be assumed that all elements in the array are distinct.

Input: arr[] = {11, 15, 6, 8, 9, 10}, x = 16
Output: true
There is a pair (6, 10) with sum 16

Input: arr[] = {11, 15, 26, 38, 9, 10}, x = 35
Output: true
There is a pair (26, 9) with sum 35

Input: arr[] = {11, 15, 26, 38, 9, 10}, x = 45
Output: false
There is no pair with sum 45.
"""

k = [1, 2, 3, 4, 5]

def findPivot(arr, low , high):
    if high < low: return -1

    if low == high: return low

    mid = (low + high) / 2

    if mid > low and arr[mid] < arr[mid - 1]:
        return mid - 1
    elif mid < high and arr[mid] > arr[mid + 1]:
        return mid
    elif arr[low] > arr[mid]:
        return findPivot(arr, low, mid - 1)
    return findPivot(arr, mid + 1, high)

if __name__=='__main__':
    len_arr = len(k)
    arr = k
    pivot = findPivot(k, 0, len_arr-1)
    sum1 = 10
    lowest = (pivot + 1) % len_arr
    highest = pivot
    while(highest!=lowest):
        if (arr[highest] + arr[lowest]) == sum1:
            print(lowest, highest)
            break;
        elif ( arr[highest] + arr[lowest]) > sum1:
            highest = (len_arr + highest - 1) % n

        elif ( arr[highest] + arr[lowest] ) < sum1:
            lowest = (lowest + 1) % len_arr
