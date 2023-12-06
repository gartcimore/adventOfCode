from common.Mode import Mode
from common.Step import Step


class Day:
    def __init__(self, day_name: str, mode: Mode = Mode.TEST, step: Step = Step.STEP_1, split_by: str = "\n") -> None:
        self.num: int = int("".join([char for char in list(day_name) if char.isdigit()]))
        self.mode = mode
        self.step: Step = step
        self.split_by: str = split_by
        self.raw_items: list[str] = []
        self.load_data()

    def dummy(self):
        return """ Dummy method of Day {}, running in step {} """.format(self.num, self.step)

    def load_data(self) -> None:
        # with open(f"./input{self.step.value}{'' if self.mode == Mode.PROD else '_test'}", "r") as input_file:
        with open(f"./input{'' if self.mode == Mode.PROD else '_test'}", "r") as input_file:
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
