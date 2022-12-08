idade = int(input("Digite uma idade:"))
soma = idade
contador = 0
lista = [idade]

while idade > 0:
    idade = int(input("Digite uma idade:"))
    soma = soma + idade
    soma2 = soma - idade
    contador +=  1

    if idade < 0:
        contador1 = contador + 1
        
        media = float ( soma2 / contador)
        #print(media)
        #print (soma2)
        print ("A média de idades é:",media)
        break