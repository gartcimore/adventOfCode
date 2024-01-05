import math

from common.Day import Day
from common.Mode import Mode
from common.Step import Step
from day7.Hand import Hand


class Day7(Day):

    def __init__(self, step: Step = Step.STEP_1) -> None:
        super().__init__(__class__.__name__, mode=Mode.TEST, step=step)

    def solveStep1(self):
        hands = []
        for index, line in enumerate(self.raw_items):
            hands.append(Hand(line))
            # print(f" created {hands[index]}")

        hands.sort()
        sum = 0
        for index, hand in enumerate(hands):
            sum += (index + 1) * hand.bid
        return sum


# Part 1
day: Day7 = Day7(step=Step.STEP_1)
print(f"Part#1 Test: {day.solveStep1()}")
day.prod_mode()
print(f"Part#1 Prod: {day.solveStep1()}")


# Part 2
day: Day7= Day7(step=Step.STEP_2)
print(f"Part#2 Test: {day.dummy()}")
day.prod_mode()
print(f"Part#2 Prod: {day.dummy()}")
