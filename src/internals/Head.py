class Head:
    def __init__(self, st):
        self.state = st

    def __str__(self):
        return "<{0}>".format(self.state)


    
    def read_from_tape(self, tape):
        return tape.current_cell

    def write_to_tape(self, tape, val):
        tape.current_cell = val

    def move_tape_left(self, tape):
        tape.shift_left()

    def move_tape_right(self, tape):
        tape.shift_right()
        
