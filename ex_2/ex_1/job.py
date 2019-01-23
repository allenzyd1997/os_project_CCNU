from yidan_time import YidanTime

class Job(object):
	
	def __init__(self, sequence, enterTime, runningTime, priority, waitingTime):
		self.sequence 		= sequence
		self.enterTime 		= YidanTime(enterTime)
		self.runningTime	= YidanTime(runningTime)
		self.priority		= priority
		self.endTime 		= YidanTime(0)
		self.waitingTime	= YidanTime(waitingTime)
		self.inChannelTime  = YidanTime(0)
		self.cyclingTime 	= YidanTime(0)
		self.runnedTime     = YidanTime(0)
		

	def wait(self, clock):
		self.waitingTime 	= self.waitingTime + 1 

	def execute(self, clock):
		self.runnedTime  	= self.runnedTime  +  1
		if self.runningTime  ==  self.runnedTime:
			self.endTime 	= clock
			return True
		else:
			return False

