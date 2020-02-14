#code
#projet jeu SCTE

username = input("Choisis ton pseudo ")
weapon = input("Maintenant choisis ton arme parmis celles-ci : ak, sniper, smg, lmg, mma, shotgun, crossbow ")



import random
b = [' mort',' en vie']
crossbow = ['raté','raté','raté','raté','raté','raté','raté','raté','réussi','raté','raté','raté','raté','raté','raté']
ak = ['']
sniper = ['']
smg = ['']
lmg = ['']
mma = ['']
shotgun = ['']
cut = ["T'es mort !", "Bien joué !", "Le trolleur trollé ! Tu t'es fait cut !","T'es mort !","T'es mort !","T'es mort !","T'es mort !","Bien joué !","Bien joué !","Bien joué !","T'es mort !","T'es mort !","T'es mort !","T'es mort !","T'es mort !","T'es mort !",]
c = random.choice(crossbow)
c = random.choice(ak)
c = random.choice(sniper)
c = random.choice(smg)
c = random.choice(lmg)
c = random.choice(mma)
c = random.choice(shotgun)
g = random.choice(cut)
a = random.randrange(1,8)

#liste evenements
z = ['ederCr surgit de derriere un mur, ','Guest_' + str(a) + ' apparait devant toi, ']
y = ["1 pour brandir ton arme, 2 pour esquiver, 3 pour le troller avec le cut","1 pour tirer, 2 pour bhop autour de lui, 3 pour le troller avec le cut"]
e = random.choice(z)
f = random.choice(y)

print("Ta premiere partie commence!")

if weapon == crossbow:
    choice = input(str(e) + str(f))
choice = input(str(e) + str(f))
if choice == '1':
    print('Tir ' + str(c) + '!')
elif choice == '2':
    print('Tir ' + str(c) + '!')
elif choice == '3':
    print(str(g))


if weapon == ak:
    choice = input(str(e) + str(f))
choice = input(str(e) + str(f))
if choice == '1':
    print()
elif choice == '2':
    print()
elif choice == '3':
    print(str(g))


if weapon == sniper:
    choice = input(str(e) + str(f))
choice = input(str(e) + str(f))
if choice == '1':
    print()
elif choice == '2':
    print()
elif choice == '3':
    print(str(g))

if weapon == smg:
    choice = input(str(e) + str(f))
choice = input(str(e) + str(f))
if choice == '1':
    print()
elif choice == '2':
    print()
elif choice == '3':
    print(str(g))

if weapon == lmg:
    choice = input(str(e) + str(f))
choice = input(str(e) + str(f))
if choice == '1':
    print()
elif choice == '2':
    print()
elif choice == '3':
    print(str(g))

if weapon == mma:
    choice = input(str(e) + str(f))
choice = input(str(e) + str(f))
if choice == '1':
    print()
elif choice == '2':
    print()
elif choice == '3':
    print(str(g))

if weapon == shotgun:
    choice = input(str(e) + str(f))
choice = input(str(e) + str(f))
if choice == '1':
    print()
elif choice == '2':
    print()
elif choice == '3':
    print(str(g))