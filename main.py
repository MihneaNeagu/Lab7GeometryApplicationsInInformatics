import numpy as np
import math as m

def deBoorDerivata(t, x, n, pc, g):
    """
    t: nodului lui x
    x: pozitia
    n: lista de noduri
    pc: lista de puncte de control
    g: gradul curbei B-spline
    """
    q = [g * (pc[j + t - g + 1] - pc[j + t - g]) / (n[j + t + 1] - n[j + t - g + 1]) for j in range(0, g)]

    for r in range(1, g):
        for j in range(g - 1, r - 1, -1):
            right = j + 1 + t - r
            left = j + t - (g - 1)
            alpha = (x - n[left]) / (n[right] - n[left])
            q[j] = (1.0 - alpha) * q[j-1] + alpha * q[j]

    return q[g - 1]

def main():
    while True:
        print("1. Dati punctele de control: ")
        print("2. Dati nodurile : ")
        print("3. Dati t : ")
        print("4. Afiseaza r(t): ")
        print("x. Iesire")

        optiune = input("Dati optiunea: ")

        if optiune == "1":
            list1 = []
            for i in range(0, 5):
                a = float(input("Dati coordonata x a punctului: "))
                b = float(input("Dati coordonata y a punctului: "))
                list1.append([a, b])
        elif optiune == "2":
            list2 = []
            for i in range(0, 8):
                print("Dati enter dupa introducerea nodului: ")
                ele2 = float(input())
                list2.append(ele2)
        elif optiune == "3":
            t = int(input("Dati t:"))
        elif optiune == "4":
            g = 3
            x = 0.5
            puncte = np.array(list1)
            noduri = np.array(list2)
            print("De Boor:", deBoorDerivata(t, x, noduri, puncte, g))
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")

    #puncte = np.array([[i, m.sin(i / 3.0), m.cos(i / 2)] for i in range(0, 11)])
    #noduri = np.array([0, 0, 0, 0, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 1.0, 1.0, 1.0, 1.0])
    #print("De Boor:", deBoorDerivata(t, x, noduri, puncte, g))

main()

