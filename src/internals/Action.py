#-------------------------------------------------------------------------------
# Action description representation
#-------------------------------------------------------------------------------
class Action:
    """
    Base class for Instruction and Algorithm classes Composite structure;
    """
    def match(self, tape, head):
        pass
    
    def execute(self, tape, head):
        pass
#-------------------------------------------------------------------------------





#-------------------------------------------------------------------------------
class Instruction(Action):
    """
    Instructions are read from text field in the form:
        <state>, <symbol> -> <new state>, <new symbol>, <shift>;
    Example:
        q1, 'a' -> q1, 'b', L;
        This means, that if in state q1 found 'a' then replace it
        with 'b', change state to q2 and shift the head to the left.
    """
    def __init__(self, num, inst):
        def quoted(s):
            return s[0] == s[-1] == "'"
        spl = inst.split('->')
        if len(spl) != 2:
            raise ValueError("[TMERR]: bad instructions {0}".format(inst))
        pre, post = [list(map(str.strip, i.strip().split(','))) for i in spl]
        if (len(pre) != 2 or len(post) != 3
            or not quoted(pre[1]) or not quoted(post[1])):
            raise ValueError("[TMERR]: bad instruction: {0}".format(inst))
        pre[1], post[1] = pre[1][1:-1], post[1][1:-1]
        self._ist, self._isym, self._ost, self._osym, self._mov = pre + post
        self._text = inst # save original text for syntax highlight


    def __str__(self):
        return self._text

    
    def match(self, tape, head):
        if head.state == self._ist and head.read_from_tape(tape) == self._isym:
            return True
        else:
            return False
        

    def execute(self, tape, head):
        head.write_to_tape(tape, self._osym)
        head.state = self._ost
        if self._mov == 'L':
            head.move_tape_right(tape)
        elif self._mov == 'R':
            head.move_tape_left(tape)
        return self._text
#-------------------------------------------------------------------------------





#-------------------------------------------------------------------------------
class Algorithm(Action):
    """
    Algorithm is a Composite Action that can be named and
    executed linearly by calling it's name in the code;
    basically is a collection of Instructions;
    """
    def __init__(self, text):
        insts, spt, self._last_inst = [], ['', text], None
        while spt[1].strip() != '':
            spt = spt[1].strip().split(';', maxsplit = 1)
            if len(spt) == 1: raise ValueError("missed ';'")
            else: insts.append(spt[0].strip())
        try:
            self._ilist = [Instruction(n, i) for n, i in enumerate(insts)]
        except ValueError as e:
            raise ValueError(e)

        
    def __str__(self):
        return ";\n".join(map(str, self._ilist)) + ';'

        
    def execute(self, tape, head):
        """
        One time run through all the instructions;
        return True if executed instruction, and False otherwise
        """
        for i in self._ilist:
            if i.match(tape, head):
                self._last_inst = i.execute(tape, head)
                return True
        return False
#-------------------------------------------------------------------------------
