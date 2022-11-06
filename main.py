import random as random
import time

def check_ticket(odds, jackpot):
    ticket = random.randrange(0, odds)
    #print(ticket, jackpot, '\n')
    if ticket == jackpot:
        return True
    return False #else, return False


odds = 292201338 # the odds of winning the powerball jackpot
jackpot = random.randrange(0, odds)
winner = False
tickets = 0
price = 2
cost = 0
prize = 1600000000

x = time.time()
print(f'We are trying to get {jackpot}')
print('Beginning to buy tickets :)')
while winner != True:
    tickets += 1
    winner = check_ticket(odds, jackpot)
    
y = time.time()
print((y-x)) # time it took in seconds to randomly generate the jackpot-winning ticket.
print(tickets/odds, '\n') # ratio of tickets bought to tickets it should take to win in theory.

cost = price * tickets
print(f'{str(tickets)} tickets were bought before the jackpot was won.\nThose tickets cost ${str(price)} each and ${str(cost)} total.\nThe grandprize jackpot was ${str(prize)}.')