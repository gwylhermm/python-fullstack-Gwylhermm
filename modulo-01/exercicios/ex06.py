"""
Explorando tipos de dados com type().

Cria seis variáveis de tipos diferentes (int, float, str, bool,
NoneType e str vazia) e exibe o valor e o tipo de cada uma.
"""

# Número inteiro: ano atual
ano = 2026

# Número de ponto flutuante: temperatura em Celsius
temperatura = 28.5

# String: nome de uma cidade
cidade = "Boa Vista"

# Booleano: indica se está chovendo
chovendo = True

# Valor especial None: representa "nenhum valor" (ainda sem previsão)
previsao = None

# String vazia: continua sendo str, mesmo sem nenhum caractere
vazia = ""

# Exibe o valor e o tipo de cada variável no formato "valor → tipo"
print(ano, "→", type(ano))
print(temperatura, "→", type(temperatura))
print(cidade, "→", type(cidade))
print(chovendo, "→", type(chovendo))
print(previsao, "→", type(previsao))
print(repr(vazia), "→", type(vazia))