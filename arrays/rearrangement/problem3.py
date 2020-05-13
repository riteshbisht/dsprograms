"""
Positive elements at even and negative at odd positions (Relative order not maintained)
You have been given an array and you have to make a program to convert that
array such that positive elements occur at even numbered places in the array
and negative elements occur at odd numbered places in the array/
We have to do it in place.

There can be unequal number of positive and negative values
and the extra values have to left as it is.

Example

Input : arr[] = {1, -3, 5, 6, -3, 6, 7, -4, 9, 10}
Output : arr[] = {1, -3, 5, -3, 6, 6, 7, -4, 9, 10}

Input : arr[] = {-1, 3, -5, 6, 3, 6, -7, -4, -9, 10}
Output : arr[] = {3, -1, 6, -5, 3, -7, 6, -4, 10, -9}

"""
def rearrange(arr):
    pos = 0
    neg = 1
    arr_len = len(arr)

    while(True):
        while(pos < arr_len and arr[pos] > 0):
            pos += 2
        
        while(neg < arr_len and arr[neg] < 0):
            neg += 2

        if(pos < arr_len and neg < arr_len):
            arr[pos], arr[neg] = arr[neg], arr[pos]
        else:
            break

if __name__ == '__main__':
    arr = [1, -3, 5, 6, -3, 6, 7, -4, 9, 10]
    print("Before:- ", arr)
    rearrange(arr)
    print("After:-", arr)
    
