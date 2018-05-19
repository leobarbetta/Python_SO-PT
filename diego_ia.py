from random import randint

falas = ["Opa!", "Qual o prazo?", "Ve lá com o cara!", "Qual a dificuldade?", "É tipo wi-fi só que com cabo.", "Já está pronto?"]

print("Bem vindo a Diego's IA, vamos conversar?")
print("Para sair escreva 0")

while True:
    entrada = input("Diga alguma coisa: ")
    if(entrada == "0"):
        break
    index_fala = randint(0, 5)
    print(falas[index_fala])

