def test_string(myStr):
	myStr += '99'
	print("in function:" + myStr)

def test_string2(myStr):
	myStr = 'newString'
	print(myStr)

def test_list(myList):
	myList.append(99)

def test_list2(myList):
	myList[0] = 99

def test_list3(myList):
	myList = [99,99,99,99]

#passing a copy of a list
def test_list4(myList):
	myList += [5]
	print("in function:")
	print(myList)

def test_int(myInt):
	myInt += 99
	print("in function:" + str(myInt))


def test_int2(myInt):
	myInt = 99
	print("in function:" + str(myInt))


testString = 'abcdef'
print(testString)
test_string(testString)
print(testString)
print('--------------------')

testString2 = 'abcdef'
print(testString2)
test_string2(testString2)
print(testString2)
print('--------------------')

testList = [1,2,3,4,5,6]
print(testList)
test_list(testList)
print(testList)
print('--------------------')

testList2 = [8,9,10,11,12,13]
print(testList2)
test_list2(testList2)
print(testList2)
print('--------------------')

testList3 = [8,9,10,11,12,13]
print(testList3)
test_list3(testList3)
print(testList3)
print('--------------------')


testList4 = [1,2,3,4,5,6]
print(testList4)
test_list4(testList4[:])
print(testList4)
print('--------------------')

testInt = 0
print(testInt)
test_int(testInt)
print(testInt)
print('--------------------')

testInt2 = 0
print(testInt2)
test_int(testInt2)
print(testInt2)
print('--------------------')

