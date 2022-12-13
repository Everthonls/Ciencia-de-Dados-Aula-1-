HoraInicio = int(input("Indique a hora, na configuração 00 à 23, que o jogo começou:"))
MinIncio = int(input("Indique o minuto, na configuração 00 à 59, em que o jogo começou:"))
HoraFinal = int(input("Indique a hora, na configuração 00 à 23, que o jogo finalizou:"))
MinFinal = int(input("Indique o minuto, na configuração 00 à 59, em que o jogo finalizou:"))


if HoraInicio < HoraFinal:
    HoraTotal = HoraFinal - HoraInicio
if MinIncio < MinFinal:
    MinTotal = MinFinal - MinIncio
if MinFinal < MinIncio:
    MinTotal = MinIncio - MinFinal 
if HoraInicio > HoraFinal: 
    HoraTotal = (24 - HoraInicio) + HoraFinal

print(" O jogo durou", HoraTotal, "hora(s)", MinTotal, "minuto(s)")      

