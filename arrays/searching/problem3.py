"""
Find a triplet that sum to a given value
Given an array and a value, find if there is a triplet
in array whose sum is equal to the given value.
If there is such a triplet present in array,
then print the triplet and return true. Else return false.
For example, if the given array is {12, 3, 4, 1, 6, 9} and given sum is 24,
then there is a triplet (12, 3 and 9) present in array whose sum is 24.

"""

arr = [12, 3, 4, 1, 6, 9]
sum1 = 24
for i in range(len(arr)):
    flag = False
    hashmap = set()
    curr_sum = sum1 - arr[i]
    for j in range(i+1, len(arr)):
        x = curr_sum - arr[j]
        if x  in hashmap:
            print(arr[i] , curr_sum - arr[j], arr[j])
            flag = True
            break;
        else:
            hashmap.add(arr[j])
    if flag:
        break