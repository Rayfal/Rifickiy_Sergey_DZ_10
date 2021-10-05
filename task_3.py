class Cell:
    def __init__(self, nums):
        self.nums = nums
    def make_order(self, rows):
        return' \n '. join(['*' * rows for _ in range(self.nums // rows)]) \
               + '\n' + '*' * (self.nums%rows)
    def __add__(self, other):
        return str(self.nums + other.nums)
    def __sub__(self, other):
        return str(self.nums - other.nums)
    def __mul__(self, other):
        return str(self.nums * other.nums)
    def __floordiv__(self, other):
        return str(self.nums // other.nums)


work1 = Cell(40)
work2 = Cell(50)
print(work1.make_order(10))
print(work1 + work2)
print(work1 - work2)
print(work1 * work2)
print(work1 // work2)