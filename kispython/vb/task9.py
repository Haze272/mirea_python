class FSM:
    def __init__(self):
        self.A = "A"
        self.B = "B"
        self.C = "C"
        self.D = "D"
        self.E = "E"
        self.F = "F"
        self.G = "G"

        self.start = self.A
        self.current_state = self.start

    def mask(self):
        if self.current_state == self.A:
            self.current_state = self.B
            return 0
        elif self.current_state == self.B:
            self.current_state = self.C
            return 1
        elif self.current_state == self.C:
            self.current_state = self.A
            return 3
        elif self.current_state == self.F:
            self.current_state = self.B
            return 7
        elif self.current_state == self.G:
            self.current_state = self.B
            return 9
        else:
            raise KeyError

    def loop(self):
        if self.current_state == self.C:
            self.current_state = self.D
            return 2
        elif self.current_state == self.D:
            self.current_state = self.E
            return 4
        elif self.current_state == self.E:
            self.current_state = self.F
            return 5
        elif self.current_state == self.F:
            self.current_state = self.G
            return 6
        elif self.current_state == self.G:
            self.current_state = self.A
            return 8
        else:
            raise KeyError


def main():
    evaluator = FSM()

    return evaluator
