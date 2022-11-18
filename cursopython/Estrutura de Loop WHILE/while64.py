"""
Iterando strings com while
"""
#       012345678910
nome = 'Luiz Otávio'  # Iteráveis
#      1110987654321
tamanho_nome = len(nome) 
print(nome)
print(tamanho_nome)
print(nome[3])

nova_string = ''
i = 0 
while(i < tamanho_nome ):
    letra = nome[i]+ '*'
    nova_string += letra   
    i += 1

print(nova_string)    