

k = [1, 2, 3, 4, 5, 6, 7, 8, 9]
actual_index = 0

# Recurive approach for binary search.
def binary_search(arr, start, end, element):
    arr = arr[start:end]
    
    if not len(arr):
        return

    mid = (start +  end)/2

    if arr[mid] == element:
        return mid
    elif element < arr[mid]:
        return binary_search(arr, start, mid-1, element)
    else:
        return binary_search(arr, mid+1, end, element)

if __name__=='__main__':
    index = binary_search(k, 0, len(k), 2)
    print(index)

































    #     arr_len = len(arr[start:end])
    # if arr_len == 0:
    #     return 
    # mid = (start +  end)/2
    # if arr[mid] == element:
    #     return mid
    # elif arr[mid] > element:
    #     return binary_search(arr, start, mid, element)
    # elif arr[mid] < element:
    #     return binary_search(arr, mid + 1, end , element)
