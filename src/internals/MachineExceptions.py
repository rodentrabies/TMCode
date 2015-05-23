# Machine error classes
from .Machine import *



# base class
class MachineException(Exception):
    """
    Exception to throw when bad configuration given
    (for example, inconsistency between alphabet and data).
    """
    pass
    
class AlphabetException(MachineException): pass
    
class StateException(MachineException): pass

class IncompleteMachineException(MachineException): pass

class InstructionException(MachineException): pass
