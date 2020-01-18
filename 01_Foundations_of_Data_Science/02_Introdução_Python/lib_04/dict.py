def iniciar():
	print('Iniciando')

def count_freq(lista):
	a =[a**2 for a in lista if a < 3]
	print(a)

#QUESTAO 36
def count_freq2():
	f = open('char.txt','r')
	a = f.readlines()
	lista = []
	countpy, countc, counttxt = 0,0,0
	for item in a:
		item = item.strip('\n')
		lista.append(item)
		if 'def' in item:
			countpy+=1
		if '%' in item:
			countc+=1
		if 'def 'not in item and '%' not in item:
			counttxt+=1
	print(lista)
	if countpy  > countc:
		print('E um programa py')
	if countc > countpy:
		print('E um programa c')
	if counttxt > countc and  counttxt > countpy:
		print('E um programa txt')

#QUESTAO 37
def anagram(lista):

	dock, docker = [], []
	for item in lista:
		dock.append(sorted(item))
	for i in range(0, len(lista)):
		pool = []
		for a in range(0, len(dock)):
			if dock[i] == dock[a] and lista[a] not in pool:
				pool.append(lista[a])
		if pool not in docker:
			docker.append(pool)
	print(docker)

#QUESTAO 38
def valuesort(dic):
	a = sorted(dic)
	print(a)
	for item in a:
		print(dic[item])

#QUESTAO 39
def inverdic(dict):
	a = sorted(dict)
	b =  {}
	num = []
	print(dict)
	print(type(a), type(b), type(dict))
	for item in a:
		num.append(dict[item])
	print(a, num)
	count=0
	for i in num:
		b[i] = a[count]
		count+=1
	print(b)
