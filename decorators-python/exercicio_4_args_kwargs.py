# Exercício 4 – Decorator com *args e **kwargs

def announce(f):
    def wrapper(*args, **kwargs):
        print("[INFO] Iniciando execução da função...")
        resultado = f(*args, **kwargs)
        print("[INFO] Execução concluída com sucesso!")
        return resultado
    return wrapper


@announce
def cumprimentar(nome):
    print(f"Olá, {nome}!")


# Teste
cumprimentar("Ana")
