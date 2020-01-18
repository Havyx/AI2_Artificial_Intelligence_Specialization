def carros():

	a=[]
	n = int(input("Digite quantas vezes voce quer add: "))
	for i in range(1,n+1):
		var1 = input("Qual o carro p/ add a lista: ")
		a.append(var1)
		#print(var1)
	return a

def imp(a):
	#lista=['leleo', 'Andre', 'Cristiano', 'Daniel','Savio', 'Alessandra', 'Wana', 'Lucas', 'Rafael', 'Jessica', 'Leticia', 'Alexandre', 'Gabriel', 'Lazaro', 'Bruna', 'Vitor', 'Harrison', 'grabiela', 'Duan', 'Felipe']
	num = len(a)
	print(a)
	filtrar = str(input("Digite letra: "))
	for i in range(0, num):
		nome = a[i]
		if nome[0] == filtrar:
			print(nome)
