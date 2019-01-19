def minimum_total_waiting_time(service_times):
	service_times.sort()
	total_waiting_time = 0
	for i, service_time in enumerate(service_times):
		num_remaining_queries = len(service_times) - (i+1)
		print(num_remaining_queries)
		print(service_time)
		total_waiting_time += service_time * num_remaining_queries
	return total_waiting_time

print(minimum_total_waiting_time([3,2,1,0]))
print(minimum_total_waiting_time([3,2,1,5]))