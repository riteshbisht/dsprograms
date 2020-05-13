"""
An array contains both positive and negative numbers in random order.
Rearrange the array elements so that positive and negative numbers are placed
alternatively.
Number of positive and negative numbers need not be equal.
If there are more positive numbers they appear at the end of the array.
If there are more negative numbers, they too appear in the end of the array.

For example, if the input array is [-1, 2, -3, 4, 5, 6, -7, 8, 9],
then the output should be [9, -7, 8, -3, 5, -1, 2, 4, 6]

Note: The partition process changes relative order of elements. I.e
the order of the appearance of elements is not maintained with this approach.
See this for maintaining order of appearance of elements in this problem.
"""

# first partion into left to negative right to positive

arr =  [-1, 2, -3, 4, 5, 6, -7, 8, 9] 

if __name__ == '__main__':
    count = -1
    for index in range(len(arr)):
        if (arr[index] < 0):
            count = count + 1
            arr[index], arr[count] = arr[count], arr[index]

    pos = count + 1
    neg = 0

    while(pos < len(arr) and neg < pos and arr[neg] < 0):
        arr[pos], arr[neg] = arr[neg], arr[pos]
        pos += 1
        neg += 2
    print(arr)

