
from common.Day import Day
from common.Mode import Mode
from common.Step import Step


class Day4(Day):


    def __init__(self, step: Step = Step.STEP_1) -> None:
        super().__init__(__class__.__name__, mode=Mode.TEST, step=step)

    def step1(self):
        sol = 0
        rows, cols = len(self.raw_items), len(self.raw_items[0])
        for row in range(rows):
            for col in range(cols):
                if col+3 < cols and self.raw_items[row][col]== "X" and self.raw_items[row][col+1]== "M" and self.raw_items[row][col+2]== "A" and self.raw_items[row][col+3]== "S":
                    sol +=1
                if row+3 < rows and self.raw_items[row][col]== "X" and self.raw_items[row+1][col]== "M" and self.raw_items[row+2][col]== "A" and self.raw_items[row+3][col]== "S":
                    sol +=1
                if row+3 < rows and col+3 < cols and self.raw_items[row][col]== "X" and self.raw_items[row+1][col+1]== "M" and self.raw_items[row+2][col+2]== "A" and self.raw_items[row+3][col+3]== "S":
                    sol +=1

                if col+3 < cols and self.raw_items[row][col]== "S" and self.raw_items[row][col+1]== "A" and self.raw_items[row][col+2]== "M" and self.raw_items[row][col+3]== "X":
                    sol +=1
                if row+3 < rows and self.raw_items[row][col]== "S" and self.raw_items[row+1][col]== "A" and self.raw_items[row+2][col]== "M" and self.raw_items[row+3][col]== "X":
                    sol +=1
                if row+3 < rows and col+3 < cols and self.raw_items[row][col]== "S" and self.raw_items[row+1][col+1]== "A" and self.raw_items[row+2][col+2]== "M" and self.raw_items[row+3][col+3]== "X":
                    sol +=1
                if row-3 >= 0 and col+3 < cols and self.raw_items[row][col]== "S" and self.raw_items[row-1][col+1]== "A" and self.raw_items[row-2][col+2]== "M" and self.raw_items[row-3][col+3]== "X":
                    sol +=1
                if row-3 >= 0 and col+3 < cols and self.raw_items[row][col]== "X" and self.raw_items[row-1][col+1]== "M" and self.raw_items[row-2][col+2]== "A" and self.raw_items[row-3][col+3]== "S":
                    sol +=1

        return sol

    def step2(self):
        sol = 0
        rows, cols = len(self.raw_items), len(self.raw_items[0])
        for row in range(rows):
            for col in range(cols):
                if row+2<rows and col+2<cols and self.raw_items[row][col]=='M' and self.raw_items[row+1][col+1]=='A' and self.raw_items[row+2][col+2]=='S' and self.raw_items[row+2][col]=='M' and self.raw_items[row][col+2]=='S':
                    sol += 1
                if row+2<rows and col+2<cols and self.raw_items[row][col]=='M' and self.raw_items[row+1][col+1]=='A' and self.raw_items[row+2][col+2]=='S' and self.raw_items[row+2][col]=='S' and self.raw_items[row][col+2]=='M':
                    sol += 1
                if row+2<rows and col+2<cols and self.raw_items[row][col]=='S' and self.raw_items[row+1][col+1]=='A' and self.raw_items[row+2][col+2]=='M' and self.raw_items[row+2][col]=='M' and self.raw_items[row][col+2]=='S':
                    sol += 1
                if row+2<rows and col+2<cols and self.raw_items[row][col]=='S' and self.raw_items[row+1][col+1]=='A' and self.raw_items[row+2][col+2]=='M' and self.raw_items[row+2][col]=='S' and self.raw_items[row][col+2]=='M':
                    sol += 1

        return sol


# Part 1
day: Day4 = Day4(step=Step.STEP_1)
print(f"Part#1 Test: {day.step1()}")
day.prod_mode()
print(f"Part#1 Prod: {day.step1()}")


# Part 2
day: Day4= Day4(step=Step.STEP_2)
print(f"Part#2 Test: {day.step2()}")
day.prod_mode()
print(f"Part#2 Prod: {day.step2()}")
