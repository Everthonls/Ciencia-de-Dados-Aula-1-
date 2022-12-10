ValorP = float(input("Digite o valor da prestação:"))
Tempo = int(input("Digite a quantidade de dias em atraso:"))
contador = 0
soma = 0

while ValorP != 0: 
    def ValorPagamento (ValorP, Tempo):
        multa = (ValorP * 3) / 100
        resultado1 = (1.001) ** Tempo
        resultado = (ValorP * resultado1) + multa
        return resultado

    M = round(ValorPagamento(ValorP, Tempo),2)
    print ("Total com juros a ser pago: R$",M)
    soma = round (soma + ValorPagamento(ValorP, Tempo),2)
    ValorP = float(input("Digite o valor da prestação:"))
    Tempo = int (input("Digite a quantidade de dias em atraso:"))
    contador = contador + 1
   

#while False:

contador = contador 
print("Relatório do dia!\n Quantidade de prestações:", contador, "\n Valor total das prestações: R$", soma)
