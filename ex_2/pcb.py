from psw 	 import	PSW
from yidan_time import YidanTime

class PCBlock(object):

	def __init__(self, process, pid, job):
		self.pid 			= pid
		#self.psw 			= PSW("CREAT")

		self.job 			= job
		# The Process' priority comparing with other processes
		self.priority 		= job.priority
		# record the different information, such as clock
		# Time Period Allocate to the process
		self.time_period  	= YidanTime(0)
		# The Event that This process is waiting for
		self.event 			= job.event_name
		# print("---------------")
		# print(type(process))
		# print(type(process.os))

		self.lower_bound, self.upper_bound = process.os.apply_space()
		if self.lower_bound == None:
			print("Applying Space Fail")
			self.os.HangUp(self)

		self.happen_time 	= job.happen_time
		self.running_time	= job.running_time
		