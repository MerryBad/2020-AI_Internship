# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 23:28:06 2020

@author: user
"""

from pyswip import *

p = Prolog()

p.assertz("mamm(X) :- hair(X)") # R1
p.assertz("predator(X) :- fronteyes(X),foot(X),teeth(X),mamm(X)") # R9
p.assertz("predator(X) :- mamm(X),meat(X)") # R5
p.assertz("cheetah(X) :- mamm(X),brown(X),blackspot(X)") # R7


p.assertz('fronteyes(Sprinter)')
p.assertz('foot(Sprinter)')
p.assertz('teeth(Sprinter)')
p.assertz('hair(Sprinter)')
p.assertz('brown(Sprinter)')
p.assertz('blackspot(Sprinter)')

print('치타 맞남? : ', bool(list(p.query('cheetah(Sprinter)'))))
