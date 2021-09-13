# Nicklas Thor
import collections
import random

def get_random_risk():
    '''
    get_random_risk is a function to get a random rate that can sometimes be lucky or unlucky
    
    Returns:
        risk (object): Object contining rate, is_lucky and is_unlucky
            rate (int): a random int based on predetermine values
            is_lucky (bool): tell if its a lucky rate this time, with means rate is higher then usual
            is_unlucky (bool): tell if its a unlucky rate this time, with means rate is lower then usual
    '''
    random_risk = collections.namedtuple('random_risk', ['rate', 'is_lucky', 'is_unlucky'])
    max = 40 # int used for highest possible random int
    min = -40 # int used for lowest possible random int
    lucky = 30 # int to check when being lucky
    lucky_bonus = 200 # int for how much bonus being lucky gives
    unlucky = -30 # int to check when being unlucky
    unlucky_penalty = 40 # int for how much penalty being unlucky gives
    random_number = random.randint(min, max) # random int betwin min and max
    is_lucky = False # bool for tracking if lucky
    is_unlucky = False # bool for tracking if is_unlucky

    # check if lucky
    if random_number >= lucky:
        is_lucky = True
    #check if unlucky
    elif random_number <= unlucky:
        is_unlucky = True
    
    # apply lucky_bonus if is_lucky on random_number
    if is_lucky:
        random_number += lucky_bonus
    # apply unlucky_penalty if is_unlucky on random_number
    elif is_unlucky:
        random_number -= unlucky_penalty

    risk = random_risk(rate = random_number, is_lucky = is_lucky, is_unlucky = is_unlucky)
    return risk

def risky_investment(cash, time):
    '''
    calculate and print out result year by year and end result of a risky investment 

        Parameters:
            cash (float): amount of starting cash
            time (int): amount of years the risky investment will last
                most be positive integer
    '''

    year = 0 # int used to track how many year it been
    new_cash = 0.00 # float used to check how cash changes during each loop
    old_cash = cash # float to be used to check total cash change
    
    # while loop for each year that update that happen with money and print out what happens every year
    while year < time:
        year += 1
        risk = get_random_risk() # random_risk with a random rate and if it was lucky, unlucky or neither
        new_cash = cash * (1 + risk.rate/100)
        cash_change = new_cash - cash # float for how big cash change it was this year

        # check if this year was a lucky or unlucky year and print it out to user
        if risk.is_lucky:
            print('\nDetta år gick det ovanligt bra, vilket fantastisk tur du har.')
        elif risk.is_unlucky:
            print('\nDetta år gick det ovanligt dåligt, vilket usel otur du har.')
        
        # print out this years result
        print(f'\nÅr {year} ändrades dina pengar med {round(cash_change, 2)} kr och det är {round(new_cash, 2)} kr på din investering.')

        cash = new_cash # update cash to be same as new cash
    
    # print out result of this risky investment 
    print(f'\nTotalt efter {year} år har {round(cash, 2)} kr vilket är en ändring på {round(cash - old_cash, 2)} kr ifrån {round(old_cash, 2)} kr som du startade med.')

#Definiera en funktion som sköter uträkningen av ränta på ränta samt returnerar en variabel - ci - avrundad till två decimaler
def compound_interest(cash, rate, time):
    a = cash * pow((1 + rate/100), time)
    ci = a - cash
    return round(ci, 2)

def print_bank_result(amount_cash, yearly_rate, periods):
    # print out result of using bank to save money
    print('\n---------------RESULTAT---------------')
    print(f'\nSammansatt ränta efter {periods} år: {compound_interest(amount_cash, yearly_rate, periods)}')
    print(f'\nTotalt efter {periods} år: {amount_cash + compound_interest(amount_cash, yearly_rate, periods)}')

#Begär input från användaren
amount_cash = float(input('Hur mycket pengar har du idag: '))
periods = int(input('Antal år att räkna på: '))

bank_or_investment = int(input('Vill du \n1: Spara pengar på en bank. \n2: Göra en riskfyld investering \n: '))
while True:
    if bank_or_investment == 1 or bank_or_investment == 2:
        break
    print("Du måste välj 1 för att spara på en bank eller 2 för att göra en riskfyld investering")
    bank_or_investment = int(input(': '))

# if bank_or_investment is 1 proced with bank savings
if bank_or_investment == 1:
    yearly_rate = float(input('Ränta i procent: '))
    print_bank_result(amount_cash, yearly_rate, periods)

# if bank_or_investment 2 proced with risky investment
elif bank_or_investment == 2:
    risky_investment(amount_cash, periods)

# something is wrong with how bank_or_investment is handle as i shall only be 1 or 2
else:
    error_msg = f"""
Something went wrong when bank_or_investment \
should only be int 1 or 2 when bank_or_investment now is: {bank_or_investment}
"""
    raise Exception(error_msg)
