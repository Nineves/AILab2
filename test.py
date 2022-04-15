from pyswip import *

prolog = Prolog()

prolog.consult("Agent.pl")



list(prolog.query("reposition([on,off,off,off,off,off])"))

print(list(prolog.query("explore(L)")))