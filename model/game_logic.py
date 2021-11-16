import random

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

player_hand = []
cpu_hand = []


def deal_hand():
    card = random.randint(0, len(cards) - 1)
    return cards[card]


def calculate_hand(hand):
    total = 0
    for i in range(0, len(hand)):
        total += hand[i]
    return total


def ai_behaviour():
    cpu_card_count = calculate_hand(cpu_hand)
    while True:
        if cpu_card_count <= 10:
            cpu_hand.append(deal_hand())
            cpu_card_count = calculate_hand(cpu_hand)
        elif cpu_card_count <= 15:
            choice = bool(random.getrandbits(1))
            if choice:
                cpu_hand.append(deal_hand())
                cpu_card_count = calculate_hand(cpu_hand)
                break
            break
        elif cpu_card_count <= 21:
            break
        if cpu_card_count > 21:
            print("Ai lost by going over 21")
            print(cpu_hand)
            break
    return cpu_card_count


def player_logic():
    print(f"Your hand is {player_hand} has the total wort of {calculate_hand(player_hand)}")
    print(f"Cpu has [{cpu_hand[0]}] has the total value of {cpu_hand[0]}")
    choice = input("Do you want extra card say y for it \n")
    while choice == 'y':
        player_hand.append(deal_hand())
        print(player_hand)
        if calculate_hand(player_hand) > 21:
            print(calculate_hand(player_hand))
            print(player_hand)
            print("you lost by going over 21")
            break
        choice = input("Do you want more if yes press y")
    return calculate_hand(player_hand)
