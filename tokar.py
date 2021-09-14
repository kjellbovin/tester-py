
def compound_interest(cash, rate, time):
    '''
    Calculates compound interest from the following parameters:
        cash (amount of money to start with)
        rate (rate from which interest is calculated from)
        time (time span in years to calculate compound interest)
    
    Variables:
    total = total amount of money after compound interest is added to the starting amount
    ci = compound interest

    Returns ci rounded by two decimals
    '''

    total = cash * pow((1 + rate/100), time)
    ci = total - cash
    return round(ci, 2)

def input_type_check(user_message:str, data_type):
    '''
    Function to execute an input prompt formatted from the following parameters:
        user_message = prompt
        data_type = preferred data type (str, int, float)

    If the user answer with wrong data type an error message is returned and the user will be asked to 
    enter their input again.

    Returns input_value
    '''

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

print("  _____                                  __  _      __                  __ ")
print(" / ___/__  __ _  ___  ___  __ _____  ___/ / (_)__  / /____ _______ ___ / /_")
print("/ /__/ _ \/  ' \/ _ \/ _ \/ // / _ \/ _  / / / _ \/ __/ -_) __/ -_|_-</ __/")
print("\___/\___/_/_/_/ .__/\___/\_,_/_//_/\_,_/ /_/_//_/\__/\__/_/  \__/___/\__/ ")
print("              /_/                                                          \n\n")

'''
Create a variable by calling the function input_type_check
'''
amount_cash = input_type_check(user_message='Hur mycket pengar har du idag: ', data_type=float)
yearly_rate = input_type_check(user_message='Ränta i procent: ', data_type=float)
periods = input_type_check(user_message='Antal år att räkna på: ', data_type=float)

print('\n---------------RESULTAT---------------')
print(f'\nSammansatt ränta efter {periods} år: {compound_interest(cash=amount_cash, rate=yearly_rate, time=periods)}')
print(f'\nTotalt efter {periods} år: {amount_cash + compound_interest(cash=amount_cash, rate=yearly_rate, time=periods)}')