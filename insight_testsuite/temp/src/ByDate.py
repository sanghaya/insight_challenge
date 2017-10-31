import numpy as np

class ByDate(object):
	"""
	Object to keep track and update transaction values for each (cmtd_id, date) pair.
	Use slots to allocate space for only fixed attributes.

	"""
	__slots__ = ['cmte_id', 'date', 'trx_amt']
	def __init__(self, cmte_id, date):
		self.cmte_id = cmte_id
		self.date = date
		self.trx_amt = []

	def __eq__(self, other):
		if isinstance(other, self.__class__):
				return self.cmte_id == other.cmte_id and self.date == other.date
		else:
				return False

	def increment(self, trx_amt):
		self.trx_amt.append(trx_amt)

	# Made a rounding function instead of the built-in function because of its special edge case
	# For instance, round(240.5) will return 240 instead of 241 that we want

	def getMedian(self):
		temp = np.median(self.trx_amt)
		deci = temp-int(temp)
		return int(temp)+int(round(deci+1))-1

	def toString(self):
		return self.cmte_id+'|'+self.date+'|'+str(self.getMedian())+'|'+str(len(self.trx_amt))+'|'+str(sum(self.trx_amt))+'\n'




