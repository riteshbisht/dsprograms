"""
Write a program to print all the LEADERS in the array.
An element is leader if it is greater than all the elements to its right side.
And the rightmost element is always a leader.
For example int the array {16, 17, 4, 3, 5, 2}, leaders are 17, 5 and 2.
Let the input array be arr[] and size of the array be size.
"""

arr = [16, 17, 4, 3, 5, 2]

if __name__ == '__main__':

    max_ele = arr[len(arr)-1] 
    print(max_ele)   
    for i in range(len(arr)-2, 0, -1):
        if(arr[i] > max_ele):
            print(arr[i])
            max_ele = arr[i]