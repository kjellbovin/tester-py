#Definiera en funktion för att räkna ut compound interest utifrån argumenten cash, rate och time
#Returnerar variabeln ci avrundat till två decimaler
def compound_interest(cash, rate, time):
    a = cash * pow((1 + rate/100), time)
    ci = a - cash
    return round(ci, 2)

#Definiera en funktion som tar in två argument: user_message samt data_type
#Om datatypen som matas in inte stämmer överrens med argumentet data_type returneras ett felmeddelande.
def input_type_check(user_message:str, data_type):
    while True:
        try:
            input_value = data_type(input(user_message))
            break
        except ValueError:
            print('__________________________________________\n')
            print(' Felaktig datatyp. Använd enbart siffror. \n')
            print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\n')
            continue
    return input_value

#Begär data från användaren genom att skapa en variabel som hänvisar till funktionen input_type_check.
amount_cash = input_type_check(user_message='Hur mycket pengar har du idag: ', data_type=float)
yearly_rate = input_type_check(user_message='Ränta i procent: ', data_type=float)
periods = input_type_check(user_message='Antal år att räkna på: ', data_type=float)

'''while True:
    try:
        amount_cash = float(input('Hur mycket pengar har du idag: '))
        break
    except ValueError:
        print('__________________________________________\n')
        print(' Felaktig datatyp. Använd enbart siffror. \n')
        print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\n')
        continue
while True:
    try:
        yearly_rate = float(input('Ränta: '))
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
'''

#Framställning av resultatet
print('\n---------------RESULTAT---------------')
print(f'\nSammansatt ränta efter {periods} år: {compound_interest(cash=amount_cash, rate=yearly_rate, time=periods)}')
print(f'\nTotalt efter {periods} år: {amount_cash + compound_interest(cash=amount_cash, rate=yearly_rate, time=periods)}')