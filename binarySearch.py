def binarySearch(arr, left, right, x):
	if right>==1:
		mid = 1 + (r-1) / 2

		if arr[mid] == x:
			return mid

		elif arr[mid] > x:
			return binarySearch(arr, left, mid-1, x)

		else:
			return binarySearch(arr, mid+1, right, x)