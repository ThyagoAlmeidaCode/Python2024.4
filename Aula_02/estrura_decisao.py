""" 
Estrturas de decisão

Classificação
    >Simples
    >Composta
    >Encadeada
    >Aninhadas

Operadores: 
    == (igual a)
    != (diferente de)
    < (Menor que)
    > (Maior que)
    <= (Menor igual a)
    >= (Maior igual a)

"""
print("Simples - é dada por uma única decisão")
idade = 18
if idade >= 18:
    print("Maior de idade")

print(15*"-")

print("Composta - é dada por uma unica decisão e uma resposta padrao")

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")

print(15*"-")

print("Encadeada - é dada por mais de uma decisão em uma resposta padrão")

if idade >=18:
    print("Maior de idade")
elif idade <= 18:
    print("Menor de idade")
else:
    print("Você é extraterrestre!")

print("Aninhada - Possui uma estrura de decisão dentro da outra")

classificacao = 16
ingresso = False

if classificacao >= 16:
    if ingresso == True:
        print("Você pode assistir ao filme")
    else:
        print("Você não pode assitir ao filme")
else:
    print("Você não pode assitir ao filme")


