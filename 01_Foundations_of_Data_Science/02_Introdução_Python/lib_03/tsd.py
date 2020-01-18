def check():
	print("Iniciando...")

def pro1():
	x = [0,1,[2]]
	x[2][0] = 3
	print(x)
	x[2].append(4)
	print(x)
	x[2] = 2
	print(x)

def sum_(lista):
	soma = 0
	print(len(lista))
	for i in range(0, len(lista)):
		soma = int(lista[i]) + soma
	print("Soma: {}".format(soma))

def sum_s(lista):
	conc = ""
	for i in range(0, len(lista)):
		conc = conc + lista[i]
	print(conc)

def product(lista):
	pro = 1
	for i in range(0, len(lista)):
		pro = lista[i] * pro
	print(pro)

def fact(f):
	fact = f
	for i in range(1, f):
		f = f - 1
		fact = fact * f
	print(fact)

def reverse(list):
	list_n = list[:]
	#print(list_n)
	num = len(list_n)
	for item in list:
		num = num - 1
		list_n[num] = item
	print(list_n)

def min_f(parametros):
	minimo = 1
	lista = parametros[:]
	for i in range(0, len(lista)):
		for a in range(0, len(lista)):
			if lista[i] >= parametros[a]:
				minimo = parametros[a]
	print("bugado",minimo)

def cumul_sum(lista):
	lista_c = lista[:]
	for i in range(1, len(lista)):
		lista_c[i] = lista_c[i-1] + lista_c[i]
	print(lista_c)

def cumul_pro(produ):
	for i in range(1, len(produ)):
		produ[i] = produ[i-1] * produ[i]
	print(produ)
def unique_f(lista):
	lista_c = lista[:]
	for i in range(0, len(lista)):
		chave = 1
		for a in range(1, len(lista)-1):
			if lista_c[i] == lista[a]:
				chave = chave + 1
		if chave == 1:
			print(lista_c[i])
def dups(lista):
	lista_c = lista[:]
	var = ""
	for item in lista:
		count = 0
		for item_c in lista_c: 
			if item == item_c:
				count = count + 1
				if count > 1:
					var = item
		print(var)
def group(lista, size):
	tam = len(lista)
	resul = int(tam/size)
	print(resul)
	for i in range(0, tam, resul):
		c = lista[i:resul+i]
		print(c)

def lensort(lista):

	listagem = lista[:]
	i = 0
	new_list = []
	for item in lista:
		if len(lista) < len(listagem[i]):
			new_list[i] = lista
	print(new_list)
