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

def fitnes(f):
	return 1/(f+0.1)

def fungsi(x,y):
	return 3*(x**2) + 2*(y**2) - 4*x + y/2

def parentSelection(probPopulation, rand):
	total = 0
	for a in range(10):
		total += probPopulation[a]
		if(total > rand):
			return a

#inisialisasi populasi
pop = [[randint(0,1) for x in range(gen)] for y in range(nPop)]


#fitness populasi
genFit = []
for a in range(10):
	conv = "".join(map(str,pop[a]))
	bil = decoding(conv)
	genFit.append(fitnes(fungsi(bil[0], bil[1])))

prob = [(genFit[a]/sum(genFit)) for a in range(10)] #probabilitas fitness 

#seleksi orang tua
par = []
while len(par) < 2: #roulette-wheel
	n = uniform(0,sum(genFit))
	par.append(pop[parentSelection(prob,n)])

# def crossOver(kromosom):
# 	titik = sample(range(1,8),3)
# 	# i = 0
# 	# while len(titik) < 3 :
# 	# 	titik.append(randint(1,8))
# 	# 	titik.sort()
# 	return titik.sort()

# print crossOver(par[0])