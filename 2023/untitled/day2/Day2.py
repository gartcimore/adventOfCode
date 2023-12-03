import re

from common.Day import Day
from common.Mode import Mode
from common.Step import Step


class Day2(Day):

    _max_red = 12
    _max_blue = 14
    _max_green = 13

    def __init__(self, step: Step = Step.STEP_1) -> None:
        super().__init__(1, mode=Mode.TEST, step=step)



    def getSumOfGameIDs(self):
        sum = 0

        for current_line in day_2.raw_items:
                matchs = re.search(r'Game (\d+)', current_line)
                game_id = matchs.group(1)
                all_blue = re.findall(r'\d+ blue', current_line)

                valid_game = True
                for blue in all_blue:
                    value = blue.split()[0]
                    if int(value) > self._max_blue:
                        print(f"discard this game because of blue value {value} is > {self._max_blue}")
                        valid_game = False

                all_green = re.findall(r'\d+ green', current_line)
                for green in all_green:
                    value = green.split()[0]
                    if int(value) > self._max_green:
                        print(f"discard this game because of green value {value} is > {self._max_green}")
                        valid_game = False

                all_red = re.findall(r'\d+ red', current_line)
                for red in all_red:
                    value = red.split()[0]
                    if int(value) > self._max_red:
                        print(f"discard this game because of red value {value} is > {self._max_red}")
                        valid_game = False

                if(valid_game):
                    print(f"valid game, adding id {game_id} to {sum}")
                    sum += int(game_id)

        return sum

    def getSumPower(self):
        sum = 0

        for current_line in day_2.raw_items:
            matchs = re.search(r'Game (\d+)', current_line)
            game_id = matchs.group(1)
            all_blue = re.findall(r'\d+ blue', current_line)

            max_blue = 0
            max_red = 0
            max_green = 0
            for blue in all_blue:
                value = blue.split()[0]
                if int(value) > max_blue:
                    max_blue = int(value)


            all_green = re.findall(r'\d+ green', current_line)
            for green in all_green:
                value = green.split()[0]
                if int(value) > max_green:
                    max_green = int(value)

            all_red = re.findall(r'\d+ red', current_line)
            for red in all_red:
                value = red.split()[0]
                if int(value) > max_red:
                    max_red = int(value)

            sum += max_blue * max_red * max_green

        return sum


# Part 1
day_2: Day2 = Day2(step=Step.STEP_1)
print(f"sum of game ids, Part#1 Test: {day_2.getSumOfGameIDs()}")
day_2.prod_mode()
print(f"sum of game ids, Part#1 Prod: {day_2.getSumPower()}")

# Part 2
day_2: Day2 = Day2(step=Step.STEP_2)
print(f"Sums of power: {day_2.getSumPower()}")
day_2.prod_mode()
print(f"Sums of power: {day_2.getSumPower()}")