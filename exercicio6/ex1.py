#Crie um tuplo com temperaturas diárias da semana e use in para verificar se uma temperatura específica ocorreu; calcule depois a média com sum() e len().
temperaturas = (20, 22, 18, 25, 23, 19, 21)
temp_especifica = 23
if temp_especifica in temperaturas:
    print(f"A temperatura {temp_especifica} ocorreu na semana.")
else:
    print(f"A temperatura {temp_especifica} não ocorreu na semana.")
media = sum(temperaturas) / len(temperaturas)
print(f"A média das temperaturas é: {media}")