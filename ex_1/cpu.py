from yidan_time import YidanTime

class cpu(object):

	def __init__(self):
		self.currentJobTime = 0
		self.job  	= None
		self.clock  = YidanTime(0)
	
	def addJob(self, job, clock):
		if self.job == None:
			self.job = job 
			return None
		else:
			self.job.waitingTime = self.job.waitingTime - (clock - self.clock)
			original_job = self.job
			self.job = job
			self.clock = clock
			return original_job

	def sort(self,lista):

		lista.sort(key = lambda x:(x.currentJob.priority), reverse = False)
