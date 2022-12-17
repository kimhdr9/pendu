import random

"""
pierre   'r' (rock)
papier   'p'
ciseaux  's' (scissors) 
"""
statisques ={
    'nul' : 0,
    'j1'  : 0,
    'j2'  : 0,
}

desciption = {
    'r':'la pierre',
    'p':'le papier',
    's':'les ciseaux'
}
possibilites=['r','p','s']

def is_win(player,opponent):
    """
    la pierre (r) bat les ciseaux (s)
    les ciseaux (s) bat le papier (p)
    le papier (p) bat la pierre
    """
    if (player == 'r' and opponent =='s') or (player == 's' and opponent =='p') or (player == 'p' and opponent =='r') :
        return True

def qui_gagne(joueur1,joueur2):
    """
    renvoie le résultat 
    """
    qui="le joueur2 gagne"
    if (joueur1 == joueur2) :
        qui=" égalité "
        statisques['nul']=statisques['nul']+1
    else :    
        if is_win(joueur1,joueur2) :
            qui=" joueur1 gagne"
            statisques['j1']=statisques['j1']+1
        else :
            statisques['j2']=statisques['j2']+1


    return qui


def tirage(nombre,affiche=True) :
    """
    nombre : nombre d'itération
    affiche : affiche sur le terminal le résultat d'un tirage valeur par défaut vrai,
    """


    for i in range(1,nombre):
        joueur1=random.choice(possibilites)
        joueur2=random.choice(possibilites)
        choix1=desciption[joueur1]
        choix2=desciption[joueur2]
        if affiche :
            print( f"le joueur1 a choisi {choix1} et le  joueur2 a choisi {choix2}")
            print(qui_gagne(joueur1,joueur2))        
        else :
            qui_gagne(joueur1,joueur2)
    
    print(statisques)

def test():
    statisques['j1'] = statisques['j1'] +8
    print(statisques['j1'])

if __name__ == '__main__':
    nombre = int(input('nombre de tirage : '))
    tirage(nombre=nombre,affiche=False)