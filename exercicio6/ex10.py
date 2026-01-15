#Crie um tuplo de palavras de uma senha; converta para set, remova vogais e verifique se a senha original tem pelo menos 3 consoantes únicas com in.
senha = ("segura", "senha", "complexa")
senha_set = set(senha)
vogais = {"a", "e", "i", "o", "u"}
consoantes = senha_set - vogais
if len(consoantes) >= 3:
    print("A senha tem pelo menos 3 consoantes únicas.")
else:
    print("A senha não tem pelo menos 3 consoantes únicas.")