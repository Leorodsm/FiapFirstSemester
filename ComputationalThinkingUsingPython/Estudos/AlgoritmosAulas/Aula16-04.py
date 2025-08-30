"""
Algoritmo: Relógio Digital
"""

h = 0

while h <= 23:
    m = 0

    while m <= 59:
        s = 0

        while s <= 59:
            print(f"{h}:{m}:{s}")

            s+=1
        m+=1
    h+=1

    