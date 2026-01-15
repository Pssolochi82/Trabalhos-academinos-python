#Converta uma string de e-mail para set de caracteres únicos, verifique com in se contém "@" e conte vogais únicas.
email = input("Digite um e-mail: ")
caracteres_unicos = set(email)
if "@" in caracteres_unicos:
    print("O e-mail contém '@'.")
else:
    print("O e-mail não contém '@'.")
vogais = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
vogais_no_email = caracteres_unicos.intersection(vogais)
print(f"As vogais únicas no e-mail são: {vogais_no_email}")
print(f"Número de vogais únicas no e-mail: {len(vogais_no_email)}")

