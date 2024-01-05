from __future__ import annotations

from collections import Counter
from day7.HandType import HandType


class Hand:
    CARD_VALUES = {
        "A": 14,
        "K": 13,
        "Q": 12,
        "J": 11,
        "T": 10,
        "9": 9,
        "8": 8,
        "7": 7,
        "6": 6,
        "5": 5,
        "4": 4,
        "3": 3,
        "2": 2
    }

    def __init__(self, line):
        hand, bid = line.split()
        self.bid = int(bid)
        self.hand = hand

        self.handType = self.analyse_hand(hand)

    def __str__(self):
        return f"Hand: {self.hand} of type {self.handType} and {self.bid}"

    def __repr__(self):
        return Hand.__str__(self)

    def __lt__(self, __other:Hand):
        if self.handType.value < __other.handType.value:
            return True
        if self.handType.value > __other.handType.value:
            return False
        for index in range(5):
            if Hand.CARD_VALUES.get(self.hand[index]) < Hand.CARD_VALUES.get(__other.hand[index]):
                return True
            if Hand.CARD_VALUES.get(self.hand[index]) > Hand.CARD_VALUES.get(__other.hand[index]):
                return False
        return False

    @staticmethod
    def analyse_hand(hand):
        counter = list(Counter(hand).values())
        if 5 in counter:
            return HandType.FiveOfKind
        if 4 in counter:
            return HandType.FourOfKind
        if 3 in counter:
            if 2 in counter:
                return HandType.FullHouse
            return HandType.ThreeOfKind
        if 2 in counter:
            nb_pair = len([item for item in counter if item == 2])
            if nb_pair == 2:
                return HandType.TwoPair
            return HandType.OnePair
        return HandType.HighCard
