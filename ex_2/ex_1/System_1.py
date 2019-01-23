from utils import base_sort, algorithm_fifs, algorithm_sp, algorithm_rrh
from job   import Job
from channel_manager import channel_manager
from yidan_time import YidanTime

class System_1(object):

	def __init__(self, algorithm = algorithm_rrh, file = None):
		print("Does Priority Apply for Your Job List? 1 for Yes, 0 for No")
		
		self.priority = int(input())

		self.job_list = self.initialize(file)

		print("Input the channel of the system")
		self.channel 	= int(input())

		self.clock    	= YidanTime(0)

		self.cm 		= channel_manager(self.channel)

		self.algorithm  = algorithm

		self.excuted_job = []

		self.happened_job = []

	def calculate(self):
		# This method is for calculating the job requirement
		# Channel is the channel amount offered to this algorithm
		# Algorithm is the algorithm used in this computation
		# What will be calculated and return?
		# *** Beginning time: Beginning time of each job
		# *** End Time: End Time of each Job
		# *** Cycling Time
		# *** Weighted Cycling Time
		# *** Average Cycling Time
		# *** Average Weighted Cycling Time.
		return None

		

	def run(self):

		# Imitate the actual system running in this function

		assert self.channel == 1 or (self.channel !=1 and self.priority == 1), "while channel is one, you need offered the priority of the job"
		self.execute_list = self.job_list.copy()

		while(1):
			# Print out the current time
			self.happen_job_check()
			job = self.cm.excuteAllChannels(self.clock)
			if type(job) == Job:
				self.excuted_job.append(job)


			if self.clock.minute % 10 == 0:
				
				print("\n******************************")
				print("Current Time ", self.clock)
				print("******************************\n")
				
			
			while(1):

				result = self.cm.isChannelEmpty(self.clock)

				if result == False:
					break

				else:
					if self.isOtherJob():
						self.cm.addJob(self.happened_job[0], self.clock)
						self.happened_job = self.happened_job[1:]
					else:
						break
					
			self.clock = self.clock + 1
			

			if self.clock == YidanTime("14:00")	:
				print("\n******************************")
				print("Current Time ", self.clock)
				print("******************************\n")
				print("====================>  Time Over  <====================")

				break

	def happen_job_check(self):

		for job in self.job_list:
			if self.clock == job.enterTime:
				self.happened_job.append(job)
		return 



	def isOtherJob(self):
		if self.happened_job == []:
			return False
		else:
			self.sort()
			return True

	def sort(self):
		self.algorithm(self.happened_job)

	def write_back_job(self, filename):
		# Write the Job list to the file
		if filename[-4:] != ".csv":
			filename += ".csv"
		with open(filename, "w") as fw:

			fw.write("Sequence, Enterring Time, Running Time, Priority, Waiting Time\n")

			for job in self.job_list:

				try:
					sent = str(job.sequence) +","+ str(job.enterTime)+","+str(job.runningTime)+","+str(job.priority)+","+str(job.waitingTime)+"\n"
				except:
					continue

				if sent != "\n":
					fw.write(sent)
		return 

	def show_job_list(self, lista):
		# Show the List
		if lista != None:
			print("")
			print("=================================================================================================\n")
			
			print("=========================>>                                       <<=============================\n")
			print("{:<20}{:<20}{:<20}{:<20}{:<20}{:<20}{:<20}".format('Sequence','Enter Time', 'Running', 'Priority', 'Waiting Time', 'enter Channel Time' , 'Cycling Time'))

			for job in lista:
				if self.priority == 0:
					print("{:<20}{:<20}{:<20}{:<20}{:<20}{:<20}{:<20}".format(job.sequence, job.enterTime, job.runningTime, "N\A", job.waitingTime, job.inChannelTime, job.cyclingTime))
				else:
					print("{:<20}{:<20}{:<20}{:<20}{:<20}{:<20}{:<20}".format(job.sequence, job.enterTime, job.runningTime, job.priority, job.waitingTime, job.inChannelTime,  job.cyclingTime))
			print("=================================================================================================\n")

		return 

	def initialize(self, file):
		"We Initialize the job_list in this method"

		job_list = []
		if file != None:
			assert file[-4:] == ".csv", "We required .csv file as input file"
			
			job_sequence = 0

			with open(file, "r") as f:
				for line in f.readlines()[1:]:

					ajob = line.split(",")
					try:
						int(ajob[0]) 
					except:
						continue

					if self.priority == 0:
						if ajob[1] == None or ajob[2] == None:
							continue
						job_list.append(Job(job_sequence, ajob[1], ajob[2], None, 0))
					else:
						if ajob[1] == None or ajob[2] == None or ajob[3] == None:
							continue
						job_list.append(Job(job_sequence, ajob[1], ajob[2], ajob[3], 0))
					job_sequence += 1

			return job_list

		else:

			job_sequence = 0 

			while(1):

				print(" ")
				print("===================================================================")

				print("1 for input a job. 0 for no more job")


				command = input()
				if command == "1":

					# The First Input
					print("-----------------------------------------------------------------")
					print("please input the enterring time, eg:   10:00 ")
					enter_time = input()
					try:
						assert len(enter_time) == 5 and int(enter_time[:2]) <= 24 and int(enter_time[:2]) >= 0 and enter_time[2] == ":" and int(enter_time[3:]) >= 0 and int(enter_time[3:])<=60
					except:
						print("Time Input Error, Please Enter informaiton again")
						continue
					

					# The Second Input
					print("-----------------------------------------------------------------")
					print("please input the running time")
					run_time = input()
					try:
						assert int(run_time) >0 
					except:
						print("Running Time Should be Greater than 0, Please Enter informaiton again")
						continue
					

					if self.priority == 1:

						# The Third Input
						print("-----------------------------------------------------------------")
						print("please input the priority")
						priority = input()
						try:
							assert int(priority) > 0 
						except:
							print("Priority Should be Greater than 0, Please Enter informaiton again")
							continue
					else:
						priority == None

					job_list.append(Job(job_sequence, enter_time, run_time, priority, 0))

					job_sequence += 1


				elif command == "0":
					break
				else:
					print("error, please input the command again")
					continue

			return job_list

def main():
	s = System_1(file = "test.csv")
	s.show_job_list(s.job_list)
	s.run()
	s.write_back_job("test1.csv")
	if s.job_list != []:
		print("job_list")
		s.show_job_list(s.job_list)
	
	print("excuted_job")
	s.show_job_list(s.excuted_job)
if __name__ == '__main__':
	main()

