#Crie um dicionário onde as chaves são números e os valores são os quadrados desses números (por exemplo, 2:4, 3:9) para os números de 1 a 5.
quadrados = {i: i**2 for i in range(1, 6)}
print("Dicionário de quadrados:", quadrados)