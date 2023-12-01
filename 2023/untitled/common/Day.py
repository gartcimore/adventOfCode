from common.Mode import Mode
from common.Step import Step


class Day:
    def __init__(self, day_number: int, mode: Mode = Mode.TEST, step: Step = Step.STEP_1, split_by: str = "\n") -> None:
        self.num: int = day_number
        self.mode = mode
        self.step: Step = step
        self.split_by: str = split_by
        self.raw_items = []
        self.load_data()

    def load_data(self) -> None:
        with open(f"./input{self.step.value}{'' if self.mode == Mode.PROD else '_test'}", "r") as input_file:
            self.raw_items = [item for item in input_file.read().split(self.split_by) if len(item.strip()) > 0]

    def display(self):
        for item in self.raw_items:
            print(item)

    def set_mode(self, mode=Mode.TEST):
        self.mode = mode
        self.load_data()

    def prod_mode(self):
        self.set_mode(Mode.PROD)

    def test_mode(self):
        self.set_mode(Mode.TEST)
