#Crie um dicionário que mapeia meses (1 a 12) para o número de dias. Peça um número de mês ao utilizador e apresente o total de dias.
meses_dias = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}
mes = int(input("Digite o número do mês (1 a 12): "))
if mes in meses_dias:
    print(f"O mês {mes} tem {meses_dias[mes]} dias.")
else:
    print("Mês inválido.")