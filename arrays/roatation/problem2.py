"""
Find the Rotation Count in Rotated Sorted array
Consider an array of distinct numbers sorted in increasing order. The array has been rotated (clockwise) k number of times. Given such an array, find the value of k.

Examples:

Input : arr[] = {15, 18, 2, 3, 6, 12}
Output: 2
Explanation : Initial array must be {2, 3,
6, 12, 15, 18}. We get the given array after 
rotating the initial array twice.

Input : arr[] = {7, 9, 11, 12, 5}
Output: 4

Input: arr[] = {7, 9, 11, 12, 15};
Output: 0

"""

# 1 2 3 4 5 6 => 0

# 3 4 5 6 1 2 => 4

# 3 4 5 6 7 8 1 2 => 5

k =  [3, 4, 5, 6, 7, 1, 2]

def countRotation(arr, low , high):
    if low==high:
        return (low + 1) % len(k)

    mid = (low + high) / 2

    if mid > low and arr[mid] < arr[mid - 1]:
        return mid
    elif mid < high and arr[mid] > arr[mid + 1]:
        return mid + 1
    elif arr[low] < arr[mid]:
        return countRotation(arr, mid + 1, high)
    return countRotation(arr, low, mid - 1)

if __name__ == '__main__':
    rotation = countRotation(k, 0, len(k) - 1)
    print(rotation)