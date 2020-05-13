"""
Replace every array element by multiplication of previous and next
Given an array of integers, update every element with multiplication of previous and next elements with following exceptions.
a) First element is replaced by multiplication of first and second.
b) Last element is replaced by multiplication of last and second last.

Example:

Input: arr[] = {2, 3, 4, 5, 6}
Output: arr[] = {6, 8, 15, 24, 30}

// We get the above output using following
// arr[] = {2*3, 2*4, 3*5, 4*6, 5*6} 
"""
arr = [2, 3, 4, 5, 6]
if __name__ == '__main__':
    previous = 0
    for index, i in enumerate(arr):
        if index == 0:
            previous = i
            arr[index] = arr[index] * arr[index+1]          
        elif index == len(arr) - 1:
            arr[index] = arr[index] * previous
        else:
            arr[index] = previous * arr[index+1]
            previous = i
    print(arr)