#10
from math import * 
print("Ajateisendus")
v=float(input("Sisesta aja minutites: "))
t=int(v//60)
sec=int(v%60)
print(f"minutes {t}:sekundid {sec}")
print()

#9
from math import * #Средная скорость 29,9км/ч
print("Rulluisutajad" )
print("Rulluisutaja keskmine kiirus on 29,9km/h" )
m=24/60
t=m*29.9
t=round(t,2)
print(f"Vastus: {t}km")
print()

#8
from math import * 
print("Kasutaja arvutamine")
l=float(input("Kasutaja sisestab tangitud kütuse liitrid"))
km=float(input("Kasutaja sisestab läbitud kilomeetrid"))
p=l/km*100
print(str(f"Vastus: {p}l/km"))
print()



#7
from math import * 
print("Pitsa võtsite 3 sõbraga suure pitsa hinnaga 12,90€")
s=10*12.90/100
s=round(s)
d=(12.90+s)
p=d/3
p=round(p,1)
print(f"iga sõber peab maksma: {p}€")
print()


#6
from random import * 
print("Arvutame kolnnurga ümbermõõdu")
a=randint(1,100)
b=randint(1,100)
c=randint(1,100)
print(f"Külg a={a}\nKülg b={b}\nKülg c={c}")
print(f"Kolmnnurga ümbermõõt = {a+b+c}")


#5
print(" @..@")
print("(----)")
print("(\__/)")
print("^^"'""'"^^")
print()

#4
from math import * 
A1=int(input("Sisesta 1. arv => "))
A2=int(input("Sisesta 2. arv => "))
A3=int(input("Sisesta 3. arv => "))
A4=int(input("Sisesta 4. arv => "))
A5=int(input("Sisesta 5. arv => "))
Keskmine=(A1+A2+A3+A4+A5)/5
print(f"Keskmine on {Keskmine}")
print()

#3
aeg = float(input("Mitu tundi kulus sõiduks? "))
teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
kiirus = aeg / teepikkus
print()
print("Sinu kiirus oli " + str(round) + " km/h")
print()




#2
print("Ristkülikukujulise maatüki diagonaal")
N=float(input("Sisesta ristküliku 1. külje pikkus => "))
M=float(input("Sisesta ristküliku 2. külje pikkus => "))
d=sqrt(N**2+M**2)
print(f"Maatüki diagonaal on {d} m**2")
print()



#1
from math import * 
print("Puu läbimõõdu arvutamine")
C=float(input("Puu ümbermõõt: "))
d=2*(C/(2*pi))
print(f"Vastus:\ läbimõõduga {C} ümbermõõt võrdub {d}")

