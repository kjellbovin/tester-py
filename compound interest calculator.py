def compound_interest(cash, rate, time):
    a = cash * pow((1 + rate/100), time)
    ci = a - cash
    return round(ci, 2)

amount_cash = int(input('Hur mycket pengar har du idag: '))
yearly_rate = int(input('Ränta: '))
periods = int(input('Antal år att räkna på: '))

print('\n---------------RESULTAT---------------')
print(f'\nSammansatt ränta efter {periods} år: {compound_interest(amount_cash, yearly_rate, periods)}')
print(f'\nTotalt efter {periods} år: {amount_cash + compound_interest(amount_cash, yearly_rate, periods)}')