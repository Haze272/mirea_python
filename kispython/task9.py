class FSM:
    def __init__(self):
        self.A = "A"
        self.B = "B"
        self.C = "C"
        self.D = "D"
        self.E = "E"
        self.F = "F"

        self.start = self.A
        self.current_state = self.start

    def peep(self):
        if self.current_state == self.B:
            self.current_state = self.C
            return 1
        elif self.current_state == self.C:
            self.current_state = self.D
            return 2
        elif self.current_state == self.D:
            self.current_state = self.B
            return 4
        elif self.current_state == self.E:
            self.current_state = self.F
            return 5
        elif self.current_state == self.F:
            self.current_state = self.A
            return 7
        else:
            return KeyError

    def mix(self):
        if self.current_state == self.A:
            self.current_state = self.B
            return 0
        elif self.current_state == self.D:
            self.current_state = self.E
            return 3
        elif self.current_state == self.E:
            self.current_state = self.B
            return 6
        elif self.current_state == self.F:
            self.current_state = self.B
            return 8
        else:
            return KeyError


def main():
    evaluator = FSM()

    return evaluator

'''
o = main()
o.mix()  # 0
o.mix()  # KeyError
o.peep()  # 1
o.peep()  # 2
o.peep()  # 4
o.peep()  # 1
o.peep()  # 2
o.mix()  # 3
o.peep()  # 5
o.mix()  # 8
o.peep()  # 1
o.peep()  # 2
o.peep()  # 4
'''
'''
o = main()
print(o.mix())  # 0
print(o.mix())  # KeyError
print(o.peep())  # 1
print(o.peep())  # 2
print(o.peep())  # 4
print(o.peep())  # 1
print(o.peep())  # 2
print(o.mix())  # 3
print(o.peep())  # 5
print(o.mix())  # 8
print(o.peep())  # 1
print(o.peep())  # 2
print(o.peep())  # 4
'''
'''
o = main()
print(o.mix())  # 0
print(o.peep())  # 1
print(o.mix())  # KeyError
print(o.peep())  # 2
print(o.peep())  # 4
print(o.peep())  # 1
print(o.peep())  # 2
print(o.mix())  # 3
print(o.peep())  # 5
print(o.peep())  # 7
print(o.mix())  # 0
print(o.mix())  # KeyError
print(o.peep())  # 1
'''
o = main()
print(o.mix())
print(o.mix())
print(o.peep())