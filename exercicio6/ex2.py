#Dado um set de frutas duplicadas de uma lista de compras, remova duplicados, adicione uma nova fruta com add() e verifique com in se "maçã" existe.
frutas = {"maçã", "banana", "laranja", "maçã", "uva"}
print("Frutas originais:", frutas)
frutas.remove("maçã")
print("Frutas após remover duplicados:", frutas)
frutas.add("pêra")
print("Frutas após adicionar pêra:", frutas)
if "maçã" in frutas:
    print("A fruta 'maçã' existe no set.")
else:
    print("A fruta 'maçã' não existe no set.")