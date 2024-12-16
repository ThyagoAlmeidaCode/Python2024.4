print(20*"-")
print("Bem vindo ao jogo de adivinhação de números")
print(20*"-")
print("")
print("Você tem apenas 3 tentativas para adivinhar o número secreto.")

numero_secreto = 42
chute = int(input("Digite um número: "))
contador = 1
pontuacao = 100

while contador < 3:
    if chute == numero_secreto:
        print("Você acertou!")
        break
    else:
        pontuacao -= 10
        print("Você errou!")
        print("Você possui mais", 3 - contador, "tentativas.")
        print("Pontuação:", pontuacao)
        chute = int(input("Digite um número: "))
        contador += 1

