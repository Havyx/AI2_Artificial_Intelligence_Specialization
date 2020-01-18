def alo():
	print("Hello world")

def maximo(a, b):
	if a > b:
		print("Maior e: {} ".format(a))
	else: print('maior e: {}'.format(b))

def errorhand(a):
	try:
		float(a)

	except ValueError:
		print("O caractere nao e numero")
		return False

	return True

def fizz_buzz(a):
	resul = errorhand(a)
	if resul == True:
		div = a % 3
		div5 = a % 5
		if div == 0 and div5 == 0:
			print("FizzBuzz")
		else:
			if div!= 0:
				print("Nao e divisivel por 3")
			else:
				print("Fizz")
		#print(tip)
			if div5 != 0:
				print("Nao e divisivel por 5")
			else:
				print("Buzz")
def speed(s):
	pontos = 0
	if s < 70:
		print("OK")
	else:
		resul = s - 70
		demerit = resul / 5
		print(int(demerit))
		for i in range(1, int(demerit) +1):
			print(resul)
			if resul >= 0:
				pontos = pontos + 1
			resul = resul - 5

		print("A quantidade de potnos retirada foi {}".format(pontos))

def shownumbers(limit):

	for i in range(1,limit + 1):
		a = i % 2
		if a == 0:
			print("EVEN")
		else:
			print("ODD")
def summult(limit):
	soma3 = 0
	soma5 = 0
	for i in range(3, limit+1, 3):
		soma3 = soma3 + i

	for i in range(5, limit+1, 5):
		soma5 = soma5 + i

	return(soma3 + soma5)

def show_stars(stars):
	asd = "*"
	while stars > 0:
		print(asd)
		asd = asd + "*"
		stars -= 1
def prime(limit):
	b = 0
	for i in range(1, limit + 1):
	
		print("vou terminar essa depois")
