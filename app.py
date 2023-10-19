class Square:
    def __init__(self, height: int, width: int):
        self.height = height
        self.width = width

    def area(self) -> int:
        return self.height * self.width

    def perimeter(self) -> int:
        return 2 * self.height + 2 * self.width

    def __str__(self) -> str:
        return f"Square(height={self.height}, width={self.width})"

    def __repr__(self) -> str:
        return f"Square({self.height}, {self.width})"
