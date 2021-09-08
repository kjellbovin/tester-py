#Definiera funktion för att räkna ut compound interest
def compound_interest(cash, rate, time):
    a = cash * pow((1 + rate/100), time)
    ci = a - cash
    return round(ci, 2)

#Begär data från användaren
amount_cash = int(input('Hur mycket pengar har du idag: '))
yearly_rate = int(input('Ränta: '))
periods = int(input('Antal år att räkna på: '))

#Returnera resultatet
print('\n---------------RESULTAT---------------')
print(f'\nSammansatt ränta efter {periods} år: {compound_interest(amount_cash, yearly_rate, periods)}')
print(f'\nTotalt efter {periods} år: {amount_cash + compound_interest(amount_cash, yearly_rate, periods)}')