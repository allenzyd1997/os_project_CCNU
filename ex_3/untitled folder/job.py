from yidan_time import YidanTime

class Job(object):
	def __init__(self, event_name, happen_time, running_time, priority):
		happen_time 	= YidanTime(happen_time)
		running_time	= YidanTime(running_time)
		priority 		= int(priority)

		assert type(event_name)  	is str,			"job parameter type error!"
		assert type(happen_time) 	is YidanTime,	"job parameter type error!"
		assert type(running_time)	is YidanTime,	"job parameter type error!"
		assert type(priority)  		is int,			"job parameter type error!"

		self.event_name 	= event_name
		self.happen_time 	= happen_time
		self.running_time 	= running_time
		self.priority 		= priority

