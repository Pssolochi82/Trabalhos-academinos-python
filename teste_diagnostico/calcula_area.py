#Crie uma função chamada "calculaArea" que receba o raio de um círculo como parâmetro e retorne a área desse círculo (área= PI*raio^2). Utilize a constante PI(3.14f) para calcular a área.
def calculaArea(raio):
    PI = 3.14
    area = PI * (raio ** 2)
    return area
raio = float(input("Digite o raio do círculo: "))
area_circulo = calculaArea(raio)
print(f"A área do círculo com raio {raio} é: {area_circulo}")
