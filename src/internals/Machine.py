from .Action import *
from .MachineExceptions import *
from .Head import *
from .Tape import *




class MachineBuilder:
    def __init__(self):
        self._slist         = None
        self._alphabet      = None
        self._endsym        = None
        self._initial_state = None
        self._initial_data  = None

    def __str__(self):
        brk = 20
        return (brk * '*' + "\nMachineBuilder:\n" + brk * '*' + "\n" +
                "{0}\n{1}\n{2}\n{3}\n{4}\n" + brk * '*').format(
            self.slist,
            self.endsym,
            self.alphabet,
            self.initial_state,
            self.initial_data
        )

    def _is_complete(self):
        a = self._slist and self._alphabet and self._endsym and \
            self._initial_data and self._initial_state
        return a

    # -----> begin 'alphabet' property
    # list of symbols the machine will be able to work with
    @property
    def alphabet(self):
        return self._alphabet
    @alphabet.setter
    def alphabet(self, val):
        self._alphabet = val
    # <----- end 'alphabet' property

    # -----> begin 'endsym' property
    # end symbol (default ' ') - the only one symbol
    # permitted to repeat infinitely
    @property
    def endsym(self):
        return self._endsym
    @endsym.setter
    def endsym(self, val):
        self._endsym = val
    # <----- end 'endsym' property

    # -----> begin 'initial_data' property
    # initial set of symbols on the tape
    @property
    def initial_data(self):
        return self._initial_data
    @initial_data.setter
    def initial_data(self, val):
        self._initial_data = val
    # <----- end 'initial_data' property

    # -----> begin 'initial_state' property
    # initial state of the head
    @property
    def initial_state(self):
        return self._initial_state
    @initial_state.setter
    def initial_state(self, val):
        self._initial_state = val
    # <----- end 'initial_state' property
    
    # -----> begin 'slist' property
    # list of all possible states the reader head can be in
    @property
    def slist(self):
        return self._slist
    @slist.setter
    def slist(self, val):
        self._slist = val
    # <----- end 'slist' property

    # -----> begin 'machine' property (readonly)
    # machine gets built and returned to user after some tests have been passed
    @property
    def machine(self):
        if self._is_complete():
            return Machine(
                self._slist,
                self._alphabet,
                self._endsym,
                Head(self._initial_state),
                Tape(self._initial_data, self._endsym)
            )
        else:
            raise MachineException()
    # <----- end 'machine' property

        

    

    
class Machine:
    def __init__(self, slist, alphabet, endsym, head, tape):
        self._slist, self._alphabet, self._endsym = slist, alphabet, endsym
        self._head, self._tape = head, tape
        self._running = False # controller variable

    def __str__(self):
        # return ("Machine\n{{{0}}}\n[{1}]\nendsym: '{2}'\n" +
        #         "{3}\n{4}\nrunning: {5}\nalgorithm:\n{6}").format(
        #     ", ".join(self._slist),
        #     ", ".join(self._alphabet),
        #     self._endsym,
        #     str(self._head),
        #     str(self._tape),
        #     self._running,
        #     str(self._algorithm)
        # )
        return str(self._tape)

        
    def step(self):
        self._running = self._algorithm.execute(self._tape, self._head)

    # tmp
    def run(self):
        self._start()
        while self._running:
            self.step()

    def _stop(self):
        self._running = False

    def _start(self):
        self._running = True
        

    def _check_alg(self, alg):
        return alg # TODO: implement checker for alphabet consistency

    # 'algorithm' is a resettable object
    # can be dynamically changed (in the text field in UI)
    # -----> begin
    @property
    def algorithm(self):
        return self._algorithm
    @algorithm.setter
    def algorithm(self, text):
        alg = self._check_alg(Algorithm(text))
        self._algorithm = alg
    # <----- end algorithm

