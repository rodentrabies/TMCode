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
        if self._initial_data:
            for i in self._initial_data:
                if not i in val:
                    raise AlphabetException()
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
        if self._alphabet:
            for i in val:
                if not i in self._alphabet:
                    raise AlphabetException()
        self._initial_data = val
    # <----- end 'initial_data' property

    # -----> begin 'initial_state' property
    # initial state of the head
    @property
    def initial_state(self):
        return self._initial_state
    @initial_state.setter
    def initial_state(self, val):
        if self._slist:
            if val not in self._slist:
                raise StateException()
        self._initial_state = val
    # <----- end 'initial_state' property
    
    # -----> begin 'slist' property
    # list of all possible states the reader head can be in
    @property
    def slist(self):
        return self._slist
    @slist.setter
    def slist(self, val):
        if self._initial_state:
            if self._initial_state not in val:
                raise StateException()
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
            raise IncompleteMachineException()
    # <----- end 'machine' property

        

    

    
class Machine:
    def __init__(self, slist, alphabet, endsym, head, tape):
        self._slist, self._alphabet, self._endsym = slist, alphabet, endsym
        self._head, self._tape = head, tape
        self.running = False # controller variable

    def __str__(self):
        return str(self._tape)
        
    def step(self):
        self.running = self._algorithm.execute(self._tape, self._head)

    def stop(self):
        self.running = False

    def start(self):
        self.running = True
        
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

    # 'current_symbol' - just a piece of useful information
    # -----> begin
    @property
    def current_symbol(self):
        return self._tape._current
    # <----- end current_symbol


    # 'current_inst' - insruction whose pattern just matched
    # -----> begin
    @property
    def current_inst(self):
        return self._algorithm._last_inst
