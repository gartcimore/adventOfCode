
from common.Day import Day
from common.Mode import Mode
from common.Step import Step
import re


class Day3(Day):

    def __init__(self, step: Step = Step.STEP_1) -> None:
        super().__init__(__class__.__name__, mode=Mode.TEST, step=step)
        self.pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
        self.pattern2 = r'do\(\)|don\'t\(\)|mul\((\d{1,3}),(\d{1,3})\)'

    def step1(self):
        sol=0
        for line in self.raw_items:
            matches = re.finditer(self.pattern, line)
            for match in matches:
                sol += int(match.group(1)) * int(match.group(2))
        return sol


    def step2(self):
        do = True
        sol=0
        for line in self.raw_items:
            matches = re.finditer(self.pattern2, line)
            for match in matches:
                if(match.group(0) == "don't()"):
                    do = False
                elif (match.group(0) == "do()"):
                    do = True
                else:
                    if(do):
                        sol += int(match.group(1)) * int(match.group(2))
        return sol


# Part 1
day: Day3 = Day3(step=Step.STEP_1)
print(f"Part#1 Test: {day.step1()}")
day.prod_mode()
print(f"Part#1 Prod: {day.step1()}")


# Part 2
day: Day3= Day3(step=Step.STEP_2)
print(f"Part#2 Test: {day.step2()}")
day.prod_mode()
print(f"Part#2 Prod: {day.step2()}")
