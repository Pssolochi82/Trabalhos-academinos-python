#Crie uma função que se chame “CalcularPromocao” e que retorne um float,dado o salário a função deve retornar o valor do salário + 10% se o salário for inferior a 700 euros, caso seja igual ou superior a 700 euros deve adicionar 5% apenas.
def CalcularPromocao(salario):
    if salario < 700:
        salario += salario * 0.10
    else:
        salario += salario * 0.05
    return salario
salario_atual = float(input("Digite o salário atual: "))
novo_salario = CalcularPromocao(salario_atual)
print(f"O novo salário após a promoção é: {novo_salario}")
