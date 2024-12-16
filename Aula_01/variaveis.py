""" Uma caixinha onde guardamos nossas coisas """
""" 
    Principais tipos de Variáveis do python
        >int - Numero/Valores inteiros
        >float - Numeros/Valores fracionarios
        >String - Palavras, frases ou caracter
        >Booleano - Verdadeiro ou falso
        >list - Cria uma lista[Array] ex: [1,2,3,4]
        >tuplas - Sememlhante a lista porém seu conteudo é imutavel ex: (1,2,3)
"""
#Declarando Variáveis
curso = "Senac"
valor = 10
valor_dois = 3.5
verdade = True
mentira = False
animais = ["Leão", "Vaca", "Cachorro"]
numeros = (1,2,3,4)

#O type permite ver o tipo da variável
print("O tipo é: ", type(curso))

""" Desafio """
#Crie um programa que solicite o time de futebol do usuário. 
#O programa deve gravar o nome do time em uma varável e em seguida exibir no terminal
nome = "Thyago Almeida"
seu_time = input("Qual seu time de Futebol? ") 
print("Seu nome:é {} e seu time é: {}".format(nome,seu_time) )

#Formas de saída da informação
#Primeira Forma
print("Primeira Forma: ", seu_time)

#Segunda Forma
print(f"Segunda Forma:{nome} {seu_time}")

#Terceira Forma
print("Terceira Forma: {}".format(seu_time))