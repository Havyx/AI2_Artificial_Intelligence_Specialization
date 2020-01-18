#!/usr/bin/python
#chmod a+x exercicios_python.py
# chmod a+x exercicios_python.py
#!/home/savio/miniconda3/envs/env01/bin/python

def hello():
	i = 0
	while i < 4:
		print("hello world!/n")
		i = i + 1
hello()

print(1 + 2)

x = 4
y = x + 1
x = 2
print(x,y)

x, y = 2, 6
x, y = y, x + 2
print(x, y)

a, b = 2, 3
c = 0
c, b = a, c + 1
print(a, b, c)

numcalls = 0
def square(x):
	global numcalls
	numcalls = numcalls + 1
	return x * x
print(square(5))
print(square(2*5))

x = 1
def f():
	return x
print(x)
print(f())

x = 1
def f():  
	x=2
	return x
print(x)
print(f())
print(x)

x = 1
def f():
	global x
	y = x
	x = 2
	return x + y
print(x)
print(f())
print(x)

x = 2
def f(a):
        x = a * a
        return x
y = f(3)
print(x,y)

def count_digits(num):
	quant = len(str(num))
	return quant
quant = count_digits(5)
print("Quantidade de caracteres: {}".format(quant))
quant = count_digits(12345)
print("Quant: {}".format(quant))

def istrcmp(a, b):
	a = a.lower()
	b = b.lower()
	if a == b:
		print("Sao iguais")
	else:
		print("nao sao iguais")

istrcmp('python', 'Python')
istrcmp('LaTeX', 'Latex')
istrcmp('a', 'b')

