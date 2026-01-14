#Escreva um programa que solicite ao utilizador que escreva um número e, em seguida, imprima a tabuada desse número. Utilize a instrução “While”.
num = int(input("Digite um número para ver a tabuada: "))
contador = 1
while contador <= 10:
    resultado = num * contador
    print(f"{num} x {contador} = {resultado}")
    contador += 1
    