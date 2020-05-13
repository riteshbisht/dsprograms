"""
Segregate even and odd numbers | Set 3
Given an array of integers, segregate even and odd numbers in the array.
All the even numbers should be present first, and then the odd numbers.

Examples:

Input : 1 9 5 3 2 6 7 11
Output : 2 6 5 3 1 9 7 11

Input : 1 3 2 4 7 6 9 10
Output : 2 4 6 10 7 1 9 3
"""
arr = [1, 3, 7, 4, 6, 8]

if __name__ == "__main__":
    odd = -1
    even = 0
    for index, i in enumerate(arr):
        if i % 2 == 0:
            odd = odd + 1
            arr[odd], arr[index] = arr[index], arr[odd]
    print(arr)
