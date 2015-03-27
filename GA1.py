from random import randint
def fungsi_minimasi (a,b):
	a = (3*a**2+2*b**2-4*a+b//2)
	return a
def fitness(a):
	fit = 1/a+0.1
	return fit

fungsi_minimasi(1,0)

def binary(a,b):
	bin_a = "{0:b}".format(a)
	bin_b = "{0:b}".format(b)
	return bin_a+bin_b

def encode(a):
	mid = len(a)//2
	x = int(a[:mid],2)
	y = int(a[mid:],2)
	return [x,y]

pop = [[randint(0,1)for a in range(6)]for b in range (10)]


a = binary(5,6)
print (a)
print (encode(a))
print (fitness(fungsi_minimasi(5,6)))
b = ''.join(map(str,pop[0]))
print (b)
