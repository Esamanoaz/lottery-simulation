import random as random
import time

def create_ticket(rules):
    n_amount, n_odds, p_amount, p_odds = rules
    ticket = {'numbers': [], 'powerball': 0}
    for i in range(n_amount):
        ticket['numbers'].append(random.randrange(1, n_odds + 1))
    for j in range(p_amount):
        ticket['powerball'] = random.randrange(1, p_odds + 1)
    return ticket


def check_ticket(ticket, jackpot, prize_book):
    t_num =sorted(ticket['numbers'])
    t_ball = ticket['powerball']
    j_num = sorted(jackpot['numbers'])
    j_ball = jackpot['powerball']
    has_powerball = False
    total_num = 0

    if t_ball == j_ball:
        has_powerball = True
    for i in range(0, len(t_num)):
        if t_num[i] == j_num[i]:
            total_num += 1
    
    if total_num == 5 and has_powerball:
        print(f'{ticket["numbers"]} {ticket["powerball"]}')

    return prize_book[has_powerball][total_num]


rules = (5, 69, 1, 29)
prize_book = {True: {5: -1, 4: 50000, 3: 100, 2: 7, 1: 4, 0: 0}, 
    False: {5: 1000000, 4: 100, 3: 7, 2: 0, 1: 0, 0: 0}}
odds = 292201338 # the odds of winning the powerball jackpot
jackpot = create_ticket(rules)
won = False
tickets = 0
price = 2
cost = 0
prize = 1900000000
money_won = 0

x = time.time()
print(f'We are trying to get {jackpot["numbers"]} {jackpot["powerball"]}')
print('Beginning to buy tickets :)')
while won != -1:
    tickets += 1
    won = check_ticket(create_ticket(rules), jackpot, prize_book)
    if won > 0:
        money_won += won
    
y = time.time()
print(f'Jackpot: {jackpot["numbers"]} {jackpot["powerball"]}')
print((y-x)) # time it took in seconds to randomly generate the jackpot-winning ticket.
print(tickets/odds, '\n') # ratio of tickets bought to tickets it should take to win in theory.

cost = price * tickets
print(f'{str(tickets)} tickets were bought before the jackpot was won.\nThose tickets cost ${str(price)} each and ${str(cost)} total.\nThe grandprize jackpot was ${str(prize)}, and the other prizes won totaled to ${str(money_won)}.')