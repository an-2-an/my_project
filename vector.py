from math import sqrt, acos, pi


class Vector:
	def __init__(self, coords):
		self.coords = coords
	def __float__(self):
		return sqrt(sum([c**2 for c in self.coords]))
	def __add__(self, other):
		return Vector([(c1 + c2) for c1, c2 in zip(self.coords, other.coords)])
	def __sub__(self, other):
		return Vector([(c1 - c2) for c1, c2 in zip(self.coords, other.coords)])	
	def __str__(self):
		return '({})'.format(', '.join([str(c) for c in self.coords]))
	def mult_k(self, k):
		return Vector([k * c for c in self.coords])	
	def __mul__(self, other):
		return sum([(c1 * c2) for c1, c2 in zip(self.coords, other.coords)])
	def alpha(self, other):
		print(self*other, float(self), float(other))
		return acos((self * other) / (float(self) * float(other))) / pi * 180
	def is_collinear(self, other):
		return all([(c1 / c2) == (self.coords[0] / other.coords[0]) for c1, c2 in zip(self.coords, other.coords)])  
	def cross_product(self, other):
		return Vector([self.coords[1]*other.coords[2] - self.coords[2]*other.coords[1], self.coords[2]*other.coords[0] - self.coords[0]*other.coords[2], self.coords[0]*other.coords[1] - self.coords[1]*other.coords[0]])

if __name__ == '__main__':
  a = Vector([2, 3, 4])
  ma = float(a)
  print(f'|a| = {ma:.2f}')
  b = Vector([5, 4, 1])
  mb = float(b)
  print(f'|b| = {mb:.2f}')
  c = a + b
  print(c)
  d = a - b
  print(d)
  e = a.mult_k(2.5)
  print(e)
  p = a * b
  print(p)
  alpha = a.alpha(b)
  print(alpha)
  a_b = a.is_collinear(b)
  print(a_b)
  a_e = a.is_collinear(e)
  print(a_e)
  f = a.cross_product(b)
  print(f)

