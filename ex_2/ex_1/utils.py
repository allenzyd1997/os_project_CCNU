def base_sort(lista):
	"A Basic Sort Methot"
	lista.sort(key = lambda x: x.enterTime)
	return lista

def priority_sort(lista):
	"A Basic Sort Methot"
	lista.sort(key = lambda x: x.priority, reverse = True)
	return lista

def channel_priority_sort(lista):
	lista.sort(key = lambda x: x.currentJob.priority, reverse = True)
	return lista

def algorithm_fifs(lista):
	"First in First servived"
	lista.sort(key = lambda x: x.enterTime)
	return lista

def algorithm_sp(lista):
	"Short Priority"
	lista.sort(key = lambda x: (x.runningTime))

def algorithm_rrh(lista):
	"Responce Ratio High"
	lista.sort(key = lambda x: (x.waitingTime + x.runningTime) / x.runningTime)
	return lista
