def lonelyInteger(list):
	result = 0
	for val in list:
		result ^= val
	return result

arr = [1,2,3,4,3,2,1]
print(lonelyInteger(arr))

arr2 = [0,0,0,1,2,3,4,0,0,1,2,3]
print(lonelyInteger(arr2))

