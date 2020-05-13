from binary_search import binary_search


def findPivot(arr, low , high):
    if low == high:
        return low
    mid = (low +  high) / 2

    if mid > low and arr[mid] < arr[mid-1] :
        return mid-1
    elif mid < high and arr[mid] > arr[mid + 1]:
        return mid
    elif arr[low] > arr[mid]:
        return findPivot(arr, low, mid-1)
    return findPivot(arr, mid + 1, high)


def pivotedBinarySearch(arr, element):

    pivot = findPivot(k, 0, len(k)-1)

    if element == k[pivot]:
        return pivot
    if arr[0] < element:
        return binary_search(arr, 0, pivot, element)

    return binary_search(arr, pivot, len(k), element)


if __name__=='__main__':
    k = [3, 4, 5, 1, 2]
    element = 5
    index = pivotedBinarySearch(k, element)
    print(index)