import math

from common.Day import Day
from common.Mode import Mode
from common.Step import Step





class Day5(Day):

    def __init__(self, step: Step = Step.STEP_1) -> None:
        super().__init__(__class__.__name__, mode=Mode.TEST, step=step)

    def extractSeeds(self):
        # match = re.search(r'seeds: (\d+)+', self.raw_items[0])
        # print(f" found seeds {match.groups()}")
        # return match.groups()
        # seeds = self.raw_items[0].split(':')[1]
        # print(f" found seeds {seeds.strip()}")

        return list(map(int, (self.raw_items[0].split(":")[1].strip().split(" "))))


    def solveStep1(self):

        seeds = self.extractSeeds()

        lowest_location = math.inf
        for seed in seeds:
            working = seed
            token = ""
            print("\nseed "+str(seed)+" =>", end=" ")
            matched = False
            for line in self.raw_items:
                if "seeds" in line:
                    pass
                elif "map" in line:
                    token = line.split()[0]
                    matched = False
                    print(token, end=" ")
                elif not matched:
                    destination, source, ranch = list(map(int, line.split()))
                    if source <= working <= source + ranch:
                        working += destination - source
                        print(str(working)+" =>", end=" ")
                        matched = True

            if(lowest_location > working):
                lowest_location = working
            print(f"\nseed {seed} => {working}")

        return lowest_location



# Part 1
day_5: Day5 = Day5(step=Step.STEP_1)
print(f"Part#1 Test: {day_5.solveStep1()}")
day_5.prod_mode()
print(f"Part#1 Prod: {day_5.solveStep1()}")


# Part 2
day_5: Day5= Day5(step=Step.STEP_2)
print(f"Part#2 Test: {day_5.dummy()}")
day_5.prod_mode()
print(f"Part#2 Prod: {day_5.dummy()}")
