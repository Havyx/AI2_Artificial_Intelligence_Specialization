#!/home/savio/miniconda3/envs/env01/bin/python

import sqlite3
conexao = sqlite3.connect('db01.db')

c = conexao.cursor()

#create table
c.execute('''CREATE TABLE hub(nome, formacao, outros)''')
c.execute("INSERT INTO hub VALUES('Savio','Eng. Mec.', '@havyx')")

conexao.commit()
conexao.close()

