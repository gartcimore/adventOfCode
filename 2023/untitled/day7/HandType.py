import enum


class HandType(enum.Enum):
    FiveOfKind = 6
    FourOfKind = 5
    FullHouse = 4
    ThreeOfKind = 3
    TwoPair = 2
    OnePair = 1
    HighCard = 0
