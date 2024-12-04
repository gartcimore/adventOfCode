
from common.Day import Day
from common.Mode import Mode
from common.Step import Step


class Day2(Day):


    def __init__(self, step: Step = Step.STEP_1) -> None:
        super().__init__(__class__.__name__, mode=Mode.TEST, step=step)

    def check_adjacent_differences(self, line, workMode=0):
        # Split the line into items (assuming space or comma separation)
        items = line.split()

        numbers = [int(item) for item in items]

        if (self.testItems(numbers, workMode)):
            return True
        elif workMode == 0:
            return False

        for i in range(len(numbers)):
            # Create a new list without the current item
            new_numbers = numbers[:i] + numbers[i + 1:]
            if self.testItems(new_numbers, workMode, numbers[i]):
                return True

        return False



    def testItems(self, numbers, workMode=0, previous=None):
        # First check if sequence is increasing or decreasing
        is_increasing = None

        # Check first pair to determine direction
        if len(numbers) > 1:
            is_increasing = numbers[1] > numbers[0]

        for i in range(len(numbers) - 1):
            difference = abs(numbers[i] - numbers[i + 1])

            # Check if is in valid range (1-3)
            if difference < 1 or difference > 3:
                return False

            # Check direction (increasing or decreasing)
            current_increasing = numbers[i + 1] > numbers[i]
            if current_increasing != is_increasing:
                return False

        return True



    def step1(self):
        valid_count = 0
        for index, line in enumerate(self.raw_items):
            if self.check_adjacent_differences(line):
                valid_count += 1
        return valid_count

    def step2(self):
        valid_count = 0
        for index, line in enumerate(self.raw_items):
            if self.check_adjacent_differences(line,1):
                valid_count += 1
        return valid_count


# Part 1
day: Day2 = Day2(step=Step.STEP_1)
print(f"Part#1 Test: {day.step1()}")
day.prod_mode()
print(f"Part#1 Prod: {day.step1()}")


# Part 2
day: Day2= Day2(step=Step.STEP_2)
print(f"Part#2 Test: {day.step2()}")
day.prod_mode()
print(f"Part#2 Prod: {day.step2()}")
