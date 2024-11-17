import random
import time
from bird import Bird
from picoo import Picoo
from combat_mecanic import combat, combat_multiple

def jeu() :
    """
    On définit la fonction principale du jeu.
    """
    nom=''
    while nom.lower() not in ['chuck','red','bomb'] :
        nom=input('Quel personnage veux-tu ? Red, Chuck, Bomb').lower()#on demande au joueur de choisir un oiseau
        if nom.lower() not in ['chuck','red','bomb'] :
            print('Valeur invalide !')
    perso=Bird(nom.lower())#on crée un bird
    picoo_list=['Minion']#on crée une liste de types possibles de picoo/cochon
    stage=1#on initialise le numéro du stage
    stop=False
    while not stop :
        while stage<9 :#jusqu'au stage 9
            picoo=Picoo(random.choice(picoo_list))#on choisit un type de cochon au hasard dans la liste)#on crée un cochon
            if stage==2 :#si on est au stage 2
                picoo_list.append('Corporal')#on ajoute corporal à  la liste de cochons possibles
            if stage==4 :#et si on est au stage 4
                picoo_list.append('Fat')#on ajoute Fat à  la liste des cochons
            print('Stage',stage,":",perso.nom,'affronte',picoo.nom)#on annonce le stage et on précise les opposants
            if combat(perso,picoo) :#si le joueur remporte le combat
                print('Stamina :',perso.stamina,'- PV',perso.nom,':',perso.PV,'/',perso.PVmax,'// PV',picoo.nom,':',picoo.PV)#on annonce le résultat
                print(picoo.nom+' est K.O.')#on précise que le picoo est K.O.
                print('Bravo! Vous passez au stage suivant.')
                perso.GainXP(30)#on ajoute de l'XP au joueur
                print('+30 XP')
                print('XP :', perso.XP,', Niveau :', perso.niveau)
                print('')
                if perso.PV+25<=perso.PVmax :#si les PV du joueur le permettent
                    perso.PV+=25#on en rajoute aux joueurs
                perso.stamina+=10#on augmente sa stamina
                if perso.stamina>=perso.staminamax :#si la stamina obtenue est supérieure à  la stamina max
                    perso.stamina=perso.staminamax#on lui donne la valeur de la stamina max
                stage+=1#on augmente le stage
            else :#sil perd
                print('Game Over')
                if input('Reprendre le stage ? 1:Oui 2:Non') == '1' :#on lui demande s'il souhaite reprendre
                    perso.PV=perso.PVmax#on remet ses stats au maximum
                    perso.stamina=perso.staminamax
                else :
                    print('àŠtes-vous sà»r de vouloir quitter ? Votre progression sera perdue.')
                    print('1: Oui')
                    print('2: Non')
                    verif = False
                    while not verif :#tant que la réponse n'est pas valide
                        rep=input()#on redemande au joueur
                        if rep in ['1','2'] :#sinon  on confirme qu'il veuille bien quitter
                            if rep=='1' :
                                stop=True#on arrête le jeu
                            else :#sinon on remet ses stats au maximum
                                perso.PV=perso.PVmax
                                perso.stamina=perso.staminamax
                                verif=True
                        else :
                            print('Format invalide !')
        while stage==9 :#au stage 9 on change de mode de jeu
            enemies=[Picoo(random.choice(picoo_list)) for i in range (3)]#liste des ennemis
            print('Stage',stage,":",perso.nom,'affronte',enemies[0].nom+', '+enemies[1].nom+' et '+enemies[2].nom)
            if combat_multiple(perso,enemies) :#si le joueur est vainqueur
                print('Bravo! Vous passez au stage suivant.')#on augmente ses stats
                perso.GainXP(60)
                print('+60 XP')
                print('XP :', perso.XP,', Niveau :', perso.niveau)
                print('')
                perso.stamina=perso.staminamax
                stage+=1
            else :
                print('Game Over')
                print('')
                perso.PV=perso.PVmax#on remet ses stats au maximum
                perso.stamina=perso.staminamax
        while stage==10 :#tant qu'il est au stage 10
            perso.PV=perso.PVmax
            perso.stamina=perso.staminamax
            perso.tour=True
            print('')
            print('Vous entrez finalement dans la demeure de King Picoo')
            print('Il vous attendais...')
            print('Vous engagez le combat sans plus attendre.')
            print('')
            Roi=Picoo('King Picoo')#on crée le boss
            tour=0
            ennemi_tour=True
            while Roi.PV>0 and perso.PV>0 :#tant que les deux ont encore des PV
                tour+=1
                print(perso.nom+': Stamina:',perso.stamina,', PV:', perso.PV,'/',perso.PVmax,'// PV '+Roi.nom+':',Roi.PV,'/',Roi.PVmax)#on rappelle les PV de chacun
                if perso.vitesse>Roi.vitesse :#si le personnage est plus rapide que le King Picoo
                    if perso.tour==True :
                        perso.attaquer(Roi)#il attaque en premier
                    if Roi.PV>0 and ennemi_tour==True:#si le roi a encore des PV
                        if tour%3==0 :#tous les trois tours
                            if 2*Roi.PVmax//3<Roi.PV<Roi.PVmax :#si le roi est dans son troisième tiers de PV
                                print('King Picoo envoie 3 Minions')
                                combat_multiple(perso,[Picoo('Minion') for i in range(3)])#il envoie trois Minions au combat
                            if Roi.PVmax//3<Roi.PV<2*Roi.PVmax//3 :#s'il est dans son deuxième tiers
                                print('King Picoo invoque 3 Corporal')
                                combat_multiple(perso,[Picoo('Corporal') for i in range(3)])#il envoie trois corporal
                            else :#s'il est dans son premier tiers
                                print('King Picoo est très en colère. \nIl invoque trois Picoos.')
                                combat_multiple(perso,[Picoo(random.choice(['Fat','Corporal'])) for i in range(3)])#il envoie de manière aléatoire trois picoos parmi Corporal et Fat
                        else :#le reste du temps
                            Roi.attaquer(perso)#le roi attaque le joueur
                else :#si le roi est plus rapide que le joueur
                    if ennemi_tour==True :
                        Roi.attaquer(perso)#il attaque le joueur en premier
                    if perso.PV>0 :
                        if perso.tour==True:
                            perso.attaquer(Roi)#puis s'il est en vie, le joueur attaque
            if Roi.PV <= 0 :#si le roi meurt
                print('Bravo! Vous avez vaincu King Picoo')#on félicite le joueur
                print("Vous avez récupéré l'oeuf !")
                stage+=1#on arrête le jeu
            else :#si le joueur meurt
                print('Game Over')
                if input('Reprendre le stage ? 1:Oui 2:Non') == '1' :#on lui demande s'il souhaite reprendre
                    perso.PV=perso.PVmax#on remet ses stats au maximum
                    perso.stamina=perso.staminamax
                else :
                    print('àŠtes-vous sà»r de vouloir quitter ? Votre progression sera perdue.')
                    print('1: Oui')
                    print('2: Non')
                    verif = False
                    while not verif :#tant que la réponse n'est pas valide
                        rep=input()#on redemande au joueur
                        if rep in ['1','2'] :#sinon  on confirme qu'il veuille bien quitter
                            if rep=='1' :
                                stop=True#on arrête le jeu
                            else :#sinon on remet ses stats au maximum
                                perso.PV=perso.PVmax
                                perso.stamina=perso.staminamax
                                verif=True
                        else :
                            print('Format invalide !')

        stop=True#on arrête le jeu
