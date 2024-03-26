brca1 = str("chr17")
cromossomo = str(input("Digite o cromossomo: "))
intervalo = int(input("Digite a posição: "))
if cromossomo == brca1 and 41196312 <= intervalo <= 41277500 :
    print("Resposta:")
    print("Sim")
else:
    print("Resposta: ")
    print("não")
