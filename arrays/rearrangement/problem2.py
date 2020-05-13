"""
Write a program to reverse an array or string
Given an array (or string), the task is to reverse the array/string.

Examples :

Input  : arr[] = {1, 2, 3}
Output : arr[] = {3, 2, 1}

Input :  arr[] = {4, 5, 1, 2}
Output : arr[] = {2, 1, 5, 4}
"""

def reverse_whole_string(k):
    start = 0
    end = len(k)
    new_tring = ""
    final, first, second = '', '', ''
    while(start < end):
        first += k[end-1]
        second = k[start] + second
        end -= 1
        start = start + 1
    final = first + second
    print(final)

def reverse_string_but_keep_words_intact(k):
    new_string =''
    temp =''

    # get string till sencond last word.
    for index, i in enumerate(k):
        temp += i
        if i == ' ':
            new_string = temp + new_string
            temp =''

    #for final word
    new_string = temp + ' ' + new_string          
    print(new_string)


if __name__ == '__main__':
    k = "this is ritesh bisht"

    reverse_whole_string(k)