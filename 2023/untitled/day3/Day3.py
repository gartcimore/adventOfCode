from functools import reduce

from common.Day import Day
from common.Mode import Mode
from common.Step import Step


class Day3(Day):

    symbols = {}

    def __init__(self, step: Step = Step.STEP_1) -> None:
        super().__init__(3, mode=Mode.TEST, step=step)


    def createSymbolMap(self):
        self.symbols = {}
        for line_index, line in enumerate(self.raw_items):
            for index, char in enumerate(line):
                char_as = ""+char
                if(char_as.isdigit() == False):
                    if(char != '.'):
                        print(f"char {char} is a symbol")
                        self.symbols[f"{line_index},{index}"] = char



    def checkIfNearSymbol(self, line_index, index):
        print(f"check for {self.raw_items[line_index][index]}")
        if(f"{line_index-1},{index-1}" in self.symbols ):
            # print(f"near a symbol at -1,-1 {line_index},{index}")
            if(self.step == Step.STEP_1):
                return True
            else:
                if(self.symbols[f"{line_index-1},{index-1}"] == "*"):
                    print(f"it's a gear")
                    return f"{line_index-1},{index-1}"
        elif(f"{line_index-1},{index}" in self.symbols):
            # print(f"near a symbol at -1,- {line_index},{index}")
            if(self.step == Step.STEP_1):
                return True
            else:
                if(self.symbols[f"{line_index-1},{index}"] == "*"):
                    print(f"it's a gear")
                    return f"{line_index-1},{index}"
        elif(f"{line_index-1},{index+1}" in self.symbols):
            # print(f"near a symbol at -1,+1 {line_index},{index}")
            if(self.step == Step.STEP_1):
                return True
            else:
                if(self.symbols[f"{line_index-1},{index+1}"] == "*"):
                    print(f"it's a gear")
                    return f"{line_index-1},{index+1}"
        elif(f"{line_index},{index-1}" in self.symbols):
            # print(f"near a symbol at -,-1 {line_index},{index}")
            if(self.step == Step.STEP_1):
                return True
            else:
                if(self.symbols[f"{line_index},{index-1}"] == "*"):
                    print(f"it's a gear")
                    return f"{line_index},{index-1}"
        elif(f"{line_index},{index+1}" in self.symbols):
            # print(f"near a symbol at -,+1 {line_index},{index}")
            if(self.step == Step.STEP_1):
                return True
            else:
                if(self.symbols[f"{line_index},{index+1}"] == "*"):
                    print(f"it's a gear")
                    return f"{line_index},{index+1}"
        elif(f"{line_index+1},{index-1}" in self.symbols):
            # print(f"near a symbol at +1,-1 {line_index},{index}")
            if(self.step == Step.STEP_1):
                return True
            else:
                if(self.symbols[f"{line_index+1},{index-1}"] == "*"):
                    print(f"it's a gear")
                    return f"{line_index+1},{index-1}"
        elif(f"{line_index+1},{index}" in self.symbols):
            # print(f"near a symbol at +1,- {line_index},{index}")
            if(self.step == Step.STEP_1):
                return True
            else:
                if(self.symbols[f"{line_index+1},{index}"] == "*"):
                    print(f"it's a gear")
                    return f"{line_index+1},{index}"
        elif(f"{line_index+1},{index+1}" in self.symbols):
            # print(f"near a symbol at +1,+1 {line_index},{index}")
            if(self.step == Step.STEP_1):
                return True
            else:
                # print(f"it's step {self.step}")
                symbol_index = f"{line_index+1},{index+1}"
                # print(f"symbol {self.symbols[symbol_index]}")
                if(self.symbols[f"{line_index+1},{index+1}"] == "*"):
                    print(f"it's a gear")
                    return f"{line_index+1},{index+1}"

        # else:
            # print(f"NOT near a symbol for {line_index},{index}")

        return False

    def solveStep1(self):
        self.createSymbolMap()

        sum = 0
        for line_index, line in enumerate(self.raw_items):
            current_number = 0
            should_sum = False
            for index, char in enumerate(line):
                char_as = ""+char
                if(char_as.isdigit()):
                    # check if a symbol is near this
                    if(should_sum == False):
                        should_sum = self.checkIfNearSymbol(line_index, index)
                    current_number = int(str(current_number)+char)
                else:
                    if(should_sum):
                        print(f"summing  sum: {sum} with current_number {current_number}")
                        sum += current_number
                    current_number = 0
                    should_sum = False
            if(should_sum):
                print(f"summing  sum: {sum} with current_number {current_number}")
                sum += current_number
        return sum


    def solveStep2(self):
        self.createSymbolMap()
        sum = 0
        gears = {}

        for line_index, line in enumerate(self.raw_items):
            current_number = 0
            gear_found = False
            for index, char in enumerate(line):
                char_as = ""+char
                if(char_as.isdigit()):
                    # check if a symbol is near this and is a gear
                    if(gear_found == False):
                        gear_found = self.checkIfNearSymbol(line_index, index)
                    current_number = int(str(current_number)+char)
                else:
                    if(gear_found):
                        print(f"found a gear at {gear_found}")
                        if gear_found in gears:
                            # print(f"already exists, append with {current_number}")
                            existing = gears[gear_found]
                            # print(f"existing is {existing}")
                            existing.append(current_number)
                            gears[gear_found] = existing
                        else:
                            gears[gear_found] = [current_number]
                            # print(f"gear ration stored  {gears[gear_found]}")
                    current_number = 0


                    gear_found = False
            if(gear_found):
                if gear_found in gears:
                    # print(f"already exists, append with {current_number}")
                    existing = gears[gear_found]
                    # print(f"existing is {existing}")
                    existing.append(current_number)
                    gears[gear_found] = existing
                else:
                    gears[gear_found] = [current_number]
                    # print(f"gear ration stored  {gears[gear_found]}")

        for gear in gears:
            if(len(gears[gear])>1):
                sum += reduce(lambda a,b: a*b, gears[gear])
        return sum


# Part 1
day_3: Day3 = Day3(step=Step.STEP_1)
print(f"Part#1 Test: {day_3.solveStep1()}")
day_3.prod_mode()
print(f"Part#1 Prod: {day_3.solveStep1()}")


# Part 2
day_3: Day3 = Day3(step=Step.STEP_2)
print(f"Part#2 Test: {day_3.solveStep2()}")
day_3.prod_mode()
print(f"Part#2 Prod: {day_3.solveStep2()}")
