#Joel

#Definiera en funktion som sköter uträkningen av ränta på ränta samt returnerar en variabel - ci - avrundad till två decimaler
def compound_interest(cash, rate, time):
    a = cash * pow((1 + rate/100), time)
    ci = a - cash
    return round(ci, 2)

#Begär input från användaren

try:
    amount_cash = float(input('Hur mycket pengar har du idag: '))
#loop som upprepar frågan tills man svarar korrekt
except ValueError:
    while True:
        try:
            amount_cash = float(input('Beloppet måste skrivas i siffror, ex 17.55: '))

        except ValueError:
            pass
        else:
            break

try:
    yearly_rate = float(input('Ränta i procent: '))

except ValueError:
    while True:
        try:
            yearly_rate = float(input('Beloppet måste skrivas i siffror, ex 17.55: '))

        except ValueError:
            pass
        else:
            break

try:
    periods = float(input('Antal år du vill spara: '))

except ValueError:
    while True:
        try:
            periods = float(input('Beloppet måste skrivas i siffror, ex 17.55: '))

        except ValueError:
            pass
        else:
            break

#Returnera två resultat - dels den sammansätta räntan men också total summa efter ränta
print('\n---------------RESULTAT---------------')
print(f'\nSammansatt ränta efter {periods} år: {compound_interest(amount_cash, yearly_rate, periods)}')
print(f'\nTotalt efter {periods} år: {amount_cash + compound_interest(amount_cash, yearly_rate, periods)},kr')




#interest = 1.1
#savings = int(input("Hur mycket vill du spara?"))#hur mycket pengar
#years = int(input("Hur många år vill du spara?"))#hur många år

#test = savings*interest**years
#print("Du kommer ha",test,"kr efter",years,"år")

        # print("while")
        # amount_cash = float(input('Beloppet måste skrivas i siffror, ex 17.55: '))
        # if type(amount_cash) == float:
        #     amount_cash_correct = True
        # if amount_cash_correct:
        #     break
# try:
#     amount_cash = float(input('Hur mycket pengar har du idag: '))
#     print("correct")
#     print(amount_cash_correct)
#     if not amount_cash_correct:
#         while True:
#             print("while")
#             amount_cash = float(input('Beloppet måste skrivas i siffror, ex 17.55: '))
#             if type(amount_cash) == float:
#                 amount_cash_correct = True
#             if amount_cash_correct:
#                 break
# except ValueError:
#     print("error")
#     amount_cash_correct = False
#     pass
# print("test")
# print(amount_cash)
# print(type(amount_cash))

#yearly_rate = float(input('Ränta i procent: '))


#periods = int(input('Antal år att räkna på: '))