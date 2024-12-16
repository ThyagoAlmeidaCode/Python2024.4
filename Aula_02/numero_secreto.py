#Guarda o numero secreto
numero_secreto = 20

#Solicta o valor ao usuario e guarda dentro da variável
palpite = int(input("Informe seu palpite: "))   

#Estrutura de decisão para decidir
if palpite == numero_secreto:
    print("Parabéns! Você acertou")
elif palpite > numero_secreto:
    print("Você errou, o seu palpite é maior que o numero secreto!")
elif palpite < numero_secreto:
    print("Você errou, seu papite é menor que o numero secreto")
else:
    print("Valor desconhecido. Jogo encerrado")