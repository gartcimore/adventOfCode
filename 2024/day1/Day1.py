
from common.Day import Day
from common.Mode import Mode
from common.Step import Step


class Day1(Day):


    def __init__(self, step: Step = Step.STEP_1) -> None:
        super().__init__(__class__.__name__, mode=Mode.TEST, step=step)

    def solveStep1(self):
        LeftCol = []
        RightCol = []

        for index, line in enumerate(self.raw_items):
            left,right = line.split()
            left,right = int(left),int(right)
            LeftCol.append(left)
            RightCol.append(right)
        sol = 0
        LeftCol.sort()
        RightCol.sort()
        for left, right in zip(LeftCol, RightCol):
            sol += abs(right - left)
        return sol

    def solveStep2(self):
        LeftCol = []
        RightCol = []

        for index, line in enumerate(self.raw_items):
            # print(f"line: {line}")
            left,right = line.split()
            # print(f"Split: {left}, {right}")
            left,right = int(left),int(right)
            LeftCol.append(left)
            RightCol.append(right)
        sol = 0

        for index, left in enumerate(LeftCol):
            times = 0
            for right in RightCol:
                if(right == left):
                    times += 1
            sol += (times * left)
        return sol



# Part 1
day: Day1 = Day1(step=Step.STEP_1)
print(f"Part#1 Test: {day.solveStep1()}")
day.prod_mode()
print(f"Part#1 Prod: {day.solveStep1()}")


# Part 2
day: Day1= Day1(step=Step.STEP_2)
print(f"Part#2 Test: {day.solveStep2()}")
day.prod_mode()
print(f"Part#2 Prod: {day.solveStep2()}")
