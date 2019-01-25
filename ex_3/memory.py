class Memory(object):

	def __init__(self, lower_bound, upper_bound):
		assert upper_bound >= lower_bound, "Memory initial error"
		self.lower_bound 	= lower_bound
		self.upper_bound 	= upper_bound
		


	def __len__(self):
		return self.upper_bound - self.lower_bound + 1 

	def __add__(self, obj):
		assert type(obj) is Memory, "object should be a memory"

		if self.lower_bound == -1 and self.upper_bound == -1:
			return obj 
		elif obj.lower_bound == -1 and obj.upper_bound == -1:
			return self
		if obj.upper_bound == self.lower_bound - 1:
			upper_bound = self.upper_bound
			lower_bound = obj.lower_bound
		elif obj.lower_bound == self.upper_bound + 1:
			upper_bound = obj.upper_bound
			lower_bound = self.lower_bound
		else:
			print("--------------- ADD ERROR ---------------")
			raise Exception

		return Memory(lower_bound = lower_bound, upper_bound = upper_bound)

	def __sub__(self, obj):
		assert type(obj) is Memory, "object should be a memory"

		assert (obj.upper_bound <= self.upper_bound) and (obj.lower_bound == self.lower_bound), "SUB error"

		if obj.upper_bound == self.upper_bound:
			return Memory(-1,-1)
		else:
			return Memory(obj.upper_bound + 1, self.upper_bound)


	def __str__(self):
		return ("{:>3} ---> {:>3}".format(str(self.lower_bound), str(self.upper_bound)) )

	def __eq__(self, obj):
		assert type(obj) is Memory, "OBJECT MUST BE MEMORY"
		if self.lower_bound == obj.lower_bound and self.upper_bound == obj.upper_bound:
			return True
		else:
			return False
