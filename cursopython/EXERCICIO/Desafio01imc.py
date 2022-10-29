"""
 Obter o ano de nascimento da pessoa (Baseado no ano atual, calcular a idade
 Obter o IMC da Pessoa com 2 casas decimais (peso e na altura da pessoa)
 Exibir um texto com os valores na tela usando F-Strings (Com chaves)
 IMC = peso / (altura ** 2))
"""
ano_atual = 2022

nome = input('Informe seu nome :')
ano_nascimento = int(input('Informe seu ano de nascimento:'))
idade = ano_atual - ano_nascimento
peso = float(input('Informe seu peso :'))
altura = float(input('Informe sua altura :'))
imc = peso / (altura ** 2)
print( f"{nome} nasceu em {ano_nascimento},seu peso é {peso} e altura é {altura} tem {idade} anos" )
print( f" seu imc é {imc:.2f}")
