"""
Carga de caminhão: divisão inteira e resto.

Calcula quantas caixas completas cabem em um caminhão com
capacidade de 850 kg e quanto peso sobra sem completar outra caixa.
"""

# Capacidade total do caminhão em kg
capacidade = 850

# Peso de cada caixa em kg
peso_caixa = 32

# Divisão inteira (//): quantas caixas completas cabem
caixas_completas = capacidade // peso_caixa

# Resto da divisão (%): peso que sobra e não completa uma caixa
peso_restante = capacidade % peso_caixa

# Exibe os resultados com mensagens claras
print(f"Caixas completas que cabem no caminhão: {caixas_completas}")
print(f"Peso restante que não completa uma caixa: {peso_restante} kg")