def bubble_sort(arr):
	
	for i in range(len(arr)-1):
	    for j in range(len(arr)-1-i):
	    	if arr[j] > arr[j+1]:
	    		arr[j], arr[j+1] = arr[j+1], arr[j]
	print(arr)


if __name__ == '__main__':
	arr = [17,41,8,3,7,4,1,10]
	bubble_sort(arr)
