def selection_sort(arr):
	for i in range(len(arr)-1):
		small_ele = i

		for j in range(i, len(arr)-1):
			if arr[j] < arr[small_ele] :
				small_ele = j
		arr[small_ele], arr[i] = arr[i], arr[small_ele]




if __name__ == '__main__':
	arr = [32,56,11,40,23,39,67,36,1,22, 41, 15]
	selection_sort(arr)
	print(arr)