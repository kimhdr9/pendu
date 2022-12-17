mot='exemple'
found =['E','L','N']
essai ='E'

def affiche(essai,mot) :
    inconnu='*'
    trouve=''
    for lettre in mot.upper() :

        if essai == lettre :
            trouve = trouve+essai
        else :
            trouve = trouve+inconnu

    return(trouve)

if __name__ == '__main__':
    mot='EXPLOSION'
    
    trouve = [letter if letter in found else '-' for letter in mot]

    print('lettres trouvées',' '.join(trouve))