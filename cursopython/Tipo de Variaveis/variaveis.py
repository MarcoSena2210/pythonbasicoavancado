'''
Tipos de Dados
    str -string
    int -inteiro
    float -real/ponto flutuante
    bool - booleano/lógico

Nomeação de variáveis
Podemos nomear variáveis e tipos de dados de diversas formas:

Declarar as variáveis em uma única linha de comando;
Atribuir um valor à diversas variáveis;
Declarar usando uma Lista;
Combinar variáveis;
Operar com operadores matemáticos;
Muitos outros.



'''

# Tipos de Variaveis
Inteiro_Exemplo_1 = int ( 100 )
Inteiro_Exemplo_2 = 100

Flutuante_Exemplo_1 = 10.50
Flutuante_Exemplo_2 = float( 10.50 )

Palavra_Exemplo_1 = 'Qualquer Palavra'
Palavra_Exemplo_2 = str( 'Qualquer Palavra' )

Booleando_Exemplo_1 = True
Booleando_Exemplo_2 = False

print( Inteiro_Exemplo_1, Inteiro_Exemplo_2, '\n' )
print( Flutuante_Exemplo_1, Flutuante_Exemplo_2, '\n' )
print( Palavra_Exemplo_1, Palavra_Exemplo_2, '\n' )
print( Booleando_Exemplo_1, Booleando_Exemplo_2, '\n' )


#string: nome
nome ='Marco'
print(nome, type(nome))
print('Sena', type('Sena'))

#int :idade
print(55, type(55))

# altura : float
print(1.67, type(1.67))

# bool : maior de idade
#idade = 55



print(55 >= 18, type(55 >= 18) )


idade = False
if (55 >= 18):
    idade = True

print(idade,type(idade))

# Nomeando Variaveis | Exemplo 1
Laranja, Melão, Limão = 1, 2, 3
print( Laranja, Melão, Limão, '\n' )

# Nomeando Variaveis | Exemplo 2
Morango = Uva = Kiwi = 100
print( Morango, Uva, Kiwi, '\n' )

# Nomeando Variaveis | Exemplo 3
# Criando uma lista
Carros = ['VW', 'GM', 'Ford']

# Nomeando as variaveis com a lista
Marca_01, Marca_02, Marca_03 = Carros
print( Marca_03, '\n' )

# Combinando Variaveis | Exemplo 1
Nome = 'Odemir'
Sobrenome = 'Depieri'
Nome_Completo = Nome + ' ' + Sobrenome
print( Nome_Completo, '\n' )

# Combinando Variaveis | Exemplo 2
Dolar = 5.40
Imposto = 0.20
Valor_Liquido = Dolar - ( Dolar * Imposto )
print( Valor_Liquido )