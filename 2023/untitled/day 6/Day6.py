from collections import defaultdict
from math import prod

from common.Day import Day
from common.Mode import Mode
from common.Step import Step


class Day6(Day):

    def __init__(self, step: Step = Step.STEP_1) -> None:
        super().__init__(__class__.__name__, mode=Mode.TEST, step=step)

    def solveStep1(self):
        times = [int(t) for t in self.raw_items[0].split(":")[1].strip().split()]
        best_distances = [int(d) for d in self.raw_items[1].split(":")[1].strip().split()]
        possible_winnings = defaultdict(int)
        for race_index in range(len(times)):
            # print(f"Race #{race_index + 1}, d: {best_distances[race_index]}mm / t: {times[race_index]}ms")
            for hold_time in range(times[race_index]):
                remaining_time = times[race_index] - hold_time
                distance = remaining_time * hold_time
                # print(f"hold: {hold_time}, remaining: {remaining_time}, distance: {distance}")
                if distance > best_distances[race_index]:
                    possible_winnings[race_index] += 1
        # print(f"possible winnings: {possible_winnings.values()}")
        return prod(possible_winnings.values())

    def solveStep2(self):
        time = int(self.raw_items[0].split(":")[1].strip().replace(" ",""))
        best_distance = int(self.raw_items[1].split(":")[1].strip().replace(" ",""))

        possible_winnings = defaultdict(int)
        start = 0
        if (time % 2) == 0:
            start = time / 2
            print(f"start is {start} because even")
        else:
            start = (time -1) / 2
            print(f"start is {start} because odd")

        winning = True
        win_count = 0
        hold_time = start -1
        while winning:
            remaining_time = time - hold_time
            distance = remaining_time * hold_time
            # print(f"hold: {hold_time}, remaining: {remaining_time}, distance: {distance}")
            if distance > best_distance:
                win_count += 1
                hold_time -= 1
            else:
                winning = False
                print(f"hold time {hold_time}")
        print(f"{start - 1 } => {hold_time + 1} == {start - hold_time }")

        return win_count*2 + 1
        # # print(f"possible winnings: {possible_winnings.values()}")
        # return prod(possible_winnings.values())

# Part 1
day: Day6 = Day6(step=Step.STEP_1)
print(f"Part#1 Test: {day.solveStep1()}")
day.prod_mode()
print(f"Part#1 Prod: {day.solveStep1()}")


# Part 2
day: Day6= Day6(step=Step.STEP_2)
print(f"Part#2 Test: {day.solveStep2()}")
day.prod_mode()
print(f"Part#2 Prod: {day.solveStep2()}")
