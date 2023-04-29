from Ruleta.Inside_bets import Inside_bet
from Ruleta.Outside_bets import Outside_bet
from Ruleta.Random_bet import Random_bet
z = 0
while True:
    z = z + 1
    sentences = ["Welcome to a rulet game!!! What tipe of bets system you want to play: Inside bets, Outside bets or Random bets?", "What tipe of bets system you want to play: Inside bets, Outside bets or Random bets?" ]
    if z == 1:
        output = sentences[0]
    else:
        output = sentences[1]
    try:
        x = input(f"{output}\n").lower()
        if x == "inside bets" or x == "inside bet" or x == "inside":
            Inside_bet(100)
            while True:
                y = input("Do you want play again? Yes or No\n").lower()
                if y == "yes":
                    break
                elif y == "no":
                    exit()
                else:
                    print("Please enter a valid response.")
        elif x == "outside bet" or x == "outside bets" or x == "outside":
            Outside_bet(100)
            while True:
                y = input("Do you want play again? Yes or No\n").lower()
                if y == "yes":
                    break
                elif y == "no":
                    exit()
                else:
                    print("Please enter a valid response.")
        elif x == "random bets" or x == "random bets" or x == "random":
            Random_bet(100)
            while True:
                y = input("Do you want play again? Yes or No\n").lower()
                if y == "yes":
                    break
                elif y == "no":
                    exit()
                else:
                    print("Please enter a valid response.")
        else:
            print("Enter opotion from menu!!!")
    except ValueError:
        print("Enter correct syntax!!!")


