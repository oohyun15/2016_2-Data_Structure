def gcd(a,b):
	while a != b:
		if a>b:
			a = a-b
		else:
			b = b-a
	return a

class Fraction:
	def __init__(self,num,denom):
		self._num = int(num / gcd(abs(num),abs(denom)))
		self._denom = int(denom / gcd(abs(num), abs(denom)))
		if self._denom == 0:
			raise ZeroDivisionError("denominator can't be 0")
		elif self._denom < 0:
			self._denom = abs(self._denom)
			self._num = -1*self._num
	def __add__(self,other):
		newnum = self._num*other._denom + self._denom*other._num
		newdenom = self._denom*other._denom
		return Fraction(newnum,newdenom)
	def __sub__(self,other):
		newnum = self._num*other._denom - self._denom*other._num
		newdenom = self._denom*other._denom
		return Fraction(newnum,newdenom)
	def __mul__(self,other):
		newnum = self._num*other._num
		newdenom = self._denom*other._denom
		return Fraction(newnum,newdenom)
	def __truediv__(self,other):
		newnum = self._num*other._denom
		newdenom = self.denom*other._num
		return Fraction(newnum,newdenom)
	def __gt__(self,other):
		return self._num*other._denom - self._denom*other._num > 0
	def __ge__(self,other):
		return self._num*other._denom - self._denom*other._num >= 0
	def __lt__(self,other):
		return self._num*other._denom - self._denom*other._num < 0
	def __le__(self,other):
		return self._num*other._denom - self._denom*other._num <= 0
	def __eq__(self,other):
		return self._num*other._denom - self._denom*other._num == 0
	def __ne__(self,other):
		return self._num*other._denom - self._denom*other._num != 0
	def __str__(self):
		if self._denom == 1:
			return str(self._num)
		else:
			return str(self._num)+"/"+str(self._denom)


