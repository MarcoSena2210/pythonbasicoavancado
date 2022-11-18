"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
i=inicio
f=fim, geralmente o final não é incluído.
p=passo (de quantos em quantos ele vai pular)
Obs.: a função len retorna a qtd 
de caracteres da str
"""
variavel = 'Olá mundo'
print(variavel[::-1])
print(variavel[4:8])
print(variavel[4:]) #Até o final da string
print(variavel[0:4]) #Do zero até o 4 -1
print(variavel[::-1]) #causa o efeito de inversão da palavra
#Passo de 2  em e
print(variavel[0:9:2])