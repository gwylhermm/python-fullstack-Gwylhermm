"""
Conversor de temperatura.

Converte uma temperatura em graus Celsius para Fahrenheit e Kelvin
e exibe os três valores formatados.
"""

# Temperatura em graus Celsius (float)
celsius = 36.5

# Fahrenheit: F = (C × 9/5) + 32
fahrenheit = (celsius * 9 / 5) + 32

# Kelvin: K = C + 273.15
kelvin = celsius + 273.15

# Exibe os três valores com uma casa decimal
print(f"Celsius: {celsius:.1f}°C")
print(f"Fahrenheit: {fahrenheit:.1f}°F")
print(f"Kelvin: {kelvin:.2f} K")