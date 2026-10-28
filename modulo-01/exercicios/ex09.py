"""
Boas-vindas personalizada.

Solicita o nome e a idade do usuário, calcula o ano de nascimento
aproximado e exibe uma mensagem de boas-vindas.
"""

# Ano atual (usado para estimar o ano de nascimento)
ano_atual = 2026

# Solicita o nome; input() retorna sempre uma string
nome = input("Qual é o seu nome? ")

# Solicita a idade e converte para int para poder fazer cálculos
idade = int(input("Qual é a sua idade? "))

# Ano de nascimento aproximado: ano atual menos a idade
ano_nascimento = ano_atual - idade

# Exibe a mensagem no formato pedido
print(f"Olá, {nome}! Você tem {idade} anos e nasceu por volta de {ano_nascimento}.")