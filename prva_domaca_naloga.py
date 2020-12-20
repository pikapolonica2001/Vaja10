from math import *

hitrost=float(input('Hitrost? '))
kot=float(input('Kot? '))
g=9.78
s=((hitrost**2)*sin(2*radians(kot)))/g
print('Razdalja meta izstreljene krogle je' , s)


