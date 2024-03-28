cromossomo = input("Digite o cromossomo: ")
posição = int(input("Digite a posição: "))
BRCA17 = cromossomo == "chr17"
posicaoBRC17 = (41196312 <= posição <= 41277500)

if BRCA17 and posicaoBRC17:
    print("Resposta:")
    print("Sim")
else:
    print("Resposta:")
    print("Não")
