class Sum:
    second: int
    first: int
    third: int
    a: int = 5
    b: int = 7

    def __init__(self, first_parameter: int, second_parameter: int) -> None:
        self.first = first_parameter
        self.second = second_parameter
        self.third = 9

    def calculate(self) -> int:
        return self.first + self.second + self.third + self.a + self.b

    def update(self) -> None:
        self.first = 18
        self.second = 22

    @classmethod
    def change(cls) -> None:
        cls.a = 8
        cls.b = 9

    @staticmethod
    def static_method() -> None:
        print('Sum is')
