def algorithm_memory_apply_best_adapt(empty_memory_list, apply_memory_size, threshold):
	# This is the algorithm used for helping the os finish the memory allocation task
	# Take the best adapt algorithm, which is, choose the biggest memory block in the list and allocate this bolck
	# return value: 
	# Bool Value, whether operation is successful or not.
	# Lower Bound, lower bound of the new memory 
	# Upper Bound, upper bound of the new memory
	empty_memory_list.sort(key = lambda x: len(x), reverse = True)
	if empty_memory_list == []:
		result = False
		lower_bound, upper_bound = None, None
		
	elif len(empty_memory_list[0])  < apply_memory_size:
		# can not successfully finish the task
		result = False
		lower_bound, upper_bound = None, None
	else:
		# can finish the job
		result = True
		# if the rest place is lesser than or equal to the threshold
		if len(empty_memory_list[0]) - apply_memory_size <= threshold:
			lower_bound = empty_memory_list[0].lower_bound
			upper_bound = empty_memory_list[0].upper_bound
		# if the rest place is not lesser than the threshold
		else:
			lower_bound = empty_memory_list[0].lower_bound
			upper_bound = empty_memory_list[0].lower_bound + apply_memory_size - 1

	return result, lower_bound, upper_bound

def algorithm_memory_recycle(empty_memory_list, recycled_memory):
	# This is the algorithm used for helping the os finish the memeory space recycling task
	# method do not return value, directly modifying the empty_memory_list
	empty_memory_list.sort(key = lambda x:x.upper_bound)

	
	if empty_memory_list == []:
		empty_memory_list.append(recycled_memory)
		return 
	# IF the new block is the most low address block
	if recycled_memory.upper_bound < empty_memory_list[0].lower_bound:
		if recycled_memory.upper_bound == empty_memory_list[0].lower_bound - 1:
			empty_memory_list[0] = empty_memory_list[0] + recycled_memory
			return 
		else:
			empty_memory_list.insert(0, recycled_memory)
			return
	# IF the new block is the highest address block 
	elif recycled_memory.lower_bound > empty_memory_list[-1].upper_bound:
		if recycled_memory.lower_bound == empty_memory_list[-1].upper_bound + 1:
			empty_memory_list[-1] = empty_memory_list[-1] + recycled_memory
		else:
			empty_memory_list.append(recycled_memory)
	else:
		# IF the new block in the middle of block list
		for seq, memory_block in enumerate(empty_memory_list):
			# Found the block should be insert or combine after or with this block, beginning judging
			if memory_block.lower_bound > recycled_memory.lower_bound:
				if memory_block.lower_bound == recycled_memory.upper_bound + 1:
					memory_block = memory_block + recycled_memory
					if empty_memory_list[seq - 1].upper_bound == recycled_memory.lower_bound - 1:
						memory_block = memory_block + empty_memory_list[seq - 1]
						empty_memory_list[seq] = memory_block
						empty_memory_list.remove(empty_memory_list[seq - 1])
						return 
					return
				elif empty_memory_list[seq - 1].upper_bound == recycled_memory.lower_bound - 1:
					empty_memory_list[seq - 1] = recycled_memory + empty_memory_list[seq - 1]
					return
				else:
					empty_memory_list.insert(seq-1, recycled_memory)
					return
	return 