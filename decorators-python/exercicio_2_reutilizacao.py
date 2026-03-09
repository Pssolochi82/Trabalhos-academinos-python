# Exercício 2 – Decorar Outra Função (Reutilização do Decorator)

def announce(f):
    def wrapper():
        print("Sobre o correr a função ...")
        f()
        print("Está feito a função.")
    return wrapper


@announce
def ola():
    print("Olá Mundo!")


@announce
def despedida():
    print("Até já!")


# Testes
ola()
despedida()
