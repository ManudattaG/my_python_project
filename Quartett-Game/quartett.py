import itertools
import random
import re
from itertools import zip_longest
from random import shuffle
from typing import List, Tuple
 
QUARTET_COUNT = 4
DECK = ['A-0', 'A-1', 'A-2', 'A-3', 'B-0', 'B-1', 'B-2', 'B-3', 'C-0', 'C-1', 'C-2', 'C-3', 'D-0', 'D-1', 'D-2', 'D-3', 'E-0', 'E-1', 'E-2', 'E-3']
PLAYERS = ["Anna", "Bert", "Claudia", "Dan"]
QUARTET_RESULT = {"Anna": 0, "Bert": 0, "Claudia": 0, "Dan": 0}

REMAINING_CARDS_MESSAGE = "There are {cards_left} cards {player_name} can ask for."
INITIAL_PLAYER_TURN_MESSAGE = "It's {player_name}'s turn."
CARD_REQUEST_MESSAGE = "{player_name} is asking {other_player_name} for {card}."
NO_CARD_MESSAGE = "{player_name} does not have {card}."
NEXT_PLAYER_TURN_MESSAGE = "It's now {player_name}'s turn."
GET_CARD_MESSAGE = "{player_name} gets {card} from {other_player_name}."
QUARTET_MESSAGE = "{player_name} has a quartet!"
QUARTET_PUTDOWN_MESSAGE = "{player_name} is putting down {quartet_set}"
OUTOFCARDS_MESSAGE = "{player_name} is out of cards!"

# Prints a template message
def print_message(message: str, player_name: str, card: str = None, 
            cards_left: int = None, other_player_name: str = None, quartet_set: List = None) -> None:
    print(message.format(player_name=player_name, card=card, 
            cards_left=cards_left, other_player_name=other_player_name, quartet_set=quartet_set))

# Returns a group of n cards
def grouper(n: int, iterable: List, fillvalue=None) -> zip_longest:
    args = [iter(iterable)] * n
    return zip_longest(fillvalue=fillvalue, *args)

# Prints player's initial set of evenly split cards
def print_player_cards(deck: List) -> dict:
    hand = grouper(5, deck)
    player_board = dict()
    for player in PLAYERS:
        player_board[player] = list(next(hand))
        print(player + ": " + str(player_board[player]))
    return(player_board)

# Prints updated player board in each set of play
def print_update_playerBoard(player_board: dict) -> None:
    all_player_empty = all([player_board[i] == [] for i in player_board])
    if not (all_player_empty):
        print("\n")
        for player in player_board.items():
            print(player[0] + ": " + str(player[1]))

# Returns remaining cards a player can ask for
def count_matching_cards(Cards: List) -> int:
    ask_count = 0
    pattern_regex_list = ["A", "B", "C", "D", "E"]
    for pattern in pattern_regex_list:
        card_pattern_count = len(re.findall(pattern, str(Cards)))
        if(card_pattern_count > 0):
            ask_count += QUARTET_COUNT - card_pattern_count
    return(ask_count)

# Calculates the number of quartets and prints if the player has a quartet
def print_quartet_message(player: str, ask_card: List) -> None:
    print_message(QUARTET_MESSAGE, player_name=player)
    print_message(QUARTET_PUTDOWN_MESSAGE, player_name=player, quartet_set=ask_card)
    QUARTET_RESULT[player] = QUARTET_RESULT[player] + 1

# Returns the card a player can ask for
def player_turn_to_askCard(Cards: List) -> list:
    first_letter = [string[0] for string in Cards]
    max_letter = max(first_letter, key=first_letter.count)
    max_letter_value = [i for i in Cards if i.startswith(max_letter)]
    num = [*range(4)]
    number_available = [int(j[2]) for j in max_letter_value]
    missing_cards = [x for x in num if x not in number_available]
    if(len(missing_cards) != 0):
        ask_card = [max_letter+"-"+str(i) for i in missing_cards]
        return(ask_card)
    else:
        return(max_letter_value)

