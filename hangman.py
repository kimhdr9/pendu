import json
import random
filename='words.json'
use_letters=[]
def mot_a_deviner(filename):
    """
    lit le contenu de filename au format json
    """
    try :
        with open(file=filename) as f:
            data= json.load(f)
    except IOError :
        print(f'ouverture impossible de {filename}') 
    return data

# nombre de mots 
# print(len(data["data"]))
# accès
def affiche(x=10,filename=filename) :
    """
    affiche les x-1 mots pris de façon aléatoire dans le fichier filename
    """
    data = mot_a_deviner(filename=filename)
    for i in range(1,x) :
        mot=random.choice(data["data"])
        print(f'{i} -- {mot}')

def utilisation_set(filename=filename) :
    """
    set décompose le mot en lettres
    """
    data = mot_a_deviner(filename=filename)
    mot=random.choice(data["data"])
    lettres=set(mot)
    print(mot)
    for lettre in lettres :
        print(f'{lettre.upper()}')

def decompose_mot_en_lettre(filename=filename):
    """
    renvoie un mot pris de façon aléatoire depuis le fichier json
    """
    data = mot_a_deviner(filename=filename)
    mot=random.choice(data["data"])

    return mot
"""
test du programme
"""
if __name__ == '__main__':
    alphabet='azertyuiopqsdfghjklmwxcvbn'
    trouvees=[]
    liste_alpha = set(alphabet.upper())
    mot = decompose_mot_en_lettre()
    lettres=set(mot.upper())
    taille = len(lettres)
    taille_2=len(mot)

    print(liste_alpha)
    print(f"le mot '{mot}' contient {taille_2} lettres mais seulement {taille} différentes.")

    iteration=0
    i=0
    while len(trouvees) < taille :
        i=i+1
        entree = input('entre une lettre :')
        alpha=entree.upper()
        if alpha in lettres :
            trouvees.append(alpha)
            iteration = i
            print('une nouvelle lettre touvée')
            print(trouvees)
            

    print(f"le mot '{mot.upper()}' a été trouvé en {iteration} iterations")
        