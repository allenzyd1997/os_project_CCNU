from page import Page

class System4(object):

	def __init__(self, file = None):

		self.data_list 	= self.data_initialize(file)
		self.length_of_data = len(self.data_list)

		self.pageAmount = self.pageAmount_intialize()
		self.algorithm 	= self.algorithm_initialize()
		self.current_list 	= []
		self.total_list 	= []
		self.changePage     = []
		


	def data_initialize(self, file):
		
		data_list = []

		if file != None:
			assert file[-4:] == ".csv", "only accept csv file"
			with open(file, "r") as fr:
				content = fr.read()
				for seq, data in enumerate(content.split(",")):
					data_list.append(Page(sequence = seq, num = int(data)))

		else:
			print("Input the Number, if you finish your inputting, please input -1 ")
			counter = 0 
			while(1):
				num = input()
				if num == "-1":
					break
				else:
					data_list.append(Page(sequence = counter, num = int(num)))
				counter += 1


		for i in data_list:
			print(i.num, end = " ")
		return data_list
	
	def algorithm_initialize(self):
		
		algorithm  = None

		print("\n please choose the algorithm you want to use:\n")
		print("1. LRU")
		print("2. OPT")
		print("3. FIFO\n")
		try:
			a = int(input())
		except:
			raise Exception

		if a == 1:
			algorithm = self.LRU
			self.LRU_Dic = {}

		elif a == 2:
			algorithm = self.OPT
		elif a == 3:
			algorithm = self.FIFO

		if algorithm == None:
			print("please input again")
			return self.algorithm_initialize()

		return algorithm

	def pageAmount_intialize(self):
		pageAmount = None 

		print("\n please input the page frame size: \n")

		pageAmount = int(input())

		return pageAmount

	def run(self):

		for i in range(self.length_of_data):

			nextPage = self.data_list[i]
			changePage, pageNum  = self.algorithm(self.current_list, nextPage)
			
			

			if changePage:
				if self.check_Page(self.current_list):
					self.supersedeLess(nextPage)
				else:
					self.supersede(pageNum, nextPage)

			a = self.current_list.copy()
			self.total_list.append(a)
			self.changePage.append(changePage)
		return

	def supersedeLess(self, nextPage):
		lista = [nextPage]
		for i in self.current_list:
			if type(i) is Page:
				lista.append(i)
		self.current_list = lista
		return

	def supersede(self, pageNum, nextPage):
		for i in self.current_list:
			if i.num == pageNum:
				self.current_list.remove(i)
				break
		self.current_list.insert(0, nextPage)
		return 

	def judge_in(self, current_list, nextPage):
		result = True
		for page in current_list:
			if nextPage.num == page.num:
				result = False
		return result

	def check_Page(self, current_list):
		counter = 0 
		for i in current_list:
			if type(i) == Page:
				counter = counter + 1 
		return counter < self.pageAmount 


	def LRU(self, current_list, nextPage):
		changePage = self.judge_in(current_list, nextPage)
		pageNum = None


		print("current_list", [a.num for a in current_list])
		if changePage:
			if self.check_Page(current_list):
				for other in self.LRU_Dic:
					self.LRU_Dic[other] += 1
				self.LRU_Dic[nextPage.num] = 1 


			else:
				if self.LRU_Dic != {}:
					pageNum = max(self.LRU_Dic, key = lambda x: self.LRU_Dic[x])

					for other in self.LRU_Dic:
						self.LRU_Dic[other] += 1
					self.LRU_Dic.pop(pageNum)
					self.LRU_Dic[nextPage.num] = 1


		else:
			pageNum = None
			
			for other in self.LRU_Dic:
				self.LRU_Dic[other] += 1
			self.LRU_Dic[nextPage.num] = 0

		return changePage, pageNum

	def FIFO(self, current_list, nextPage):
		changePage = self.judge_in(current_list, nextPage)
		pageNum = None 
		if changePage:
			if current_list != []: 
				pageNum = current_list[-1].num

		return changePage, pageNum

	def OPT(self, current_list, nextPage):
		changePage = self.judge_in(current_list, nextPage)
		pageNum = None
		opt_dic = {}
		found   = False
		
		if changePage:	
	
			for i in current_list:
				found = False

				for j in self.data_list[nextPage.sequence:]:
					if j.num == i.num:

						opt_dic[i.num] = j.sequence - nextPage.sequence
						found = True
					else:
						continue
				if found == False:
					opt_dic[i.num] = 1000000


			if opt_dic != {}:
				for i in opt_dic:
					print("current in ", nextPage.sequence, ":")
					print(i , ":", opt_dic[i])	
				pageNum = max(opt_dic, key =lambda x: opt_dic[x])
				opt_dic[nextPage.num] = 1000000



			print("----------------------")
		else:
			pageNum = None
			self.supersede(nextPage.num, nextPage)

		return changePage, pageNum

	def output(self):

		for seq, i in enumerate(self.total_list):
			print(" ----------------------------")
			print([j.num for j in i],end = "    ")
			print("CHANGED? {:>20}".format(self.changePage[seq]))
		return 

def cal_rate(lista):
	counter = 0 
	to_counter = 0
	for a in lista:
		to_counter += 1
		if a == False:
			counter += 1
	return counter / to_counter


def main():
	s = System4(file = "belady.csv")
	s.run()
	s.output()
	print("命中率:{:>10}".format(str(cal_rate(s.changePage))))
	s = System4(file = "belady.csv")
	s.run()
	s.output()
	print("命中率:{:>10}".format(str(cal_rate(s.changePage))))

if __name__ == '__main__':
	main()
