"""
 deve iniciar com letra , pode conter numeros , separar _, letras minusculas
 não pode iniciar com numero
"""
"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade = 61  # velocidade atual do carro
local_carro = 100  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

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
if (imc < 18.5):
    print('sua classificação é MAGRESA')
elif (imc >= 18.5 and  imc <=24.9):
    print('sua classificação é NORMAL')
elif (imc >= 25.0 and  imc <=29.9):
    print('sua classificação é SOBREPESO')
elif (imc >= 30.0 and  imc <=34.9):
    print('sua classificação é OBESIDADE')
elif (imc >= 35.0 and  imc <=39.9):
    print('sua classificação é OBESIDADE II')
elif (imc >= 40.0):
    print('sua classificação é OBESIDADE III')

