import os
import operator
import random

from yidan_time import YidanTime
from memory import Memory
from event 	import Event
from algorithms import algorithm_memory_apply_best_adapt, algorithm_memory_recycle
from job import Job 
from process import Process 
from utils 	import delete_a_record


class System_2(object):

	def __init__(self, memory_size = 1024 * 8):

		# ************************************************************* 
		# Memory Control Part
		# Initialize the memory of the System
		# Partner System for memory managing
		self.empty_memory 			= [Memory(lower_bound = 0, upper_bound = memory_size - 1)]
		self.used_memory 			= []
		self.space_enough  			= True

		self.threshold  			= 16
		# Arranging a max size of the pcb, imitating the real os
		self.pcb_max_size 			= 128

		# ************************************************************* 
		# The ID of the process allocated for the process
		self.pid 					= 0

		# ************************************************************* 
		# ALGORITHM AREA
		self.apply_memory_algorithm = algorithm_memory_apply_best_adapt
		self.recycle_memory_algo   	= algorithm_memory_recycle
		
		# *************************************************************
		# EVENT CONTROL AREA
		self.clock 					= YidanTime(0)
		self.time_period 			= YidanTime(0)

		self.events 				= [ 
										Event(name = "event1", semaphore = 2),
										Event(name = "event2", semaphore = 1),
										Event(name = "event3", semaphore = 2),
										Event(name = "event4", semaphore = 1),
										Event(name = "event5", semaphore = 2)
										]
		self.current_event 			= []

		self.event_sustain 			= YidanTime(0)

		self.menu_show 				= True



		# ************************************************************* 
		# LIST MANAGE PART 

		self.blocked_list			= {}
		for event in self.events:
			self.blocked_list[event.name] = []

		self.ready_list 			= {}
		for event in self.events:
			self.ready_list[event.name] = []

		self.running_process 		= None

		# ************************************************************* 

	def event_happen(self):

		self.events = self.events + self.current_event
		self.current_event = []
		event_num = random.randint(0, len(self.events))
		for i in range(event_num):
			self.current_event.append(self.events.pop(random.randint(0, len(self.events) - 1)))
		self.event_sustain = YidanTime(random.randint(1, 5))




	def menu(self):
		"Show the menu for helping do the choice"
		while(1):
			print("**************************************************")
			print("{:>50}".format("MENU"))
			print("1. Create A Process with Random Size")
			print("2. Repeal A Process in Current List")
			print("3. Set the Current Job Time Up")
			print("4. Set the Process Hang up")
			print("5. Activate a Process")
			print("6. close menu")
			print("input -1 for exit menu")


			choice = int(input())
			if choice == -1:
				break

			if choice == 1 :
				choice_opration = self.create_process(self.ask_job_info())
			elif choice == 2 :
				print("Please Input the PID ")
				pid = int(input())
				choice_opration = self.repeal_process(pid)
				if choice_opration == True:
					print("Have Already Repealed The Process")
				else:
					print("PID WRONG")

			elif choice == 3:
				choice_opration = self.timeUp_process()
			elif choice == 4:
				print("Please Input the PID ")
				mark 	= False
				pid 	= int(input())

				for i in self.blocked_list:
					in_list = self.blocked_list[i]
					for j in in_list:
						if j.pcb.pid == pid:
							mark = True
							print(str(j), type(j))
							choice_opration = self.suspend_process(j)
				if mark == True:
					print("Successfully Suspend")
				else:
					print("PID WRONG")
			elif choice == 5:
				print("Please Input a PID FOR AWAKING")
				pid = int(input())
				result = self.awake_process(pid)
				if result:
					print("Successfully Awake")
				else:
					print("PID WRONG")
			elif choice == 6:
				self.menu_show = False
				break
			self.show_list()
		return 


	def show_list(self):
		print("{:>50}".format("Ready List"))
		for i in self.ready_list:
			print("{} --> {}".format(i, [ process.pcb.pid for process in self.ready_list[i]]))

		print("{:>50}".format("Blocked List"))
		for i in self.blocked_list:
			print("{} --> {}".format(i, [ process.pcb.pid for process in self.blocked_list[i]]))

	def show_event(self):
		print("**************************************************")
		print("{:>50}".format("Rest Events"))
		print([event.name for event in self.events])
		print("{:>50}".format("Current Events"))
		print([event.name for event in self.current_event])
		print()


	def run(self):
		self.events 				= [ 
										Event(name = "event1", semaphore = 2),
										Event(name = "event2", semaphore = 1),
										Event(name = "event3", semaphore = 2),
									
										]
		self.current_event 			= [	Event(name = "event4", semaphore = 1),
										Event(name = "event5", semaphore = 2)]
		self.show_list()
		# self.load_job_info(filename = "data.csv")

		while(1):
			if self.menu_show:
					self.menu()
			self.clock += 1

			if self.clock == YidanTime("24:00"):
				break


			if self.event_sustain == YidanTime(0):


				# self.event_happen()
				self.show_event()

				self.event_sustain = self.event_sustain - 1
				self.block_ready_switch()
				self.show_list()
				self.run_process()


			else:
				self.event_sustain = self.event_sustain - 1
				
				self.run_process()

			if self.space_enough == False:
				suspend_processes = []
				
				for i in self.blocked_list:
					suspend_processes.append(random.choice(self.blocked_list[i]))
				for process in suspend_process:
					self.suspend_process(process)
				
				self.space_enough = True

			else:
				with open("suspend_list.csv", "r") as fr:
					lines = fr.readlines()
					if len(lines) > 1:
						titles 				= lines[0].split(",")
						self.awake_process(pid = lines[1][titles.index("pid")])




	# Load The Job
	def ask_job_info(self):
		# Generate a Job by asking the user
		print("Please Input the event that job required")
		eventNum = input()
		print("Please Input the job happen time")
		happenTime = YidanTime(input())
		print("Please Input the time that the job need to run")
		runningTime = YidanTime(input())
		print("Please Input the priority of the job")
		priority = int(input())

		return Job(eventNum, happenTime, runningTime, priority)

	def load_job_info(self, filename):

		"Load the jobs information from a local file "
		assert filename[-4:] == ".csv", "CSV file required"

		job_list = []
		with open(filename, "r") as fr:
			title = fr.readline()
			title = title.split(",")
			# Remove "\n"
			title[-1] = title[-1][:-1]

			eventNum 		= title.index("event_name")
			happenTime 		= title.index("happen_time")
			runningTime 	= title.index("running_time")
			priority 		= title.index("priority")
			# print("eventNum, happenTime, runningTime, priority")
			for line in fr.readlines():
				content = line.split(",")
				# print(content[eventNum], content[happenTime], content[runningTime], content[priority])
				job_list.append(Job(event_name = content[eventNum], happen_time = content[happenTime], 
									running_time = content[runningTime], priority = content[priority]))
		
		for job in job_list:
			self.create_process(job)



	# *********************************************************
	# OPERATION ORIGIN COMMAND

	def create_process(self, job):
		"Create a process based on a job"
		process = Process(os = self, pid = self.pid, job = job)
		
		process.pcb.time_period = random.randint(1, 4)

		self.pid = self.pid + 1 


		mark = self.check_event_happending(process)

		if mark:
			self.ready_list[job.event_name].append(process)
		else:
			self.blocked_list[job.event_name].append(process)


	def check_event_happending(self, process):
		event_name = process.pcb.event
		mark = False
		for i in self.current_event:
			if i.name == event_name:
				mark = True
				break
		return mark

	def run_process(self):
		"Excute the current process in the cpu"

		if self.running_process == None:
			a = self.dispatch_process()
			if a == False:
				return 


		# Check the required event is still happending?

		if not self.check_event_happending(self.running_process):
			self.waitEvent_process()
			a = self.dispatch_process()
			if a == False:
				return 

		print("{}, {}".format(self.running_process.pcb.pid, self.running_process.pcb.running_time))
		

		self.running_process.pcb.running_time -= 1


		if self.running_process.pcb.running_time == YidanTime(0):
			self.exit_process(self.running_process)
			self.running_process = None
			self.dispatch_process()

		# Time Period minus 1
		self.time_period -= 1 
		if self.time_period == YidanTime(0):
			self.timeUp_process()


	def exit_process(self, process):
		"Exit the current process, for any reason"
		process_memory = Memory(lower_bound = process.pcb.lower_bound, upper_bound = process.pcb.upper_bound)

		self.recycle_memory_algo(self.empty_memory, process_memory)

		self.used_memory.remove(process_memory)

		return 

	def repeal_process(self, pid):
		mark = False
		for i in self.ready_list:
			in_list = self.ready_list[i]
			for j in in_list:
				if j.pcb.pid == pid:
					mark = True
					self.ready_list[i].remove(j)
					self.exit_process(j)
					self.blocked_list[j.pcb.event].append(j)
					return mark
		
		for i in self.blocked_list:
			in_list = self.blocked_list[i]
			for j in in_list:
				if j.pcb.pid == pid:
					mark = True
					self.blocked_list[i].remove(j)
					self.exit_process(j)
					return mark		
		return False



	def dispatch_process(self):
		"Dispatch a ready process from ready_list based on the priority"

		record_list = {}
		for seq, i in enumerate(self.ready_list):

			if len(self.ready_list[i]) > 0:
				self.ready_list[i].sort(key = lambda x: x.pcb.priority, reverse = False)
				record_list[i] = self.ready_list[i][0].pcb.priority
		if record_list != {}:
			get_result 	= max(record_list, key = record_list.get)
			process  	= self.ready_list[get_result].pop(0)

			self.running_process 	= process
			self.time_period 		= process.pcb.time_period
		else:
			return False
		return True

	def timeUp_process(self):
		"the current process Time Up "
		if self.running_process == None:
			return
		self.ready_list[self.running_process.pcb.event].append(self.running_process)
		self.running_process = None
		return 


	def waitEvent_process(self):
		self.blocked_list[self.running_process.pcb.event].append(self.running_process)
		self.running_process = None
		return 

	def block_ready_switch(self):

		for i in [event.name for event in self.current_event]:
			if self.ready_list[i] == []:
				self.ready_list[i] 		= self.blocked_list[i]
				self.blocked_list[i] 	= []

		for i in [event.name for event in self.events]:
			if self.blocked_list[i] == []:
				self.blocked_list[i] 	= self.ready_list[i]
				self.ready_list[i] 		= []
		return 

	def suspend_process(self, process):
		assert type(process) is Process, "Suspend Object should be process"
		
		for i in self.blocked_list:
			for j in self.blocked_list[i]:
				if j.pcb.pid == process.pcb.pid:
					self.blocked_list[i].remove(j)
					break
		with open("suspend_list.csv", "a") as fw:
			sent = str(process.pcb.pid)+","+ str(process.pcb.priority)+","+ str(process.pcb.event)+","+ str(process.pcb.happen_time)+","+ str(process.pcb.running_time)+","
			fw.write(sent)
		fw.close()
		self.exit_process(process)



	def awake_process(self, pid):
		with open("suspend_list.csv", "r") as fr:
			titles = fr.readline()
			titles = titles.split(",")
			titles[-1] = titles[-1][:-1]

			pid_f 				= titles.index("pid")
			priority 			= titles.index("priority")
			event_name 			= titles.index("event_name")
			happen_time 		= titles.index("happen_time")
			running_time 		= titles.index("running_time")

			mark  =  False

			for line in fr.readlines():
				line = line.split(",")
				if pid == int(line[pid_f]):
					self.create_process(Job(event_name 		= line[event_name], 
											happen_time 	= YidanTime(line[happen_time]), 
											running_time 	= YidanTime(line[running_time]),
											priority 		= int(line[priority])))
					mark = True

		fr.close()
		if mark:
			delete_a_record(pid, "suspend_list.csv")
			return True
		else:
			return False


											



	# *********************************************************
	# Memory Managing Part
	def apply_space(self):
		result, lower_bound, upper_bound = self.apply_memory_algorithm(self.empty_memory, random.randint(0, self.pcb_max_size), self.threshold)
		if result == True:
			self.empty_memory[0] = self.empty_memory[0] - Memory(lower_bound, upper_bound)
			self.used_memory.append(Memory(lower_bound, upper_bound))
			return lower_bound, upper_bound
		else:
			self.space_enough = False
			return None, None


def main():
	s = System_2()
	s.run()

if __name__ == '__main__':
	main()
