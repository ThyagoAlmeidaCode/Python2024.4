""" 
O que é uma estrutura de repetição?
    é algo que acontece rotineiramente, ou seja, algo que se repete
"""
print("Repetição com While (Equanto)")
#Cuidado ao usar o While, pois podemos gerar um loop infinito
#Para controlar o while utilizamos um contador

contador = 0

while contador <= 10:
    print(f"Vota ao mundo {contador}")
    """ contador = contador + 1 """ #Incremento
    contador += 1

print(15*"-")

print("For - Lista")

#Cria uma lista:
caixa_frutas = ["Maçã","Banana","Pera","Goiaba"]

for fruta in caixa_frutas:
    print(f"A fruta é {fruta}")

print("For - Simples")
for conta_for in range(0, 10):
    print(f"contagem {conta_for}")

print("For - ate 10 range(0-11)")
for conta_for in range(0, 11):
    print(f"contagem {conta_for}")

print("For - Simples range(0, 10+1)")
for conta_for in range(2, 10+1):
    print(f"contagem {conta_for}")