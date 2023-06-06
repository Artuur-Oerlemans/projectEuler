from Hand import Hand
from HandJudge import HandJudge

file = open("p054_poker.txt", "r")
# file = open("p054_poker_example.txt", "r")
# file = open("poker_debug.txt", "r")
contents = file.read()
games = contents.split('\n')


def game_to_hands(game: str):
    hand1 = Hand(game[0: 14])
    hand2 = Hand(game[15: len(game)])
    return hand1, hand2


hand1_win_counter = 0
for game in games:
    hand1, hand2 = game_to_hands(game)
    hand1_score = HandJudge.get_hand_score(hand1)
    hand2_score = HandJudge.get_hand_score(hand2)
    print(hand1_score, hand2_score)
    print(hand1_score > hand2_score)
    if hand1_score > hand2_score:
        hand1_win_counter += 1

print(hand1_win_counter)
