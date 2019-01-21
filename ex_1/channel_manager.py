from channel import channel
from cpu 	 import cpu
from utils	 import priority_sort, channel_priority_sort

class channel_manager(object):

	def __init__(self, channel_num):
		self.channel_num 			= channel_num
		self.channels 				= self.build_channels()
		self.cpu 					= cpu()
		self.executing_channels 	= []
		self.empty_channels 		= self.channels

	def build_channels(self):
		channel_list = [] 

		for i in range(self.channel_num):
			channel_list.append(channel())

		return channel_list

	def isChannelEmpty(self, clock):
		"Check whether there is empty channel or not"


		if self.empty_channels == []:
			return False
		else:
			self.empty_channels[0].currentJob = None

			return True

	def addJob(self, job, clock):
		"add a job into a channel"
		if self.empty_channels == []:
			return False 
		else:
			channel = self.empty_channels.pop(0)
			channel.addJob(job, clock)
			self.executing_channels.append(channel)
			return True

	def excuteAllChannels(self, clock):
		"Simulate the executing procedure"

		channel_priority_sort(self.executing_channels)

		job = None

		if self.executing_channels == []:
			return 
		else:
			self.cpu.sort(self.executing_channels)

		result 	=	self.executing_channels[0].execute(clock, cpu)
		
		if result == True:
			job = self.executing_channels[0].summaryCurrentJob(clock)
			self.empty_channels.append(self.executing_channels.pop(0))
			if self.executing_channels != []:
				for channel in self.executing_channels:
					channel.wait(clock)
		else:
			if len(self.executing_channels) > 1 :
				for channel in self.executing_channels[1:]:
					channel.wait(clock)

		return job
	
	def restJob(self):
		return [channel.currentJob for channel in self.executing_channels]
