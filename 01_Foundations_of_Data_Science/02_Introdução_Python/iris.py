f = open('Arquivos/iris.csv', 'r')
lines = f.readlines()
#print(lines)
var = []
dock = []
for line in lines:
	#print(line)
	line = line.strip('\n')
	var = line.split(',')
	dock.append(var)
print(dock[0][0], '|', dock[0][1],'|')
print('*'* 100)
print(dock[1][0], '         |', dock[1][1], '        |')
print('-'* 100)
print(dock[2][0], '         |', dock[2][1], '          |')
print(dock[0])
print(dock[1])
print(len(dock))
