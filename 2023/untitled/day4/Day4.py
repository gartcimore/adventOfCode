from functools import reduce

from common.Day import Day
from common.Mode import Mode
from common.Step import Step

class Day4(Day):

    def __init__(self, step: Step = Step.STEP_1) -> None:
        super().__init__(__class__.__name__, mode=Mode.TEST, step=step)


    def solveStep1(self):

        sum = 0
        for line_index, line in enumerate(self.raw_items):
            clean_line = line[line.find(":") + 1:]
            winning_str, owned_str = clean_line.split("|", 1)
            winning_str = winning_str.strip()
            owned_str = owned_str.strip()
            winning_list = winning_str.split()
            owned_list = owned_str.split()
            winning_dict = {}
            for number in winning_list:
                winning_dict[number] = True
            card_score = 0
            for number in owned_list:
                if(number in winning_dict):
                    if(card_score > 0):
                        card_score = card_score * 2
                    else:
                        card_score = 1
                    print(f"line {line_index} card score is '{card_score}'")
            sum += card_score

        return sum


    def solveStep2(self):

        sum = 0
        cards = {}
        for init in range(len(self.raw_items)):
            cards[init] = 1

        for line_index, line in enumerate(self.raw_items):
            clean_line = line[line.find(":") + 1:]
            winning_str, owned_str = clean_line.split("|", 1)
            winning_str = winning_str.strip()
            owned_str = owned_str.strip()
            winning_list = winning_str.split()
            owned_list = owned_str.split()
            winning_dict = {}
            for number in winning_list:
                winning_dict[number] = True
            nb_cards = 0
            for number in owned_list:
                if(number in winning_dict):
                    nb_cards += 1
            for index in range(nb_cards):
                cards[index+line_index+1] += cards[line_index]
                # print(f"index+line_index+1: {index+line_index+1} £ cards[line_index] : {cards[line_index]} $ cards[index+line_index+1] : {cards[index+line_index+1]}")

            # print(f"end for")

        sum = reduce(lambda a,b: a+b, cards.values())
        return sum

# Part 1
day_4: Day4 = Day4(step=Step.STEP_1)
print(f"Part#1 Test: {day_4.solveStep1()}")
day_4.prod_mode()
print(f"Part#1 Prod: {day_4.solveStep1()}")


# Part 2
day_4: Day4 = Day4(step=Step.STEP_2)
print(f"Part#2 Test: {day_4.solveStep2()}")
day_4.prod_mode()
print(f"Part#2 Prod: {day_4.solveStep2()}")
