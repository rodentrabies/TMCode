# Machine error classes
from .Machine import *



# base class
class MachineException(Exception):
    """
    Exception to throw when bad configuration given
    (for example, inconsistency between alphabet and data).
    """
    # Template Methon pattern used
    @property # override default property
    def message(self):
        return "[MACHINE ERROR]" + self._msg()

    def _msg(self):
        return "incomplete machine configuration"





    
class AlphabetException(MachineException):
    """
    Inconsistence in alphabet symbols.
    """
    def __init__(self, s, a):
        self._symbol, self._alphabet = s, a

    def _msg(self):
        return "there is no symbol {0} in the alpabet {1}".format(
            self._symbol,
            self._alphabet
        )

    


    
class StateException(MachineException):
    """
    Unsupported state error.
    """
    def __init__(self, state, slist):
        self._state, self._slist = state, slist

    def _msg(self):
        return "unknown state {0} (list supported: {1})".format(
            self._state,
            ", ".join(self._slist)
        )
