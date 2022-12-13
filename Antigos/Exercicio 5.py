#Exemplo
#Salário Bruto = R$ 5000,00
#Desconto do INSS = R$ 550,00 (11% de R$ 5000,00)
#Desconto do IR = R$ 667,50 (15% de R$ 4450,00)
#Salário Líquido = 5000 - (550 + 667,50) = 3782,50


SalBruto = float(input("Digite o valor do seu salário bruto:"))
def calculaSalario (SalBruto):
    resultado = SalBruto - ((11 * SalBruto) / 100)
    SalLiq = resultado - ((15*resultado)/100)
    return SalLiq
num1 = calculaSalario(SalBruto)

print("O seu salário liquido é: R$",num1)

