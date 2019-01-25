from job import Job 
from memory import Memory

from algorithms import algorithm_memory_apply_worst_adapt, algorithm_memory_apply_best_adapt, algorithm_memory_apply_first_adapt, algorithm_memory_recycle


class System_3(object):

	def __init__(self, script = None):

		print("Please input the total size of the system")
		self.system_size 			= int(input())


		self.job_total_list			= []
		self.initialize()



		self.algorithm_set  	= [algorithm_memory_apply_worst_adapt, algorithm_memory_apply_best_adapt, algorithm_memory_apply_first_adapt]
		self.no_used_algorithm  = [algorithm_memory_apply_worst_adapt, algorithm_memory_apply_best_adapt, algorithm_memory_apply_first_adapt]
		# Algorithm setting for allocaing memory
		print("please input the algorithm that you want to use")
		print("1 Best adapt")
		print("2 Worst adapt")
		print("3 First adapt")
		choice = int(input())

		if choice == 1:

			self.algorithm  		= algorithm_memory_apply_best_adapt

		elif choice == 2:

			self.algorithm  		= algorithm_memory_apply_worst_adapt

		else:
			self.algorithm  		= algorithm_memory_apply_first_adapt


		self.no_used_algorithm.remove(self.algorithm)
		# Algorithm setting for recycle the memory
		self.recycle_algorithm 	= algorithm_memory_recycle

		# ***** MANAGE THE MEMORY *********


		# ***** THRESHOLD SETTTING ********
		print("please input the threshold of this system")
		self.threshold  	= int(input())


		
	def menu(self):

		while(1):

			print("***************************************")
			print("1  ADD A Job")
			print("2  RECYCLE A Job")
			print("3  SHOW MEMORY")
			print("4  ADD SCRIPT")
			print("-1 EXIT")
			print("***************************************")
			print()
			choice = int(input())

			if choice == -1:
				break
			elif choice == 1:
				self.add_job()

			elif choice == 2:
				self.recycle_job()

			elif choice == 3:
				self.show_memory()
				self.show_list()

			elif choice == 4:
				self.add_script()

			else:
				continue
		return 


	def run(self):

		while(1):
			# if the job list is empty means the system running is over. waiting for user command
			if self.job_list == []:
				self.menu()

			else:
				# for job in the job list do the job list allocate
				for job in self.job_list:
					result, lower_bound, upper_bound = self.algorithm(self.empty_memory_list, job.size, self.threshold)
					print("RESULT", result)
					print("LOWER_BOUND", lower_bound)
					print("upper_bound", upper_bound)
					if result:
						self.allocate_memory(job, lower_bound, upper_bound)
						self.job_list.remove(job)
						self.job_using_memory.append(job)
					else:
						self.allocate_fail()

	def initialize(self):
		

		self.memory 				= Memory(lower_bound = 0 , upper_bound = self.system_size)

		self.empty_memory_list		= []
		self.empty_memory_list.append(self.memory)
		self.allocated_memory_list	= []

		self.job_list 				= self.job_total_list 
		self.job_using_memory 		= []
		self.job_total_list			= []


	def add_job(self):
		print("Please input the job Name")
		jobName = input()
		print("Please input the job size")
		size 	= int(input())
		newJob  = Job(jobName, size)
		self.job_list.append(newJob)
		self.job_total_list.append(newJob)
		print("job added ", self.job_list)
		return

	def recycle_job(self):
		print("Please input the job name that you want to recycle")
		jobName = input()
		found 	= False
		for job in self.job_using_memory:
			if job.jobName == jobName:
				found = True
				print("Found")
				self.job_using_memory.remove(job)
				self.recycle_algorithm(self.empty_memory_list, self.allocated_memory_list, job.memory)
		if found:
			print("Already Recylced")
		else:
			print("Job Not Found")

	def show_memory(self):
		print()
		print("** ** ** ** ** ** ** ** ** ** ** **")
		print("EMPTY MEMORY LIST:")
		for memory in self.empty_memory_list:
			print(memory)
			print("---------------")
		print("** ** ** ** ** ** ** ** ** ** ** **")
		print("Allocated MEMORY LIST:")
		for memory in self.allocated_memory_list:
			print(memory)
			print("---------------")
		print("** ** ** ** ** ** ** ** ** ** ** **")
		print()
		print()

	def show_list(self):
		print()
		print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

		print("{:^60}".format("LIST  STATUS  SHOW"))
		print("{:20}".format("job list"), self.job_list)
		print("{:20}".format("job using memory"), self.job_using_memory)
		print("{:20}".format("job total list"), self.job_total_list)
		print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

	def add_script(self):	
		print("please input the script name")
		script = input()
		if script != None:
			with open(script, "r") as f:
				titles 		= f.readline()
				titles[-1] 	= titles[-1][:-1]
				
				jobName 	= titles.index("jobName")
				size 		= titles.index("size")

				for line in f.readlines():
					newJob = Job(jobName, int(size))
					self.job_list.append(newJob)
					self.job_total_list.append(newJob)



	def allocate_memory(self, job, lower_bound, upper_bound):

		newMemory = Memory(lower_bound, upper_bound)
		job.memory = newMemory
		for seq, memory in enumerate(self.empty_memory_list):
			if lower_bound == memory.lower_bound:
				# Minus the memory that allocated
				self.empty_memory_list[seq] = self.empty_memory_list[seq] - newMemory
				# Add the new memory into allocated list
				self.allocated_memory_list.append(newMemory)
				break


	def allocate_fail(self):
		if self.no_used_algorithm == []:
			print("Algorithm all tried, cannot allocate this memory")
		else:
			self.algorithm = self.no_used_algorithm.pop(0)
			if self.algorithm == algorithm_memory_apply_worst_adapt:
				print("Tring Use Worst Adapt Algorithm")
				print("...")
			elif self.algorithm == algorithm_memory_apply_best_adapt:
				print("Tring Use Best Adapt Algorithm")
				print("...")
			elif self.algorithm == algorithm_memory_apply_first_adapt:
				print("Tring Use First Adapt Algorithm")
				print("...")
			else:
				print("Wrong")

			self.initialize()


def main():
	system = System_3()
	system.run()

if __name__ == '__main__':
	main()
