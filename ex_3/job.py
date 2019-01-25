
class Job(object):
	def __init__(self, jobName, size):

		assert type(jobName) is str, "jobName should be String"
		assert type(size) 	 is int, "size should be Integer"

		self.jobName	= jobName
		self.size 		= size
		self.memory 	= None 



	def __str__(self):
		return self.jobName
	
	def __repr__(self):
			return self.jobName