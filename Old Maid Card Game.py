# In this implementation a card (that is not a 10) is represented
# by a 2 character string, where the 1st character represents a rank and the 2nd a suit.
# Each card of rank 10 is represented as a 3 character string, first two are the rank and the 3rd is a suit.

import random

def wait_for_player():
    '''()->None
    Pauses the program until the user presses enter
    '''
    try:
         input("\nPress enter to continue. ")
         print()
    except SyntaxError:
         pass


def make_deck():
    '''()->list of str
        Returns a list of strings representing the playing deck,
        with one queen missing.
    '''
    deck=[]
    suits = ['\u2660', '\u2661', '\u2662', '\u2663']
    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for suit in suits:
        for rank in ranks:
            deck.append(rank+suit)
    deck.remove('Q\u2663') # remove a queen as the game requires
    return deck

def shuffle_deck(deck):
    '''(list of str)->None
       Shuffles the given list of strings representing the playing deck    
    '''
    random.shuffle(deck)

#####################################

def deal_cards(deck):
     '''(list of str)-> tuple of (list of str,list of str)

     Returns two lists representing two decks that are obtained
     after the dealer deals the cards from the given deck.
     The first list represents dealer's i.e. computer's deck
     and the second represents the other player's i.e user's list.
     '''
     dealer=[]
     other=[]

     # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
     # YOUR CODE GOES HERE

     for i in range(51):
        if i <= 25:
            dealer.append(deck[i])
        elif i > 25:
            other.append(deck[i])
     return (dealer, other)
 


def remove_pairs(l):
    '''
     (list of str)->list of str

     Returns a copy of list l where all the pairs from l are removed AND
     the elements of the new list shuffled

     Precondition: elements of l are cards represented as strings described above

     Testing:
     Note that for the individual calls below, the function should
     return the displayed list but not necessarily in the order given in the examples.

     >>> remove_pairs(['9♠', '5♠', 'K♢', 'A♣', 'K♣', 'K♡', '2♠', 'Q♠', 'K♠', 'Q♢', 'J♠', 'A♡', '4♣', '5♣', '7♡', 'A♠', '10♣', 'Q♡', '8♡', '9♢', '10♢', 'J♡', '10♡', 'J♣', '3♡'])
     ['10♣', '2♠', '3♡', '4♣', '7♡', '8♡', 'A♣', 'J♣', 'Q♢']
     >>> remove_pairs(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢'])
     ['2♣', '5♢', '6♣', '9♣', 'A♢']
    '''

    no_pairs=[]

    # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
    # YOUR CODE GOES HERE
    cardCount = 1
    stoppedCount = False
    i = 0
    l.sort()
    while i < len(l):
        if len(l) > 0:
            if stoppedCount:
                if cardCount >= 2:
                    cardAtI = l[i]
                    if cardCount % 2 == 0:
                        stoppedCount = False
                        cardCount = 1
                        i += 1
                    else:
                        no_pairs.append(cardAtI)
                        stoppedCount = False
                        cardCount = 1
                        i += 1
                elif cardCount < 2:
                    cardAtI = l[i]
                    no_pairs.append(cardAtI)
                    stoppedCount = False
                    i += 1
                else:
                    print("Something went wrong!")
            elif stoppedCount == False:
                if i < len(l) - 1:
                    a = l[i]
                    b = l[i + 1]
                    if len(a) == 2:
                        aNum = a[:1]
                    elif len(a) > 2:
                        aNum = a[:2]

                    if len(b) == 2:
                        bNum = b[:1]
                    elif len(b) > 2:
                        bNum = b[:2]

                    if aNum == bNum:
                        cardCount += 1
                        i += 1
                    else:
                        stoppedCount = True
                else:
                    stoppedCount = True

    random.shuffle(no_pairs)
    return no_pairs

def print_deck(deck):
    '''
    (list)-None
    Prints elements of a given list deck separated by a space
    '''

    # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
    # YOUR CODE GOES HERE
    stringDeck = str(deck)
    spacedDeck = stringDeck.replace(","," ").replace("[","").replace("]","")

    print(spacedDeck)

