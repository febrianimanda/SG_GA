from random import *
from operator import itemgetter

nPop = 10
nGen = 8
era = 0;
matingPool = []
newPop = []
survivor = []
dictPop = []

def decoding(binary): #decode binary to decimal
	x = int(binary[:4],2)
	y = int(binary[4:],2)
	return [x,y]

def encoding(x,y): #encode decimal to binary
	bin1 = "{0:04b}".format(x)
	bin2 = "{0:04b}".format(y)
	return bin1+bin2

def fitnes(f): #fitness
	return 100+1/(f+0.01)

def fungsi(x,y): #problem
	return 3*(x**2) + 2*(y**2) - 4*x + y/2

def arrToString(arr):
	return "".join(map(str,arr))

def fitnessing(population, rangePop): #fungsi melakukan fitness
	gen = []
	for a in range(rangePop):
		conv = arrToString(population[a])
		bil = decoding(conv)
		gen.append(fitnes(fungsi(bil[0], bil[1])))
	return gen;

def parentSelection(fitnessPopulation, rand): #seleksi orangtua
	total = 0
	for a in range(nPop):
		total += fitnessPopulation[a]
		if(total > rand):
			return a

def rouletteWheel(fitnessPop, population):
	selected = []
	while len(selected) < 2 :
		n = uniform(min(fitnessPop), sum(fitnessPop))
		selected.append(population[parentSelection(fitnessPop,n)])
	return selected

def crossOver(par): #fungsi crossover
	titik = sample(range(1,8),3)
	titik.sort()
	silang = randint(0,1)
	a = 0 if silang == 0 else 1
	b = 1 if silang == 0 else 0
	child1 = par[a][titik[0]:titik[1]] + par[a][titik[2]:] + par[b][:titik[0]] + par[b][titik[1]:titik[2]]
	child2 = par[b][titik[0]:titik[1]] + par[b][titik[2]:] + par[a][:titik[0]] + par[a][titik[1]:titik[2]]
	return [child1, child2]

def mutation(kromosom, L, N):
	# pm = uniform(1/float(L), 1/float(N*L))
	setMutation = 0.2
	for i in range(L):
		rand = uniform(0,1)
		if (rand < setMutation) :
			kromosom[i] = 1 - kromosom[i]
	return kromosom

def books(list1, list2, n):
	book = []
	for i in range(n):
		book.append({"biner":list1[i], "fitness":list2[i]})
	return book

def initPopulation():
	return [[randint(0,1) for x in range(nGen)] for y in range(nPop)]

for era in range(10000):
	
	#inisialisasi populasi
	pop = newPop[:] if (era > 0) else initPopulation()
	# print era
	# for i in range(nPop):
	# 	print decoding(arrToString(pop[i]))
	newPop[:] = []

	#fitness populasi
	genFit = fitnessing(pop, nPop)
	dictPop = books(pop,genFit,nPop)

	solution = decoding(arrToString(pop[genFit.index(max(genFit))]))

	print solution

	maxFit = 0
	xFit = 0

	#seleksi orang tua
	matingPool[:] = []
	for i in range(nPop/2):
		parent = rouletteWheel(genFit, pop)

		# print "pool : ",decoding(arrToString(parent[0])), " ", decoding(arrToString(parent[1]))
		#crossover
		child = crossOver(parent)
		# print "child : ", decoding(arrToString(child[0])) , " ", decoding(arrToString(child[1]))
		#mutation
		child[0] = mutation(child[0],nGen,nPop)
		child[1] = mutation(child[1],nGen,nPop)
		
		matingPool.append(child)

	#seleksi survivor
	survivor[:] = []
	for i in range(nPop/2):
		for j in range(2):
			survivor.insert(i, matingPool[i][j])
	genSurvivor = fitnessing(survivor, nPop)
	dictPop.extend(books(survivor,genSurvivor,nPop))
	
	dictPop = sorted(dictPop, key=itemgetter('fitness'), reverse=True)

	for i in range(10):
		newPop.append(dictPop[i].values()[0])

print solution
print fungsi(solution[0], solution[1])