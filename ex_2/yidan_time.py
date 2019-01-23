

class YidanTime(object):
	"""docstring for Time"""

	def __init__(self, stra):
		"get time based on a string"
		super(YidanTime, self).__init__()
		self.stra = stra

		if type(stra) is str:
			assert stra[0] != "-", "minus time error " +stra

			try:
				self.hour 	= int(stra) // 60
				self.minute = int(stra) % 60
			except:

				if len(stra) == 5:
					self.hour 	= int(stra[:2])
					self.minute = int(stra[-2:])
				elif len(stra) == 4:

					if stra[1] == ":":
						self.hour 	= int(stra[0])
						self.minute = int(stra[-2:])
					elif stra[2] == ":":
						self.hour 	= int(stra[:2])
						self.minute = int(stra[-1])
					else:
						raise Exception
					
				elif len(stra) == 3:
					if stra[1] == ":":
						self.hour 	= int(stra[0])
						self.minute = int(stra[2])
					else:
						raise Exception

			
		elif type(stra) is int:
			self.hour 	= int(stra) // 60
			self.minute = int(stra) % 60

		elif stra is None:
			self.hour 	= 0 
			self.minute = 0
		elif type(stra) is YidanTime:
			self.hour 	= stra.hour
			self.minute = stra.minute
		
		else:
			raise Exception


	def __eq__(self, obj):
		if type(obj) is YidanTime:
			return self.hour == obj.hour and self.minute == obj.minute
		elif type(obj) is int:
			return self.hour * 60 + self.minute == obj

	def __add__(self, obj):
		if type(obj) is int:
			o_hour 		= obj // 60 
			o_minute 	= obj % 60

			minute 		= self.minute + o_minute

			if minute >= 60:
				hour 		= (self.hour + o_hour + 1) 
				minute 		= minute % 60
			else:
				hour 		= (self.hour + o_hour ) 

			return YidanTime(str(hour)+":"+str(minute))

		elif type(obj) is YidanTime:
			minute 	= (self.minute + obj.minute)
			if minute >= 60:
				hour 	= (self.hour + obj.hour + 1) 
				minute  = minute % 60
			else:
				hour 	= (self.hour + obj.hour ) 

			return YidanTime(str(hour)+":"+str(minute))

		elif type(obj) is str:
			return self + YidanTime(obj)
	

	def __sub__(self, obj):
		
		minute 	= 0 
		borrow 	= 0 
		hour 	= 0

		if type(obj) is YidanTime:
			if self.minute >= obj.minute:
				minute = self.minute - obj.minute
			else:
				minute = self.minute + 60 - obj.minute
				borrow = 1 
			
			hour = self.hour - borrow - obj.hour 

			assert hour > 0, "SUB CAUSE MINUS TIME ERROR"

			return YidanTime(str(hour)+":"+str(minute))
		if type(obj) is int:
			if obj <= self.minute:
				return YidanTime(str(hour)+":"+str(self.minute - obj))
			else:
				assert hour > 0, "SUB CAUSE MINUS TIME ERROR"
				return YidanTime(str(hour - 1)+":"+str(self.minute + 60 - obj))


	def __truediv__(self, obj):
		if type(obj) is YidanTime:
			return (self.hour * 60 + self.minute) / (obj.hour * 60 + obj.minute)
		elif type(obj) is int:
			return (self.hour * 60 + self.minute) / obj


	def __floordiv__(self, obj):
		if type(obj) is YidanTime:
			return (self.hour * 60 + self.minute) // (obj.hour * 60 + obj.minute)
		elif type(obj) is int:
			return (self.hour * 60 + self.minute) // obj


	def __gt__(self, obj):
		if self.hour > obj.hour:
			return True
		elif self.hour == obj.hour and self.minute > obj.minute :
			return True
		else:
			return False


	def __ge__(self, obj):
		if self.hour > obj.hour:
			return True
		elif self.hour == obj.hour:
			if self.minute > obj.minute or self.minute  == obj.minute :
				return True
			else:
				return False
		else:
			return False


	def __lt__(self, obj):
		if self.hour < obj.hour:
			return True
		elif self.hour == obj.hour and self.minute < obj.minute :
			return True
		else:
			return False
	

	def __le__(self, obj):
		if self.hour < obj.hour:
			return True
		elif self.hour == obj.hour:
			if self.minute < obj.minute or self.minute  == obj.minute :
				return True
			else:
				return False
		else:
			return False


	def __str__(self):
		try:
			a = "{:0>2}".format(str(self.hour)) + ":" + "{:0>2}".format(str(self.minute))
		except:
			print(self.hour)
			print(self.minute)
			raise Exception
		return a


	def __format__(self, format_spec):
		return format(str(self), format_spec)