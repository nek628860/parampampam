import math
import cmath

a1=float(input('введите модуль фазы А'))
a=float(input('введите угол фазы А'))
b1=float(input('введите модуль фазы B'))
b=float(input('введите угол фазы B'))
c1=float(input('введите модуль фазы C'))
c=float(input('введите угол фазы C'))
A=complex(a1*math.cos(math.radians(a)),a1*math.sin(math.radians(a)))
B=complex(b1*math.cos(math.radians(b)),b1*math.sin(math.radians(b)))
C=complex(c1*math.cos(math.radians(c)),c1*math.sin(math.radians(c)))
a=complex(-0.5,cmath.sqrt(3)/2)
A0=(A+B+C)/3
A1=(A+B*a+C*a*a)/3
A2=(A+B*a*a+C*a)/3
K2U=round(abs(A2)/abs(A1)*100,3)
K0U=round(abs(abs(A0)/abs(A1)*100*cmath.sqrt(3)),3)
