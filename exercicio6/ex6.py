#Crie um tuplo imutável de coordenadas (x, y, z); faça desempacotamento em três variáveis e verifique se z é positivo com in num set de valores válidos.
coordenadas = (10, 20, 30)
x, y, z = coordenadas
valores_validos = {10, 20, 30}
if z in valores_validos and z > 0:
    print("z é positivo e está em valores válidos.")
else:
    print("z não é positivo ou não está em valores válidos.")