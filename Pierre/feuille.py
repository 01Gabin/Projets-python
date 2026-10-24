import random

while True:

    try:
        manches = int(input("Combien de manches voulez-vous jouer ? : "))
        if manches > 0:
            break
    except ValueError:
        print("Veuillez ecrire un nombre entier.")


score_hero = 0
score_ordi = 0

options = ["P", "F", "C"]

while score_hero < manches and score_ordi < manches:

    while True:
            choix_joueur = input("Que jouez-vous ? [P]ierre, [F]euille, [C]iseaux : ").upper()
            if choix_joueur in options:
                break
            print("Veuillez choisir parmi P, F et C.")

    choix_ordi = random.choice(options)

    if choix_joueur == choix_ordi:
        print("Egalité")
    elif choix_joueur == "P" and choix_ordi == "C" \
        or choix_joueur == "C" and choix_ordi == "F" \
        or choix_joueur == "F" and choix_ordi == "P"    :
        score_hero += 1
        print("VOUS REMPORTEZ LA MANCHE :)")
    else:
        score_ordi += 1
        print("L'ORDINATEUR REMPORTE LA MANCHE (o-o)")

    print(f"{choix_joueur} X {choix_ordi}")
    print(f"Score : {score_hero} - {score_ordi}")

if score_hero == manches :
    print("VOUS AVEZ GAGNE LA PARTIE !")
else :
    print("L'ORDINATEUR GAGNE LA PARTIE.")