def get_valid_input(n):
     '''
     (int)->int
     Returns an integer given by the user that is at least 1 and at most n.
     Keeps on asking for valid input as long as the user gives integer outside of the range [1,n]
     
     Precondition: n>=1
     '''

     # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
     # YOUR CODE GOES HERE


     cardInput = None
     isValid = False
     numOfCards = str(n)
     if numOfCards.isdigit():
        print("I have " + numOfCards + " cards. If 1 stands for my first card and")
        print(numOfCards + " stands for my last card, which of my cards would you like?")
        cardInput = input("Give me an integer between 1 and " + numOfCards + ": ")

        while isValid == False:
            if cardInput.isdigit():
                if int(cardInput) >= 1 and int(cardInput) <= n:
                    isValid = True
                    cardInput = int(cardInput)
                else:
                    cardInput = input("Invalid number. Please enter an integer between 1 and " + numOfCards + ": ")

            else:
                cardInput = input("Invalid input. Please enter an integer between 1 and " + numOfCards + ": ")
     else:
        print("n did not meet the precondition!")

     return cardInput

def play_game():
     '''()->None
     This function plays the game'''
    
     deck=make_deck()
     shuffle_deck(deck)
     tmp=deal_cards(deck)

     dealer=tmp[0]
     human=tmp[1]

     print("Hello. My name is Robot and I am the dealer.")
     print("Welcome to my card game!")
     print("Your current deck of cards is:")
     print_deck(human)
     print("Do not worry. I cannot see the order of your cards")

     print("Now discard all the pairs from your deck. I will do the same.")
     wait_for_player()
     
     dealer=remove_pairs(dealer)
     human=remove_pairs(human)

     # COMPLETE THE play_game function HERE
     # YOUR CODE GOES HERE

     turnCounter = 0
     gameEnded = False

     while gameEnded == False:
          if gameEnded == False and len(dealer) > 0 and turnCounter == 0:
                 print("**********************************************")
                 print("Your turn.")
                 print("")
                 print("Your current deck of cards is:")
                 print("")
                 print_deck(human)
                 print("")
                 pickedCard = get_valid_input(len(dealer))
                 nthCard = dealer[pickedCard-1]

                 if pickedCard == 1:
                     print("You asked for my 1st card")
                 elif pickedCard == 2:
                     print("You asked for my 2nd card")
                 elif pickedCard == 3:
                     print("You asked for my 3rd card")
                 else:
                     print("You asked for my "+str(pickedCard)+"th card")

                 print("Here it is. It is " + nthCard)
                 human.append(nthCard)
                 dealer.remove(nthCard)
                 print("")
                 print("With "+nthCard+" added, your current deck of cards is:")
                 print("")
                 print_deck(human)
                 print("")
                 print("After discarding pairs and shuffling, your deck is:")
                 print("")
                 human=remove_pairs(human)
                 print_deck(human)
                 print("")
                 print("")
                 turnCounter += 1
                 wait_for_player()
          elif gameEnded == False and turnCounter == 0 and len(dealer) == 0:
                 gameEnded = True
                 print("**********************************************")
                 print("Ups. I do not have any more cards")
                 print("You lost! I, Robot, win")

          elif gameEnded == False and len(human) > 0 and turnCounter == 1:
                print("**********************************************")
                print("My turn.")
                humanDeckSize = len(human)-1
                pickedCard = random.randint(1,humanDeckSize)
                nthCard = human[pickedCard - 1]

                if pickedCard == 1:
                    print("I took your 1st card")
                elif pickedCard == 2:
                    print("I took your 2nd card")
                elif pickedCard == 3:
                    print("I took your 3rd card")
                else:
                    print("I took your "+str(pickedCard)+"th card")
                dealer.append(nthCard)
                human.remove(nthCard)
                dealer = remove_pairs(dealer)
                turnCounter = 0
                wait_for_player()
          elif gameEnded == False and turnCounter == 1 and len(human) == 0:
              gameEnded = True
              print("**********************************************")
              print("Ups. You do not have any more cards")
              print("Congratulations! You, Human, win")


# main
play_game()
