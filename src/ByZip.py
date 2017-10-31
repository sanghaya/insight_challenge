import numpy as np

class ByZip(object):
	"""
	Object to keep track and update transaction values for each (cmtd_id, zipcode) pair.
	Use slots to allocate space for only fixed attributes.

	"""
	__slots__ = ['cmte_id', 'zipcode', 'trx_amt', 'trx_tot', 'median', 'count']
	def __init__(self, cmte_id, zipcode):
		self.cmte_id = cmte_id
		self.zipcode = zipcode
		self.trx_amt = []
		self.trx_tot = 0
		self.median = 0
		self.count = 0

	def __eq__(self, other):
		if isinstance(other, self.__class__):
				return self.cmte_id == other.cmte_id and self.zipcode == other.zipcode
		else:
				return False

	def increment(self, trx_amt):
		self.trx_amt.append(trx_amt)
		self.trx_tot += trx_amt
		self.count += 1
		self.median = self.getMedian()

	# Made a rounding function instead of the built-in function because of its special edge case
	# For instance, round(240.5) will return 240 instead of 241 that we want

	def getMedian(self):
		temp = np.median(self.trx_amt)
		deci = temp-int(temp)
		return int(temp)+int(round(deci+1))-1

	def toString(self):
		return self.cmte_id+'|'+self.zipcode+'|'+str(self.median)+'|'+str(self.count)+'|'+str(self.trx_tot)+'\n'




