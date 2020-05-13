def insertion_sort(arr):
    
    for i in range(1, len(arr)-1):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j = j -1

        arr[j+1] = key

    print(arr)

if __name__ == '__main__':
    arr = [21, 2, 43,3, 44, 5, 61, 6, 0, 2]
    insertion_sort(arr)