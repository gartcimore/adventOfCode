from common.Day import Day
from common.Mode import Mode
from common.Step import Step


class Day1(Day):
    _mapping = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
        "6": "6",
        "7": "7",
        "8": "8",
        "9": "9",
    }

    def __init__(self, step: Step = Step.STEP_1) -> None:
        super().__init__(1, mode=Mode.TEST, step=step)

    def getCalibrationValue(self):
        calibration_value = 0
        for current_line in day_1.raw_items:
            current_line_numbers = list(filter(str.isdigit, current_line))
            current_line_cv = int(current_line_numbers[0] + current_line_numbers[-1])
            calibration_value += current_line_cv
        return calibration_value

    def getCalibration_value_step2(self):
        calibration_value = 0
        for current_line in day_1.raw_items:
            processed_line = ""
            while len(current_line) > 0:
                for num_name, num_value in self._mapping.items():
                    if current_line.find(num_name) == 0:
                        processed_line += num_value
                        print(f"length of found {num_name} is {len(num_name)}")
                        print(f"current line is  {current_line}")
                        break
                current_line = current_line[1:]

            print(f"current line is: {processed_line}")
            current_line_numbers = list(filter(str.isdigit, current_line))
            current_line_cv = int(processed_line[0] + processed_line[-1])
            calibration_value += current_line_cv
        return calibration_value


# Part 1
day_1: Day1 = Day1(step=Step.STEP_1)
print(f"Calibration Value, Part#1 Test: {day_1.getCalibrationValue()}")
day_1.prod_mode()
print(f"Calibration Value, Part#1 Prod: {day_1.getCalibrationValue()}")

# Part 2
day_1: Day1 = Day1(step=Step.STEP_2)
print(f"Calibration Value: {day_1.getCalibration_value_step2()}")
day_1.prod_mode()
print(f"Calibration Value: {day_1.getCalibration_value_step2()}")
