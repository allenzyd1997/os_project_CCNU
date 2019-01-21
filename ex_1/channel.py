class channel(object):

	def __init__(self):
		self.empty = True
		self.currentJobTime = 0
		self.currentJob = None
	
	def addJob(self, job, clock):
		self.currentJob = job
		self.currentJobTime = clock
		self.currentJob.inChannelTime = clock

	def wait(self, clock):
		self.currentJob.wait(clock)

	def execute(self, clock, cpu):
		result = self.currentJob.execute(clock)
		return result

	def summaryCurrentJob(self, clock):
		self.endTime 				=	 clock
		self.currentJob.cyclingTime =  self.currentJob.endTime - self.currentJob.enterTime
		return self.currentJob