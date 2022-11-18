usuario = input('Digite seu nome ')
qtd_caracteres = len(usuario)
print(f'O nome {usuario} digitado tem a {qtd_caracteres} caracteres, seu tipo é {type(usuario)} ' )

#Pode ser usado para fazer a som
string1 ="Luis "
string2 ='Maria'
print('o total de caracteres é ',len(string1+string2))

# Porem se string 2 receber um valor  string vai funcionar, exemplo é digitado 12345
string2 = input ('Digite qualquer coisa ')  # Digite 123456
print(len(string2))


# Isso dará erro porque o len não conta variaveis do tipo numerica
string2 =123456
print(len(string2))

