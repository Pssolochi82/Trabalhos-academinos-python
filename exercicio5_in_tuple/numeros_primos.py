# Crie um programa que calcule os números primos compreendidos no intervalo 1000 e 2000. Deve usar uma função chamada “primos”, que deverá ser o modulo de um ficheiro principal, cujo nome será “primo.py”. O nome do ficheiro externo (modulo), deve ter o nome “funções.py”.

def primos(inicio, fim):
    numeros_primos = []
    for num in range(inicio, fim + 1):
        if num > 1:  # Números primos são maiores que 1
            for i in range(2, int(num**0.5) + 1):
                if (num % i) == 0:
                    break
            else:
                numeros_primos.append(num)
    return tuple(numeros_primos)
if __name__ == "__main__":
    inicio = 1000
    fim = 2000
    primos_encontrados = primos(inicio, fim)
    print(f"Números primos entre {inicio} e {fim}:")
    print(primos_encontrados)
    