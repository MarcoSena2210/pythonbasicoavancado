"""
    Formatando valores com modificadores
'
    :s  - Texto (strings)
    :d  - Inteiro (int)
    :f  - Números de ponto flutuante (float)
    :.(NUMERO)f - Quantidade de casas decimaois (float)
    :(CARACTERE) (> ou < ou ^^) (QUANTIDADE) (TIPO -s, d ou f))
    > -esquerda
    < -Direita
    ^ -Centro
"""
num_1 = 10
num_2 = 3
divisao = 10 / 3
print(divisao)                   # Retorna 3.3333333333333335
print('{:.2F}'.format(divisao))  # Retorna 3.33

#Formatando string
nome = "Marco Sena"
nome_formatado_esquerda = '{:@>20}'.format(nome)
nome_formatado_centro = '{:*^20}'.format(nome)
nome_formatado_direita = '{:@<20}'.format(nome)
print(nome_formatado_esquerda) #Retorna @@@@@@@@@@Marco Sena
print(nome_formatado_centro)   # Retorna *****Marco Sena*****
print(nome_formatado_direita)  # Retorna Marco Sena@@@@@@@@@@

nome_formatado = '{n}'.format(n=nome)
print(nome_formatado)   # Retorna Marco Sena
nome_formatado1 = '{n} x {n}'.format(n=nome)
print(nome_formatado1)  # Retorna Marco Sena x Marco Sena

nome_formatado3 = '{n:0<25}'.format(n=nome)
print(nome_formatado3)    # Retorna Marco Sena000000000000000


usuario = 'fulano de tal'
print(usuario.lower())  # tudo minusculo
print(usuario.upper())  # tudo maiusculo
print(usuario.title())  # Primeira letras maiuscula

a = 'AAAAA'
b = 'BBBBBB'
c = 1.1
string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'
formato = string.format(
    nome1=a, nome2=b, nome3=c
)

print(formato)
nome = "Luiz"
idade = 23
formato = '{1} tem {0} anos'
print(formato.format(nome, idade))