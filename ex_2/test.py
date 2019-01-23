from memory import Memory
from algorithms import algorithm_memory_apply_best_adapt, algorithm_memory_recycle


m1 = Memory(0, 19)
m2 = Memory(21, 28)
m3 = Memory(39, 55)
m4 = Memory(56, 79)
m5 = Memory(88, 99)


mc_1 = Memory(29, 38)
mc_2 = Memory(80, 82)

a_memory_list = [m1, m2, m3, m4, m5]

threshold = 1

def show_list(a_memory_list):
	for a in a_memory_list:
		print(a)
	return 


while(1):
	print("do_memory operation")
	print("1. for applying new memory")
	print("2. for recyling memory")
	print("3. for show the memory list")
	print("input -1 for exit")

	choice = int(input())
	if choice == 1:
		print("input size you wanna apply")
		size = int(input())
		result, lower, upper = algorithm_memory_apply_best_adapt(a_memory_list, size, threshold)
		for seq, i in enumerate(a_memory_list):
			if i.lower_bound == lower:
				a_memory_list[seq] = Memory(upper+1, i.upper_bound)

		if result == True:
			print("Success")
			show_list(a_memory_list)
			print(Memory(lower, upper))
		else:
			print("Fail")
			show_list(a_memory_list)

	elif choice == 2:
		print("input the memory lower address you wanna recycled")
		lower = int(input())
		print("input the memory upper address you wanna recycled")
		upper = int(input())
		algorithm_memory_recycle(a_memory_list, Memory(lower, upper))
		show_list(a_memory_list)

	elif choice == 3:
		show_list(a_memory_list)
	elif choice == -1:
		break
	else:
		print("choice wrong")
		continue
	




# import random


# class a(object):

# 	def __init__(self):
# 		self.events = [10,213,34,231,24]
# 		self.current_event = []
# 	def event_happen(self):
# 		self.events = self.events + self.current_event
# 		self.current_event = []
# 		event_num = random.randint(0, len(self.events))
# 		for i in range(event_num):
# 			self.current_event.append(self.events.pop(random.randint(0, len(self.events) - 1)))

# b = a()

# for i in range(100):

# 	b.event_happen()
# 	print("********************************************************")
# 	print()
# 	print("This is events: ", b.events)
# 	print("This is current_event", b.current_event)
# 	print()













