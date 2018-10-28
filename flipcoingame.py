import random
import time

#informations and so on
message = "Welcome to the Coinflip game by SirFulgeruL.\n\nBefore we start here are some helpful informations:\n -the game can be played with 2 players\n -1 player has to choose heads or tails\n -if the coin lands on heads the winner is the player that chose heads and so on.\n\nHave fun!"
print(message)
time.sleep(3)
# a list so that random fanction can choose either heads or tails
heads_options = ["heads", "tails"]
# a list so that random function can choose either player1 or player2 should choose his side
player_options = ["player1", "player2"]
# a dictionary in which gets stored the option that the player 1 choose either heads or tails
player1 = {}
# a dictionary in which gets stored the option that the player 2 choose either heads or tails
player2 = {}
player1_points = 0
player2_points = 0

while True:
    # the function that randomizes the output if either heads or tails wins
    heads_choice = random.choice(heads_options)
    # the function that randomizes the ouput if either player 1 or player 2 should start
    playerchoice = random.choice(player_options)
    # asks the player which side he wants to choose
    noname = str(input("{} please choose which side of the coin you want (heads or tails): ".format(playerchoice)).lower().strip())
    # if the user types anything else then heads or tails he has to chose a valid option
    if noname != "heads" or "tails":
        print("Please choose a valid option either heads or tails.")
        break
    # here if playerchoice is player1 add in the dictionary player1 whichever he typed in
    elif playerchoice == "player1" and noname == "heads" or "tails":
        player1[noname] = {"heads_options": noname}
    # here if playerchoice is player2 add in the dictionary player1 whichever he typed in
    elif playerchoice == "player2" and noname == "heads" or "tails":
        player2[noname] = {"heads_options": noname}
    # try function needed for an expection more details down below
    try:
        # function that checks if what player1 chose is winning
        if heads_choice == player1[heads_choice]["heads_options"]:
            # displays a message saying player1 gets 1 points
            print("Player1 got 1 point.")
            # this function clears the values+key inside the dictionary (i needed to do that because I had a bug that didn't matter what u wrote heads/tails u always won.
            player1.clear()
            # this function adds whatever the number is atm in the variable player1_points with 1
            player1_points = player1_points +1
            # displays a message saying player1 has x points and player2 has x points
            print("Player1 has {} and player2 has {}.".format(player1_points,player2_points))
            # a bit of delay so that the players can read the message
            time.sleep(2)
            pass
        # if what player1 chose isn't the winning answer and the if function can't find it it would display an keyerror ouput and this function
        # baiscly expects the keyerror and if the error happens means that player2 won the game because the winning part isn't saved in player1 dictionary
    except KeyError:
        # displays a message saying player1 gets 1 points
        print("Player2 got 1 point.")
        # this function clears the values+key inside the dictionary (i needed to do that because I had a bug that didn't matter what u wrote heads/tails u always won.
        player2.clear()
        # this function adds whatever the number is atm in the variable player1_points with 1
        player2_points = player2_points + 1
        # displays a message saying player1 has x points and player2 has x points
        print("Player2 has {} points and player1 has {} points.".format(player2_points, player1_points))
        time.sleep(2)
        # a bit of delay so that the players can read the message
        pass
    # this function checks if player1 points are higher or equal to 5
    if player1_points >= 5:
        # if the player1 points are higher or equal to 5 it displays this message
        print("Player1 won the game. Congrats!")
        # this ends the whole game
        break
    # this function checks if player2 points are higher or equal to 5
    elif player2_points >=5:
        # if the player1 points are higher or equal to 5 it displays this message
        print("Player2 won the game. Congrats!")
        # this ends the whole gamea
        break

