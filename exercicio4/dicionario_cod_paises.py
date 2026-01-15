#Dado um dicionário que mapeia códigos de país para nomes (por exemplo, 'PT': 'Portugal'), verifique se um certo código está presente usando in.
paises = {"PT": "Portugal", "ES": "Espanha", "FR": "França"}
codigo_verificar = "PT"
if codigo_verificar in paises:
    print(f"O código {codigo_verificar} está no dicionário.")
else:
    print(f"O código {codigo_verificar} não está no dicionário.")