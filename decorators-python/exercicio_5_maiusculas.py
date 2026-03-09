# Exercício 5 – Decorator @maiusculas

def maiusculas(f):
    def wrapper(*args, **kwargs):
        resultado = f(*args, **kwargs)

        if isinstance(resultado, str):
            resultado = resultado.upper()
            print(resultado)

        return resultado
    return wrapper


@maiusculas
def mensagem():
    return "bom dia, mundo"


# Teste
mensagem()
