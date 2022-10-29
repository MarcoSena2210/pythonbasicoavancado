"""
Python é uma linguagem de programação orientada a objetos.

Quase tudo em Python é um objeto, com suas propriedades e métodos.

Uma classe é como um construtor de objetos, ou um "projeto" para criar objetos.
"""
class Pessoa:

  # Metodo Construtor
  def __init__(self, Nome, Idade):
    self.Nome = Nome
    self.Idade = Idade

  def Boas_Vindas(self):
    print('Olá seja benvindo: ', self.Nome)

  def Recusado(self):
    print('Seu acesso foi recusado!')

  # Função
  def Maior_Idade(self):
    if self.Idade >= 18:
      print('Usuário é maior de idade')
      self.Boas_Vindas()
    else:
      print('Usuário é menor de Idade')
      self.Recusado()

Pessoa('fulano',25).Boas_Vindas()