# Returns the other game player to request for
def ask_another_player_card(players: list, game_player: str, game_player_board: List) -> str:
    other_player_list = [player for player in players if player != game_player]
    nonempty_player_list = [player for player in other_player_list if game_player_board[player]]
    requesting_player = random.choice(nonempty_player_list)
    return(requesting_player)

def print_final_result():
    print("\n")
    for player in PLAYERS:
        print(player + " has " + str(QUARTET_RESULT[player]) + " quartets")
    max_quartets = max(QUARTET_RESULT.values())
    winners = [k for k,v in QUARTET_RESULT.items() if v == max_quartets]
    if(len(winners) > 1):
        winner_msg = ', '.join(str(value) for value in winners)
        print(winner_msg + " are the Winners!!!!!!")
    else:
        print(winners[0] + " is the Winner!!!!!!")

def start_game(game_player: str, player_board: List, prev_asked_card: str, players: List = PLAYERS) -> tuple():
    """
    Play the Quartet game according to https://maestromusic.eu/game-rules-maestro-quartet
    :param game_player: A game player
    :param player_board: Evenly split of each player board from the shuffled deck
    :param prev_asked_card: Previously asked card of a game_player to avoid asking again
    :param players: List of computer players playing this game

    :returns: Tuple (game_player, player_board, asked_card)
    """
    ask_count = count_matching_cards(player_board[game_player])
    if(ask_count != 0):
        print_message(INITIAL_PLAYER_TURN_MESSAGE, player_name=game_player)
        print_message(REMAINING_CARDS_MESSAGE, player_name=game_player, cards_left=ask_count)

        ask_card = player_turn_to_askCard(player_board[game_player])
        if(len(ask_card) != 4):
            if(prev_asked_card != None):
                ask_card = [card for card in ask_card if card != prev_asked_card]
            ask_card = random.choice(ask_card)
            requesting_player = ask_another_player_card(players, game_player, player_board)
            print_message(CARD_REQUEST_MESSAGE, player_name=game_player, card=ask_card, other_player_name=requesting_player)

            # If opponent player has the requested card
            if(ask_card in player_board[requesting_player]):
                print_message(GET_CARD_MESSAGE, player_name=game_player, card=ask_card, other_player_name=requesting_player)
                player_board[game_player].append(ask_card) # Add requested card to the player board
                quartet_card = player_turn_to_askCard(player_board[game_player])
                if(len(quartet_card) == 4):
                    print_quartet_message(game_player, quartet_card)
                    for element in quartet_card:
                        player_board[game_player].pop(player_board[game_player].index(element)) # Remove quartet cards from the player board
                player_board[requesting_player].pop(player_board[requesting_player].index(ask_card)) # Remove handed over card from the player board
                print_update_playerBoard(player_board)
                return(game_player, player_board, ask_card)

            else:
                # If opponent player does not have the requested card
                print_message(NO_CARD_MESSAGE, player_name=requesting_player, card=ask_card)
                print_message(NEXT_PLAYER_TURN_MESSAGE, player_name=requesting_player)
                print_update_playerBoard(player_board)
                return(requesting_player, player_board, ask_card)
        else:
            print_quartet_message(game_player, ask_card)
            return(game_player, player_board, None)
    else:
        print_message(OUTOFCARDS_MESSAGE, player_name=game_player)
        other_player = ask_another_player_card(players, game_player, player_board)
        return(other_player, player_board, None)


if __name__ == "__main__":
    shuffle(DECK) # Shuffling deck of 20 cards
    player_board = print_player_cards(DECK)
    game_initiator = random.choice(PLAYERS)
    next_player, next_player_board, prev_asked_card = start_game(game_initiator, player_board, prev_asked_card=None)
    for player in PLAYERS:
        while(next_player_board[player]):
            next_player, next_player_board, prev_asked_card = start_game(next_player, next_player_board, prev_asked_card)
            continue
    else:
        print_message(OUTOFCARDS_MESSAGE, player_name=next_player)
        print("All players out of cards - game is over!")
        print_final_result()