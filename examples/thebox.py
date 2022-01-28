from meshi import *

w = 100
l = 180
h = 30

wallW = 2
plateW = 1.5

init()

a = Box(w, l, h)
Box(w-wallW, l-wallW, h).move(z=plateW).substractFrom(a)
