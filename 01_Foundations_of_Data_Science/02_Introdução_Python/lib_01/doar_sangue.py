import sys, math

def isnumber(num, num2):
        try:
                float(num)
                float(num2)

        except ValueError:
                print("Algum dos caracteres digitados nao foi reconhecido como numero")
                return False

        return True

def check(n, n2):
        if(n > n2):
                print("O numero {} e menor que {}".format(n2,n))
        else:
                print("O numeto {} e menor que {} ".format(n, n2))

def doar_sangue():
	idade = int(input("Digite a sua idade: "))
	peso = float(input("quanto vc pesa? Resposta: "))
	descan = int(input("Quantas horas de descanso? Resposta: "))

	if  16 <= idade <= 69:
		if peso > 50:
			if descan > 6:
				print("Voce pode doat sangue.")
			else: print("voce nao dormiu o suficiente")
		else: print("voce nao pesa o suficiente")
	else: print("sua idade nao permite que voce doe sangue")

def raiz_q():

	a = int(input("digite a: "))
	b = int(input("digite b: "))
	c = int(input("digite c: "))

	delta = (b^2)-(4*a*c)
	print(delta)
	if delta == 0:
		print("uma raiz real")
	if delta > 0:
		print("Ha duas raizes reais")
	if delta < 0:
		print("nao ha raizes reais")
def somar():
	n1 = int(input("Digite n1: "))
	n2 = int(input("Digite n2: "))
	resul = isnumber(n1, n2)
	if resul == True:
		somado = n1 + n2
		if somado > 20:
			somado = somado + 8
			print("Resultado: {}".format(somado))
		if somado <= 20:
			somado = somado - 5
			print("Resultado: {}".format(somado))
def numero():
	n1 = int(input("Digite o numero: "))
	if n1 >= 0:
		print(math.sqrt(n1))
	if n1 < 0:
		print(math.pow(n1,2))
def mes():
	lista_m = {1: 'Janeiro', 2: 'Fevereiro', 3: 'Marco', 4: 'Abril', 5: 'Maio', 6: 'Junho', 7: 'Julho', 8: 'Agosto', 9:'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'}
	a = int(input("Digite o valor do mes: "))
	if 1 <= a <= 12:
		resul =  lista_m[a]
		print(resul)
	else: print("Nesse planeta nao existe esse mes")
