def number_of_ways(n,m):
	def compute_number_of_ways_to_xy(x, y):
		if x == y == 0:
			return 1

		if number_of_ways[x][y] == 0:
			print(x)
			print(y)
			print("________________________________")
			ways_top = 0 if x == 0 else compute_number_of_ways_to_xy(x-1, y) #go up a space
			ways_left = 0 if y == 0 else compute_number_of_ways_to_xy(x, y-1) #go down a space
			print("ways_top" + str(ways_top))
			print("ways_left" + str(ways_left))
			number_of_ways[x][y] = ways_top + ways_left
			return number_of_ways[x][y]

	number_of_ways = [[0] * m for _ in range(n)]
	return compute_number_of_ways_to_xy(n-1, m-1)







print(number_of_ways(5,5))