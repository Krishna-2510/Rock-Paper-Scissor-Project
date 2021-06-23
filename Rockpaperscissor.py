import random


def Won(p, com):
    if p == com:
        return None
    elif com == 'r':
        if p == 'p':
            return True
        elif p == 's':
            return False
    elif com == 'p':
        if p == 's':
            return True
        elif p == 'r':
            return False
    elif com == 's':
        if p == 'r':
            return True
        elif p == 'p':
            return False


print('''                                      ROCK, PAPER AND SCISSOR GAME''')
print('''                                                                                   To quit enter q''')
while(True):
    player = input("Your turn: Rock(r), Paper(p), Scissor(s)\n")
    if player is 'q':
        print("                                Thankyou for playing")
        exit()
    else:
        c = random.randint(1, 3)
        if c == 1:
            comp = 'r'
        elif c == 2:
            comp = 'p'
        elif c == 3:
            comp = 's'
        res = Won(player, comp)
        print(f"                               The computer chose {comp}")
        if res is None:
            print("                            Its a Draw")
        elif res:
            print("                            You have won!!!")
        else:
            print("                            You lose!!!")
