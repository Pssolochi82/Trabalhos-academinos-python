#Faça um programa que crie uma lista com 5 tipos de frutas e a seguir execute as seguintes tarefas:
#a. Liste a lista
#b. Insira uma nova fruta
#c. Liste a lista
#d. Ordene a lista
#e. Liste a lista
#f. Elimine um elemento da lista
#g. Liste a lista
#h. Mostre somente o 2o elemento da lista
#i. Imprima caracter a caracter a terceira fruta da lista

# Criando a lista com 5 tipos de frutas
frutas = ["maçã", "banana", "laranja", "uva", "manga"]
# a. Liste a lista
print("Lista inicial de frutas:", frutas)   
# b. Insira uma nova fruta
nova_fruta = "abacaxi"
frutas.append(nova_fruta)
# c. Liste a lista
print("Lista após adicionar nova fruta:", frutas)
# d. Ordene a lista
frutas.sort()
# e. Liste a lista
print("Lista ordenada de frutas:", frutas)
# f. Elimine um elemento da lista
fruta_a_remover = "banana"
if fruta_a_remover in frutas:
    frutas.remove(fruta_a_remover)
# g. Liste a lista
print("Lista após remover uma fruta:", frutas)
# h. Mostre somente o 2o elemento da lista
if len(frutas) >= 2:
    print("O 2º elemento da lista é:", frutas[1])
# i. Imprima caracter a caracter a terceira fruta da lista
if len(frutas) >= 3:
    terceira_fruta = frutas[2]
    print("Caracteres da terceira fruta:")
    for char in terceira_fruta:
        print(char)
            