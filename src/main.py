from internals.Machine import *

builder = MachineBuilder()

builder.alphabet = 'abcd'
builder.slist = ['q1', 'q2', 'q3']
builder.endsym = ' '
builder.initial_state = 'q1'
builder.initial_data = 'abbbbd'

machine = builder.machine
#print(machine)

code = """q1, 'a' -> q1, 'a', R;
          q1, 'b' -> q1, 'c', R;
          q1, 'd' -> q2, 'd', L;
          q2, 'c' -> q2, 'c', L;
          q2, 'a' -> q3, 'a', N;

       """
machine.algorithm = code
print(machine)
machine.run()
print(machine)
