"""
Given an array of integers of size n. Assume '0' as invalid number and all
other as valid number.

Convert the array in such a way that if next number is a valid number
and same as current number, double its value and replace the next number with 0.
After the modification, rearrange the array such that all 0's are shifted to the end.

Examples:

Input : arr[] = {2, 2, 0, 4, 0, 8}
Output : 4 4 8 0 0 0

Input : arr[] = {0, 2, 2, 2, 0, 6, 6, 0, 0, 8}
Output :  4 2 12 8 0 0 0 0 0 0
"""

def swap(arr, index1, index2):
    arr[index1], arr[index2] = arr[index1], arr[index1]

arr = [0, 5, 5, 2, 2, 0, 4, 0, 8]

if __name__ == '__main__':
    count = 0
    for index in range(len(arr)):
        if(index != len(arr)-1 and arr[index] == arr[index+1] and arr[index] !=0):
            arr[index] = arr[index]  * 2
            arr[index+1] = 0
            # swap
        if arr[index] != 0:
            swap(arr, count, index)
            count = count + 1
    print(arr)