=======

from .bird import Bird
from .picoo import Picoo
from .utils import sort_speed, verif_int

def combat(perso,ennemi) :
    """
    Fonction combat qui permet de lancer un combat entre deux adversaires donnés en paramètres (perso et ennemi). Elle retourne True si le perso est gagnant, False sinon
    """
    global ennemi_tour
    ennemi_tour=True
    perso.tour==True
    while perso.PV>0 and ennemi.PV>0 :#tant que les deux ont encore des PV le combat se poursuit
        if perso.vitesse>ennemi.vitesse :#si le perso est plus rapide que l'ennemi
            if perso.tour==True :
                if perso.nom=='Bomb' :
                    perso.attaquer([ennemi])#le perso attaque en premier
                else :
                    perso.attaquer(ennemi)
            if ennemi.PV > 0 and ennemi_tour==True:#et si l'ennemi a encore des PV
                ennemi.attaquer(perso)#il attaque
            else :
                ennemi_tour=True
        else :#si à  l'inverse c'est l'ennemi qui est plus rapide
            if ennemi_tour==True :
                ennemi.attaquer(perso)#il attaque le perso
            if perso.PV>0 and perso.tour==True:#qui s'il a encore des PV
                if perso.nom=='Bomb' :
                    perso.attaquer([ennemi])#attaque l'ennemi
                else :
                    perso.attaquer(ennemi)
        if perso.nom=='Chuck' :
            if perso.backlash>=1 :
                perso.backlash-=1
                perso.defense-=5
        if perso.nom=='Red' :
            if perso.backlash>0 :
                perso.backlash-=1
                print('Red se sent mieux.')
            elif perso.backlash==0 :
                perso.tour=True
    return perso.PV>0#si le joueur a encore des PV on retourne True, False sinon

