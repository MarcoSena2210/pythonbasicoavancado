
nome = 'Selma'

idade =18
altura = 1.80
e_maior = idade >= 18
data_atual = 2022

print('nome   :', nome)
print('idade  :',  idade)
print('altura :', altura)
print('e_maior:', e_maior)
peso = 80
ano_atual = 2022
ano_nascimento = 1990
idade = ano_atual - ano_nascimento

imc = peso / (altura ** 2)
print(nome, ' tem ', idade, ' anos de idade e seu imc é ', imc   )

# Usando string formatada

print(f'{nome}, tem ,{idade}, anos de idade e seu imc é  {imc}' )