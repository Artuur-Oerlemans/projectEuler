import functools
from collections import Counter

from Card import Card
from Hand import Hand
from HandScore import HandScore


class HandJudge:

    # straight flush is 8, high card is 0 (royal flush is already highest, without it being a special case)
    @staticmethod
    def get_hand_score(hand: Hand):
        score = HandJudge.straight_flush(hand)
        if score is not None:
            return score
        score = HandJudge.four_of_a_kind(hand)
        if score is not None:
            return score
        score = HandJudge.full_house(hand)
        if score is not None:
            return score
        score = HandJudge.flush(hand)
        if score is not None:
            return score
        score = HandJudge.straight(hand)
        if score is not None:
            return score
        score = HandJudge.three_of_a_kind(hand)
        if score is not None:
            return score
        score = HandJudge.two_pairs(hand)
        if score is not None:
            return score
        score = HandJudge.one_pair(hand)
        if score is not None:
            return score

        return HandScore(0, [], hand.cards)

    @staticmethod
    def straight_flush(hand: Hand):
        if HandJudge.is_straight(hand) and HandJudge.is_flush(hand):
            return HandScore(8, [], hand.cards)

    @staticmethod
    def four_of_a_kind(hand: Hand):
        rank_dict = HandJudge.get_rank_occurrence_counter_dict(hand.cards)
        for rank in rank_dict.keys():
            if rank_dict[rank] == 4:
                return HandScore(7, [rank], hand.cards)

    @staticmethod
    def full_house(hand: Hand):
        rank_dict = HandJudge.get_rank_occurrence_counter_dict(hand.cards)
        for rank1 in rank_dict.keys():
            if rank_dict[rank1] == 3:
                for rank2 in rank_dict.keys():
                    if rank_dict[rank2] == 2:
                        return HandScore(6, [rank1, rank2], hand.cards)

    @staticmethod
    def flush(hand: Hand):
        if HandJudge.is_flush(hand):
            return HandScore(5, [], hand.cards)

    @staticmethod
    def straight(hand: Hand):
        if HandJudge.is_straight(hand):
            return HandScore(4, [], hand.cards)

    @staticmethod
    def three_of_a_kind(hand: Hand):
        rank_dict = HandJudge.get_rank_occurrence_counter_dict(hand.cards)
        for rank in rank_dict.keys():
            if rank_dict[rank] == 3:
                return HandScore(3, [rank], hand.cards)

    @staticmethod
    def two_pairs(hand: Hand):
        rank_dict = HandJudge.get_rank_occurrence_counter_dict(hand.cards)
        pairs = []
        for rank in rank_dict:
            if rank_dict[rank] == 2:
                pairs.append(rank)
        if len(pairs) == 2:
            pairs.sort(reverse=True)
            return HandScore(2, pairs, hand.cards)

    @staticmethod
    def one_pair(hand: Hand):
        rank_dict = HandJudge.get_rank_occurrence_counter_dict(hand.cards)
        for rank in rank_dict.keys():
            if rank_dict[rank] == 2:
                return HandScore(1, [rank], hand.cards)

    @staticmethod
    def is_flush(hand: Hand):
        suit = hand.cards[0].suit
        are_same_suit = [card.suit == suit for card in hand.cards]
        return functools.reduce(lambda x, y: x and y, are_same_suit)

    @staticmethod
    def is_straight(hand: Hand):
        rank = hand.cards[0].rank_to_int()
        for i in range(1, 5):
            if hand.cards[i].rank_to_int() != rank - i:
                return False
        return True

    @staticmethod
    def get_rank_occurrence_counter_dict(cards: list[Card]):
        rank_ints = [card.rank_to_int() for card in cards]
        return Counter(rank_ints)
