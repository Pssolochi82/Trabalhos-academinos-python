#Crie um pequeno sistema de login com um dicionário que guarda utilizadores e palavras-passe. Leia um utilizador e palavra-passe e verifique se a combinação está correta usando in e comparação de valores.
utilizadores = {
    "ana": "1234",
    "bruno": "abcd",
    "carlos": "efgh"
}
utilizador = input("Digite o nome de utilizador: ")
palavra_passe = input("Digite a palavra-passe: ")
if utilizador in utilizadores and utilizadores[utilizador] == palavra_passe:
    print("Login bem-sucedido.")
else:
    print("Utilizador ou palavra-passe incorretos.")