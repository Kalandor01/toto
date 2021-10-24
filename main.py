import random

# változók
ran = random
nyer = ""
tipp_n = 14
talal = []
talal_10 = 0
talal_11 = 0
talal_12 = 0
talal_13 = 0
talal_14 = 0
jatekos_tip = []

# nyeremény
for j in range(tipp_n):
    szam = ran.randint(1, 3)
    if szam == 3:
        nyer += "X"
    else:
        nyer += str(szam)

# játékosok száma
try:
    jatekos_n = int(input("\nKérem a totójátékosok számát: "))
except ValueError:
    jatekos_n = 0
print()

# nem jó szám
if jatekos_n < 1:
    print("Nem jó szám!")

# játékosok tipjei
else:
    if jatekos_n > 100000:
        print("Tippek bekérése:")
    for i in range(jatekos_n):
        # százalék
        if jatekos_n > 100000:
            if i % (round(jatekos_n / 100)) == 0:
                if round(i / (jatekos_n / 100)) >= 99:
                    print("\rKész!", end="")
                else:
                    print("\r" + str(round(i / (jatekos_n / 100))) + "%", end="")
        jatekos_tip.append("")
        for j in range(tipp_n):
            szam = ran.randint(1, 3)
            if szam == 3:
                jatekos_tip[i] += "X"
            else:
                jatekos_tip[i] += str(szam)

    # mennyit találtak el
    if jatekos_n > 100000:
        print("\n\nTalálatok kiszámítása: ")
    for i in range(jatekos_n):
        # százalék
        if jatekos_n > 100000:
            if i % (round(jatekos_n / 100)) == 0:
                if round(i / (jatekos_n / 100)) >= 99:
                    print("\rKész!", end="")
                else:
                    print("\r" + str(round(i / (jatekos_n / 100))) + "%", end="")
        talal.append(0)
        for j in range(tipp_n - 1):
            if nyer[j] == jatekos_tip[i][j]:
                talal[i] += 1
        if talal[i] == (tipp_n - 1) and nyer[tipp_n - 1] == jatekos_tip[i][tipp_n - 1]:
            talal[i] += 1
        # print(str(jatekos_tip[i]) + ": " + str(talal[i]))
        if talal[i] == tipp_n - 4:
            talal_10 += 1
        if talal[i] == tipp_n - 3:
            talal_11 += 1
        if talal[i] == tipp_n - 2:
            talal_12 += 1
        if talal[i] == tipp_n - 1:
            talal_13 += 1
        if talal[i] == tipp_n:
            talal_14 += 1

    # nyertesek
    if jatekos_n > 100000:
        print("\n")
    print("Nyerő számok: " + nyer)
    # 10
    if talal_10 > 0:
        print("\n10-es találatok: " + str(talal_10))
        for i in range(jatekos_n):
            if talal[i] == tipp_n - 4:
                print(str(i + 1) + ".: " + str(jatekos_tip[i]))
    # 11
    if talal_10 > 0:
        print("\n11-es találatok: " + str(talal_10))
        for i in range(jatekos_n):
            if talal[i] == tipp_n - 3:
                print(str(i + 1) + ".: " + str(jatekos_tip[i]))
    # 12
    if talal_10 > 0:
        print("\n12-es találatok: " + str(talal_10))
        for i in range(jatekos_n):
            if talal[i] == tipp_n - 2:
                print(str(i + 1) + ".: " + str(jatekos_tip[i]))
    # 13
    if talal_10 > 0:
        print("\n13-as találatok: " + str(talal_10))
        for i in range(jatekos_n):
            if talal[i] == tipp_n - 1:
                print(str(i + 1) + ".: " + str(jatekos_tip[i]))
    # 14
    if talal_10 > 0:
        print("\n14-es találatok: " + str(talal_10))
        for i in range(jatekos_n):
            if talal[i] == tipp_n:
                print(str(i + 1) + ".: " + str(jatekos_tip[i]))
    # nincs nyertes
    if talal_10 == 0 and talal_11 == 0 and talal_12 == 0 and talal_13 == 0 and talal_14 == 0:
        print("Nincs nyertes!")


"""""
print("hurara")
for x in range(99999999):
    if x % 100000 == 0:
        print("\r" + str(x), end="")
print()
print("hurare")
"""""
