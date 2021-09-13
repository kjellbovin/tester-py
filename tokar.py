#Definiera en funktion för att räkna ut compound interest
def compound_interest(cash, rate, time):
    a = cash * pow((1 + rate/100), time)
    ci = a - cash
    return round(ci, 2)

#Begär data från användaren. Returnera ett felmeddelande om datatypen är felaktig.
while True:
    try:
        amount_cash = int(input('Hur mycket pengar har du idag: '))
        break
    except ValueError:
        print('__________________________________________\n')
        print(' Felaktig datatyp. Använd enbart siffror. \n')
        print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\n')
        continue
while True:
    try:
        yearly_rate = int(input('Ränta: '))
        break
    except ValueError:
        print('__________________________________________\n')
        print(' Felaktig datatyp. Använd enbart siffror. \n')
        print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\n')
        continue
while True:
    try:
       periods = int(input('Antal år att räkna på: '))
       break
    except ValueError:
        print('__________________________________________\n')
        print(' Felaktig datatyp. Använd enbart siffror. \n')
        print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\n')
        continue

#Returnera resultatet
print('\n---------------RESULTAT---------------')
print(f'\nSammansatt ränta efter {periods} år: {compound_interest(amount_cash, yearly_rate, periods)}')
print(f'\nTotalt efter {periods} år: {amount_cash + compound_interest(amount_cash, yearly_rate, periods)}')