class ProblemSolver:
    def __init__(self, i2s, d):
        self.i2s = i2s()
        self.d = d()

    def solve(self):
        for i in range(1, 100):
            val = self.i2s.convert(i)
            self.d.display(val)
        return True


class Int2String:
    def convert(self, number):
        raise NotImplementedError  # pragma: no cover


class Displayer:
    def display(self, s):
        raise NotImplementedError  # pragma: no cover
