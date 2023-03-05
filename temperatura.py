# Pergunta ao usuário qual a unidade de temperatura e o valor da temperatura
unidade = input("Digite a unidade de temperatura (C, F, K): ")
temperatura = float(input("Digite o valor da temperatura: "))

# Converte a temperatura para Celsius
if unidade == "F":
    celsius = (temperatura - 32) * 5/9
elif unidade == "K":
    celsius = temperatura - 273.15
else:
    celsius = temperatura

# Converte a temperatura para Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Converte a temperatura para Kelvin
kelvin = celsius + 273.15

# Exibe os resultados das conversões
print("Celsius: ", celsius)
print("Fahrenheit: ", fahrenheit)
print("Kelvin: ", kelvin)


# Este algoritmo começa perguntando ao usuário qual a unidade de temperatura e o valor da temperatura. Em seguida, ele converte a temperatura para Celsius, se necessário, usando um if-elif-else. Em seguida, ele converte a temperatura para Fahrenheit e Kelvin e exibe os resultados das conversões.