def combat_multiple(perso,enemies) :
    """
    Fonction qui permet de déclencher un combat avec plusieurs ennemis en tour par tour
    """
    global ennemi_tour
    ennemi_tour=True
    perso.tour=True
    while any([p.PV>0 for p in enemies]) and perso.PV>0:#tant l'un au moins des picoos est encore en vie
        opponents=sort_speed(enemies+[perso])#liste de tous les oposants du combat (cà d bird+picoos) triés par vitesse
        if perso.tour==True:
            print('Choisis un ennemi à   attaquer:')#on demande au joeuuru de choisir un ennemi à  attaquer
            for i in range(len(enemies)) :
                print(str(i+1)+':'+enemies[i].nom+'- PV:',enemies[i].PV)
            verif=False
            while not verif :
                i_ennemi=input()
                if verif_int(i_ennemi):
                    i_ennemi=int(i_ennemi)
                    verif=i_ennemi-1 in range(len(enemies))
                else  :
                    print('Entrée invalide')
            ennemi=enemies[i_ennemi-1]#ennemi que le joueur a choisi d'attaquer
        for opp in opponents :#pour chaque opposants (bird compris)
            if type(opp)==Bird and opp.PV>0 and opp.tour==True:#si l'opposant est le bird
                print(perso.nom+' attaque '+ennemi.nom+':')#on le fait attaquer l'ennemi qu'il a choisi
                if perso.nom=='Bomb' :
                    opp.attaquer(enemies,i_ennemi)
                elif perso.nom in ['Chuck','Red'] :
                    if perso.tour==True:
                        opp.attaquer(ennemi)
                if ennemi.PV<=0 :
                    print(ennemi.nom+' est K.O.')
                    print('')
                    enemies.pop(i_ennemi-1)#si le joueur bat l'ennemi, on le retire de la liste des ennemis

            elif type(opp)==Picoo and opp.PV>0 and ennemi_tour==True:#si l'opposant est un Picoo
                opp.attaquer(perso)#il attaque le joueur
            elif ennemi_tour==False :
                ennemi_tour=True
        print('')
        for pic in enemies :
            print('PV '+pic.nom+':',pic.PV)#on affiche les PV de chaque ennemi
        print('PV '+perso.nom+': ',perso.PV)
        print('')
        if perso.nom=='Chuck' :
            if perso.backlash>=1 :
                print('- 5 DEF')
                perso.backlash-=1
                perso.defense-=5
        elif perso.nom=='Red' :
            if perso.backlash>0 :
                perso.backlash-=1
                print('Red se sent mieux')
            elif perso.backlash==0 :
                perso.tour=True
    return perso.PV>0
>>>>>>> 1df242b49c06524e8cf5cc7f8001b8686c33d605
