from random import *

nPop = 10
gen = 8

def decoding(binary): #decode binary to decimal
	x = int(binary[:4],2)
	y = int(binary[4:],2)
	return [x,y]

def encoding(x,y): #encode decimal to binary
	bin1 = "{0:04b}".format(x)
	bin2 = "{0:04b}".format(y)
	return bin1+bin2

def fitnes(f): #fitness
	return 1/(f+0.1)

def fungsi(x,y): #problem
	return 3*(x**2) + 2*(y**2) - 4*x + y/2

def parentSelection(fitnessPopulation, rand): #seleksi orangtua
	total = 0
	for a in range(10):
		total += fitnessPopulation[a]
		if(total > rand):
			return a

def crossOver(par): #fungsi crossover
	titik = sample(range(1,8),3)
	titik.sort()
	silang = randint(0,1)
	a = 0 if silang == 0 else 1
	b = 1 if silang == 0 else 0
	child1 = par[a][titik[0]:titik[1]] + par[a][titik[2]:] + par[b][:titik[0]] + par[b][titik[1]:titik[2]]
	child2 = par[b][titik[0]:titik[1]] + par[b][titik[2]:] + par[a][:titik[0]] + par[a][titik[1]:titik[2]]
	return [child1, child2]

#inisialisasi populasi
pop = [[randint(0,1) for x in range(gen)] for y in range(nPop)]


#fitness populasi
genFit = []
for a in range(10):
	conv = "".join(map(str,pop[a]))
	bil = decoding(conv)
	genFit.append(fitnes(fungsi(bil[0], bil[1])))

#seleksi orang tua
parent = []
while len(parent) < 2: #roulette-wheel
	n = uniform(min(genFit),sum(genFit))
	parent.append(pop[parentSelection(genFit,n)])

#crossover
child = crossOver(parent)
print child