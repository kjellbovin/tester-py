# Kjell Bovin
#Definiera en funktion som sköter uträkningen av ränta på ränta samt returnerar en variabel - ci - avrundad till två decimaler
def compound_interest(cash, rate, time):
    a = cash * pow((1 + rate/100), time)
    ci = a - cash
    return round(ci, 2)

#Begär input från användaren
amount_cash = int(input('Hur mycket pengar har du idag: '))
yearly_rate = float(input('Ränta i procent: '))
periods = int(input('Antal år att räkna på: '))

#Returnera två resultat - dels den sammansätta räntan men också total summa efter ränta
print('\n---------------RESULTAT---------------')
print(f'\nSammansatt ränta efter {periods} år: {compound_interest(amount_cash, yearly_rate, periods)}')
print(f'\nTotalt efter {periods} år: {amount_cash + compound_interest(amount_cash, yearly_rate, periods)}')
