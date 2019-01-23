from pcb import PCBlock

class Process(object):

	def __init__(self, os, pid, job):
		self.os 		=	os 

		self.pcb 		= 	PCBlock(self, pid, job)