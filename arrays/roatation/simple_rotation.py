from mytime import calculate_time
import sys

k = list(range(1, 10))

# it takes O(n) time complexity and O(d) space complexity space.
@calculate_time
def simple_rotation_using_temp_array(arr, d):
    len_arr = len(arr)
    d = d % len_arr
    temp = []
    for index, i in enumerate(arr):
        temp.append(i)
        if not (index + d) >= len_arr:
            arr[index] = arr[(index+d)]
        else:
            arr[index] = temp[(index+d)%len_arr]


# it takes O(n*d) time complexity
@calculate_time
def rotation_using_shifing_d_times(arr, d):
    len_arr = len(arr)
    d = d % len_arr
    for index in range(d):
        temp = arr[0]
        for i in range(len_arr - 1):
            arr[i] = arr[i + 1]
        arr[i + 1] = temp

# block swap algorith, time complexity O(n) 
@calculate_time
def iterative_block_swap_algorithm(arr, d):

    def swap(arr, start, end, d):
        for i in range(d):
            temp = arr[start + i]
            arr[start + i] = arr[end + i]
            arr[end + i] = temp

    n = len(arr)
    if d == n or d == 0:
        return
    i = d
    j = n - d
    while(i != j):
        if(i<j):
            swap(arr, d - i, d + j - i, i)
            j -= i
        else:
            swap(arr, d-i, d, j)
            i -= j

    swap(arr, d-i, d, i)
    print(arr)


def reverse_algorithm(arr, d):
    arr_len = len(arr)
    d = d % arr_len
    def swap(arr, start, end):
        while(start < end):
            arr[start], arr[end] = arr[end], arr[start]
            start += 1; end -= 1;
    swap(arr, 0, d-1)
    swap(arr, d, arr_len-1)
    swap(arr, 0, arr_len-1)
    print(arr)


if __name__=='__main__':
    argv = sys.argv[1] if len(sys.argv) > 1 else ''
    k = input()
    print(k)
    if argv == '1':
        simple_rotation_using_temp_array(range(4), 3)
    elif argv == '2':
        rotation_using_shifing_d_times(k, 2)
    elif argv == '3':
        iterative_block_swap_algorithm(k, 3)
    elif argv == '4':
        reverse_algorithm(k, 5)
    else:
        print("plead provide  either 1 or 2")


