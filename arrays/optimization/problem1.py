"""
Largest Sum Contiguous Subarray
Write an efficient program to find the sum of contiguous
subarray within a one-dimensional array of numbers which has the largest sum.

"""

arr = [-2, -3, 4, -1, -2, 1, 5, -3]


#arr= [-1, -2, -1, -4, -5, -1, 1, 1]
def max_contigous_sum(arr):
    max_sum = 0
    max_so_far = 0
    for i in range(len(arr)):
        max_so_far += arr[i]

        if(max_so_far < 0):
            max_so_far = 0

        if(max_sum < max_so_far):
            max_sum = max_so_far

    print(max_sum)

def max_contigous_sum_negative(arr):

    curr_sum = arr[0]
    max_so_far = arr[0]

    for i in range(1, len(arr)):
        if(arr[i] > curr_sum + arr[i]):
            max_sum = arr[i]
        else:
            max_sum = curr_sum + [i]

        if max_sum > max_so_far:
            max_so_far = max_sum

    print(max_so_far)
if __name__ == '__main__':

    #max_contigous_sum(arr)

    max_contigous_sum_negative(arr)
    