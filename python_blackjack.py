import os
import random

decks = input("Kaç Deste İle Oynamak İstersiniz: ")

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*(int(decks)*4)

wins = 0
losses = 0

def deal(deck):
    hand = []
    for i in range(2):
        random.shuffle(deck)
        card = deck.pop()
        if card == 11:card = "J"
        if card == 12:card = "Q"
        if card == 13:card = "K"
        if card == 14:card = "A"
        hand.append(card)
    return hand

def play_again():
    again = input("BİR DAHA OYNAMAK İSTERMİSİN? (E/H) : ").lower()
    if again == "e":
        dealer_hand = []
        player_hand = []
        deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
        game()
    else:
        print("Bye!")
        exit()

def total(hand):
    total = 0
    for card in hand:
        if card == "J" or card == "Q" or card == "K":
            total+= 10
        elif card == "A":
            if total >= 11: total+= 1
            else: total+= 11
        else: total += card
    return total

def hit(hand):
    card = deck.pop()
    if card == 11:card = "J"
    if card == 12:card = "Q"
    if card == 13:card = "K"
    if card == 14:card = "A"
    hand.append(card)
    return hand

def clear():
    if os.name == 'nt':
        os.system('CLS')
    if os.name == 'posix':
        os.system('clear')

def print_results(dealer_hand, player_hand):
    clear()

    print("\n    BLACKJACK'E HOŞGELDİNİZ...!\n")
    print("-"*30+"\n")
    print("    \033[1;32;40mWINS:  \033[1;37;40m%s   \033[1;31;40mLOSSES:  \033[1;37;40m%s\n" % (wins, losses))
    print("-"*30+"\n")
    print ("KRUPİYER'İN ELİ " + str(dealer_hand) + "TOPLAM EL " + str(total(dealer_hand)))
    print ("SENİN ELİN " + str(player_hand) + " TOPLAM EL " + str(total(player_hand)))

def blackjack(dealer_hand, player_hand):
    global wins
    global losses
    if total(player_hand) == 21:
        print_results(dealer_hand, player_hand)
        print ("TEBRİKLER,BLACKJACK!\n")
        wins += 1
        play_again()
    elif total(dealer_hand) == 21:
        print_results(dealer_hand, player_hand)
        print ("KAYBETTİN KASA BLACKJACK\n")
        losses += 1
        play_again()

def score(dealer_hand, player_hand):
        global wins
        global losses
        if total(player_hand) == 21:
            print_results(dealer_hand, player_hand)
            print ("TEBRİKLER BLACKJACK\n")
            wins += 1
        elif total(dealer_hand) == 21:
            print_results(dealer_hand, player_hand)
            print ("KAYBETTİN KASA BLACKJACK\n")
            losses += 1
        elif total(player_hand) > 21:
            print_results(dealer_hand, player_hand)
            print ("KAYBETTİN ELİN 21'DEN BÜYÜK\n")
            losses += 1
        elif total(dealer_hand) > 21:
            print_results(dealer_hand, player_hand)
            print ("KASA 21'DEN BÜYÜK AÇTI,KAZANDIIN...\n")
            wins += 1
        elif total(player_hand) < total(dealer_hand):
            print_results(dealer_hand, player_hand)
            print ("KAYBETTİN KASADAN DAHA KÜÇÜK ELİN VAR...\n")
            losses += 1
        elif total(player_hand) > total(dealer_hand):
            print_results(dealer_hand, player_hand)
            print ("TEBRİKLER KAZANDIIN!ELİN KASADAN DAHA BÜYÜK\n")
            wins += 1

def game():
    global wins
    global losses
    choice = 0
    clear()
    print("\n    BLACKJACK'E HOŞGELDİN!\n")
    print("-"*30+"\n")
    print("    \033[1;32;40mWINS:  \033[1;37;40m%s   \033[1;31;40mLOSSES:  \033[1;37;40m%s\n" % (wins, losses))
    print("-"*30+"\n")
    dealer_hand = deal(deck)
    player_hand = deal(deck)
    print ("KRUPİYER GÖSTERİYOR " + str(dealer_hand[0]))
    print (" SENİN ELİN " + str(player_hand) + " TOPLAM EL " + str(total(player_hand)))
    blackjack(dealer_hand, player_hand)
    quit=False
    while not quit:
        choice = input("SEÇİMİNİ YAP [A]KART AL, [K]KAL, or [Ç]ÇIKIŞ: ").lower()
        if choice == 'a':
            hit(player_hand)
            print(player_hand)
            print("TOPLAM EL: " + str(total(player_hand)))
            if total(player_hand)>21:
                print('YANDIN!')
                losses += 1
                play_again()
        elif choice=='k':
            while total(dealer_hand)<17:
                hit(dealer_hand)
                print(dealer_hand)
                if total(dealer_hand)>21:
                    print('Krupiyer kaybetti... Kazandıın!')
                    wins += 1
                    play_again()
            score(dealer_hand,player_hand)
            play_again()
        elif choice == "ç":
            print("GÖRÜŞÜRÜZ...!")
            quit=True
            exit()


if __name__ == "__main__":
   game()