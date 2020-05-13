
def partition(arr, start ,end):
    """Using first element as Pivot."""
    i = start + 1
    piv = arr[start]

    for j in range(start + 1, end):
        if arr[j] < piv:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[start], arr[i-1] = arr[i-1], arr[start]           
    return i-1


def partition2(arr, start, end):
    """  Using last element as Pivot.   """
    piv = arr[end-1]
    i = start
    for j in range(start, end):
        if arr[j] < piv:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[end-1] = arr[end-1], arr[i]
    return i


def quick_sort(arr, low, high):
    if low < high:
        pi = partition2(arr, low, high)

        quick_sort(arr, low, pi)
        quick_sort(arr, pi+1, high)

if __name__ == '__main__':
    arr=  [80, 30, 90, 40, 50, 70]
    quick_sort(arr, 0, len(arr))
    print(arr)