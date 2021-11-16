from model.game_logic import *
for i in range(0, 2):
    player_hand.append(deal_hand())
    cpu_hand.append(deal_hand())

player_logic()

ai_behaviour()


if calculate_hand(cpu_hand) <= 21 and calculate_hand(player_hand) <= 21:
    if calculate_hand(player_hand) > calculate_hand(cpu_hand):
        print(f"{player_hand} your hand")
        print(f"{cpu_hand} cpu hand")
        print("You win")
    elif calculate_hand(cpu_hand) == calculate_hand(player_hand):
        print(f"{player_hand} your hand")
        print(f"{cpu_hand} cpu hand")
        print("Draw")
    else:
        print("you loose")
        print(f"{player_hand} your hand")
        print(f"{cpu_hand} cpu hand")





