# CrÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â©ÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â© par drabotsous, le 14/10/2024 en Python 3.2

import random
import time

class Bird :
    "DÃ©finition d'un Bird"

    def __init__(self,nom) :
        self.tour=True
        if nom=='red' :#s'il choisit red
            #on initialise les stats du perso
            self.nom='Red'
            self.PV = 100
            self.PVmax = 100
            self.backlash=0
            self.XP=0
            self.attaque=85
            self.defense=20
            self.niveau=0
            self.vitesse=75
            self.stamina=40
            self.staminamax=40
            self.att_spe=['Rage',150]
        elif nom=='chuck' :#de mÃªme pour chuck
            self.nom='Chuck'
            self.backlash=0
            self.PV = 50
            self.PVmax = 50
            self.XP=0
            self.attaque=70
            self.defense=15
            self.niveau=0
            self.vitesse=100
            self.stamina=50
            self.staminamax=50
            self.att_spe=['Hyperactive',0]
        elif nom=='bomb' :#et pour bomb
            self.nom='Bomb'
            self.PV = 120
            self.PVmax = 120
            self.XP=0
            self.attaque=100
            self.defense=25
            self.niveau=0
            self.vitesse=40
            self.stamina=30
            self.staminamax=30
            self.att_spe=['Kamikaze',50]

    def attaquer(self,ennemi,indice=0) :
        """
        On crÃ©e une mÃ©thode qui prend un ennemi en paramÃ¨tre et permet au Bird d'attaquer l'ennemi avec l'attaque de son choix.
        """
        global ennemi_tour
        ennemi_tour=True
        attaque_valide=False#on initialise une variable qui permettra de vÃ©rfier que le Bird peut attaquer
        while not attaque_valide :
            if self.nom=='Bomb' :
                print(self.nom+': Stamina:',self.stamina,', PV:', self.PV,'/',self.PVmax,'// PV '+ennemi[indice].nom+':',ennemi[indice].PV)#on rappelle les PV de chacun
            else :
                print(self.nom+': Stamina:',self.stamina,', PV:', self.PV,'/',self.PVmax,'// PV '+ennemi.nom+':',ennemi.PV)#on rappelle les PV de chacun
            attaque=input('Quelle attaque souhaitez-vous lancer ? 1: Normal, 2: '+self.att_spe[0])#on demande au joueur quelle attaque il souhaite lancer
            if attaque=='1' :#si le joueur choisit de lancer une attaque normale
                if self.nom=='Bomb' :
                    if self.attaque<ennemi[indice].defense:#si la dÃ©fense de l'ennemi est supÃ©rieure Ã  l'attaque du joueur
                        ennemi[indice].PV-=0#le joueur ne lui fait aucun dÃ©gÃ¢t
                        print(self.nom,'attaque',ennemi[indice].nom,': Vous ne faites aucun dÃ©gÃ¢ts.')#On le prÃ©cise
                    else :
                        ennemi[indice].PV -= self.attaque-ennemi[indice].defense#on inflige des dÃ©gÃ¢ts Ã  l'ennemi qui correspondent Ã  la diffÃ©rence entre sa dÃ©fense et l'attaque du joueur
                        if ennemi[indice].PV<0 :#si les PV de l'ennemi passe en dessous de 0
                            ennemi[indice].PV=0#on les passe Ã  0
                        print(self.nom,'attaque',ennemi[indice].nom,': Vous faites',self.attaque-ennemi[indice].defense,'dÃ©gÃ¢ts.')#On prÃ©cise les dÃ©gÃ¢ts infligÃ©s
                else :
                    if self.attaque<ennemi.defense:#si la dÃ©fense de l'ennemi est supÃ©rieure Ã  l'attaque du joueur
                        ennemi.PV-=0#le joueur ne lui fait aucun dÃ©gÃ¢t
                        print(self.nom,'attaque',ennemi.nom,': Vous ne faites aucun dÃ©gÃ¢ts.')#On le prÃ©cise
                    else :
                        ennemi.PV -= self.attaque-ennemi.defense#on inflige des dÃ©gÃ¢ts Ã  l'ennemi qui correspondent Ã  la diffÃ©rence entre sa dÃ©fense et l'attaque du joueur
                        if ennemi.PV<0 :#si les PV de l'ennemi passe en dessous de 0
                            ennemi.PV=0#on les passe Ã  0
                        print(self.nom,'attaque',ennemi.nom,': Vous faites',self.attaque-ennemi.defense,'dÃ©gÃ¢ts.')#On prÃ©cise les dÃ©gÃ¢ts infligÃ©s
                attaque_valide=True#on valide l'attaque

            elif attaque=='2' :#s'il choisit son attaque spÃ©ciale
                if self.stamina>=20:#on vÃ©rifie qu'il a assez de stamina
                    if self.nom=='Chuck' :
                        print('Vous utilisez Hyperactive : +20 DEF')
                        self.defense+=20
                        ennemi_tour=False
                        self.backlash=4
                    elif self.nom=='Red':
                        print('Vous utilisez Rage')
                        if self.att_spe[1]< ennemi.defense:#si la dÃ©fense de l'ennemi est supÃ©rieure Ã  l'attaque du bird
                            ennemi.PV-=0#le joueur ne fait aucun dÃ©gÃ¢t
                            print(self.nom,'attaque',ennemi.nom,': Vous ne faites aucun dÃ©gÃ¢t.')
                        else :
                            ennemi.PV -= self.att_spe[1]-ennemi.defense#sinon on inflige des dÃ©gÃ¢ts Ã  l'ennemi
                            if ennemi.PV<0 :#si ses PV sont infÃ©rieurs Ã  0
                                ennemi.PV=0#on les passe Ã  0
                            print(self.nom,'attaque',ennemi.nom,': Vous faites',self.att_spe[1]-ennemi.defense,'dÃ©gÃ¢ts.')
                        print('Red est Ã©puisÃ©')
                        self.tour=False
                        self.backlash=1
                        attaque_valide=True#on valide l'attaque
                    else :
                        print('Vous utilisez Kamikaze.')
                        for enn in ennemi :
                            if self.att_spe[1]< enn.defense:#si la dÃ©fense de l'ennemi est supÃ©rieure Ã  l'attaque du bird
                                ennPV-=0#le joueur ne fait aucun dÃ©gÃ¢t
                                print(enn.nom,'ne se prend aucun dÃ©gÃ¢t')
                            else :
                                enn.PV -= self.att_spe[1]-enn.defense#sinon on inflige des dÃ©gÃ¢ts Ã  l'ennemi
                                if enn.PV<0 :#si ses PV sont infÃ©rieurs Ã  0
                                    enn.PV=0#on les passe Ã  0
                                print(enn.nom,'se prend',self.att_spe[1]-enn.defense,'dÃ©gÃ¢ts.')
                        print('Vous prenez 50 dÃ©gÃ¢ts de contrecoup')
                        self.PV-=50
                        attaque_valide=True#on valide l'attaque
                    self.stamina-=20#on diminue la stamina du joueur
                else :
                    print('Pas assez de stamina !')#si le joueur n'a pas assez de stamina pour lancer son attaque spÃ©ciale, on ne valide pas l'attaque

            else :
                print('Valeur invalide !')#de mÃªme s'il entre autre chose que '1' ou '2'

    def GainXP(self,nbXP) :
        """
        On crÃ©e une mÃ©thode prenant en paramÃ¨tre un nombre d'XP (int) qui sera ajoutÃ© Ã  ceux du joueur.
        """
        self.XP+=nbXP#on augmente les XP du bird
        if self.XP>100 :#si ses XP dÃ©passent 100
            self.XP=0#on repasse ses XP Ã  0
            self.niveau+=1#on augmente son niveau
            #on augmente toutes ses stats de 5
            self.PV+=5
            self.PVmax+=5
            self.attaque+=5
            self.defense+=5
            self.vitesse+=5
            self.stamina+=5
            self.staminamax+=5
            self.att_spe[1]+=5



class Picoo :
    "DÃ©finition d'un cochon"

    def __init__(self,picoo) :
        """
        on prend en paramÃ¨tres une liste de "types" de cochons
        """
        self.nom=picoo
        if self.nom=='Minion' :#si Ã§a tombe sur Minion
            #on dÃ©finit ses stats
            self.PV =100
            self.attaque=30
            self.defense=10
            self.vitesse=60
        elif self.nom=='Corporal' :#pareil pour corporal
            self.PV=100
            self.attaque=35
            self.defense=15
            self.vitesse=65
        elif self.nom=='Fat' :#pareil pour fat
            self.PV=150
            self.attaque=40
            self.defense=5
            self.vitesse=45
        elif self.nom=='King Picoo' :#et pour King Picoo
            self.PV=500
            self.PVmax=500
            self.defense=0
            self.vitesse=50
            self.attaque=40


    def attaquer(self,ennemi) :
        """
        on dÃ©finit une mÃ©thode qui permet au cochon/picoo d'attaquer le bird.
        """
        if self.attaque<ennemi.defense:#si la dÃ©fense de l'ennemi du cochon (cÃ d du bird) est supÃ©rieure
            ennemi.PV-=0#on inflige aucun dÃ©gÃ¢t
            print(self.nom,'attaque',ennemi.nom,':' ,self.nom,' ne vous fait aucun dÃ©gÃ¢ts.')
        else :
            ennemi.PV -= self.attaque-ennemi.defense#sinon on inflige des dÃ©gÃ¢ts
            if ennemi.PV<0 :#si les PV du bird sont infÃ©rieurs Ã  0
                ennemi.PV=0#on les passe Ã  0
                print(ennemi.nom+' est K.O.')
            print(self.nom,'attaque',ennemi.nom,':',self.nom, 'vous fait',self.attaque-ennemi.defense,'dÃ©gÃ¢ts.')

def combat(perso,ennemi) :
    """
    Fonction combat qui permet de lancer un combat entre deux adversaires donnÃ©s en paramÃ¨tres (perso et ennemi). Elle retourne True si le perso est gagnant, False sinon
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
        else :#si Ã  l'inverse c'est l'ennemi qui est plus rapide
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

def maximum(char) :
    """
    On dÃ©finit une fonction qui Ã  partir d'une liste char retourne l'indice du 'personnage' qui a la plus grande vitesse cette liste.
    """
    max_indice=0#on initialise l'indice
    for i in range(len(char)) :#pour chaque indice de la liste
        if char[i].vitesse > char[max_indice].vitesse :#si la vitesse du personnage Ã  l'indice i est supÃ©rieure Ã  celle du personnage au rang max_indice
            max_indice=i#on change l'indice max_indice
    return max_indice#on retourne l'indice du maximum

def verif_int(input_j) :
    """
    Fonction qui permet de vÃ©rifier qu'un input d'un joueur input_j peut Ãªtre converti en int
    """
    try:
        int(input_j)
        return True
    except :
        return False

def sort_speed(char) :
    """
    On dÃ©finit une fonction qui permet de trier une liste char par ordre dÃ©croissant (la plus grande valeur Ã  l'indice 0) des vitesses des personnages de la liste
    """
    new=[]#on crÃ©e une liste vide
    while len(char)!=0 :#tant qu'il y a encore des Ã©lÃ©ments dans la liste char
        new.append(char.pop(maximum(char)))#on ajoute le personnage qui a la plus grande vitesse Ã  la liste new
    return new#on retourne la liste avec les personnages triÃ©s

def combat_multiple(perso,enemies) :
    """
    Fonction qui permet de dÃ©clencher un combat avec plusieurs ennemis en tour par tour
    """
    global ennemi_tour
    ennemi_tour=True
    perso.tour=True
    while any([p.PV>0 for p in enemies]) and perso.PV>0:#tant l'un au moins des picoos est encore en vie
        opponents=sort_speed(enemies+[perso])#liste de tous les oposants du combat (cÃ d bird+picoos) triÃ©s par vitesse
        if perso.tour==True:
            print('Choisis un ennemi Ã Â  attaquer:')#on demande au joeuuru de choisir un ennemi Ã  attaquer
            for i in range(len(enemies)) :
                print(str(i+1)+':'+enemies[i].nom+'- PV:',enemies[i].PV)
            verif=False
            while not verif :
                i_ennemi=input()
                if verif_int(i_ennemi):
                    i_ennemi=int(i_ennemi)
                    verif=i_ennemi-1 in range(len(enemies))
                else  :
                    print('EntrÃ©e invalide')
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


def jeu() :
    """
    On dÃ©finit la fonction principale du jeu.
    """
    nom=''
    while nom.lower() not in ['chuck','red','bomb'] :
        nom=input('Quel personnage veux-tu ? Red, Chuck, Bomb').lower()#on demande au joueur de choisir un oiseau
        if nom.lower() not in ['chuck','red','bomb'] :
            print('Valeur invalide !')
    perso=Bird(nom.lower())#on crÃ©e un bird
    picoo_list=['Minion']#on crÃ©e une liste de types possibles de picoo/cochon
    stage=1#on initialise le numÃ©ro du stage
    stop=False
    while not stop :
        while stage<9 :#jusqu'au stage 9
            picoo=Picoo(random.choice(picoo_list))#on choisit un type de cochon au hasard dans la liste)#on crÃ©e un cochon
            if stage==2 :#si on est au stage 2
                picoo_list.append('Corporal')#on ajoute corporal Ã  la liste de cochons possibles
            if stage==4 :#et si on est au stage 4
                picoo_list.append('Fat')#on ajoute Fat Ã  la liste des cochons
            print('Stage',stage,":",perso.nom,'affronte',picoo.nom)#on annonce le stage et on prÃ©cise les opposants
            if combat(perso,picoo) :#si le joueur remporte le combat
                print('Stamina :',perso.stamina,'- PV',perso.nom,':',perso.PV,'/',perso.PVmax,'// PV',picoo.nom,':',picoo.PV)#on annonce le rÃ©sultat
                print(picoo.nom+' est K.O.')#on prÃ©cise que le picoo est K.O.
                print('Bravo! Vous passez au stage suivant.')
                perso.GainXP(30)#on ajoute de l'XP au joueur
                print('+30 XP')
                print('XP :', perso.XP,', Niveau :', perso.niveau)
                print('')
                if perso.PV+25<=perso.PVmax :#si les PV du joueur le permettent
                    perso.PV+=25#on en rajoute aux joueurs
                perso.stamina+=10#on augmente sa stamina
                if perso.stamina>=perso.staminamax :#si la stamina obtenue est supÃ©rieure Ã  la stamina max
                    perso.stamina=perso.staminamax#on lui donne la valeur de la stamina max
                stage+=1#on augmente le stage
            else :#sil perd
                print('Game Over')
                if input('Reprendre le stage ? 1:Oui 2:Non') == '1' :#on lui demande s'il souhaite reprendre
                    perso.PV=perso.PVmax#on remet ses stats au maximum
                    perso.stamina=perso.staminamax
                else :
                    print('ÃŠtes-vous sÃ»r de vouloir quitter ? Votre progression sera perdue.')
                    print('1: Oui')
                    print('2: Non')
                    verif = False
                    while not verif :#tant que la rÃ©ponse n'est pas valide
                        rep=input()#on redemande au joueur
                        if rep in ['1','2'] :#sinon  on confirme qu'il veuille bien quitter
                            if rep=='1' :
                                stop=True#on arrÃªte le jeu
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
            Roi=Picoo('King Picoo')#on crÃ©e le boss
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
                            if 2*Roi.PVmax//3<Roi.PV<Roi.PVmax :#si le roi est dans son troisiÃ¨me tiers de PV
                                print('King Picoo envoie 3 Minions')
                                combat_multiple(perso,[Picoo('Minion') for i in range(3)])#il envoie trois Minions au combat
                            if Roi.PVmax//3<Roi.PV<2*Roi.PVmax//3 :#s'il est dans son deuxiÃ¨me tiers
                                print('King Picoo invoque 3 Corporal')
                                combat_multiple(perso,[Picoo('Corporal') for i in range(3)])#il envoie trois corporal
                            else :#s'il est dans son premier tiers
                                print('King Picoo est trÃ¨s en colÃ¨re. \nIl invoque trois Picoos.')
                                combat_multiple(perso,[Picoo(random.choice(['Fat','Corporal'])) for i in range(3)])#il envoie de maniÃ¨re alÃ©atoire trois picoos parmi Corporal et Fat
                        else :#le reste du temps
                            Roi.attaquer(perso)#le roi attaque le joueur
                else :#si le roi est plus rapide que le joueur
                    if ennemi_tour==True :
                        Roi.attaquer(perso)#il attaque le joueur en premier
                    if perso.PV>0 :
                        if perso.tour==True:
                            perso.attaquer(Roi)#puis s'il est en vie, le joueur attaque
            if Roi.PV <= 0 :#si le roi meurt
                print('Bravo! Vous avez vaincu King Picoo')#on fÃ©licite le joueur
                print("Vous avez rÃ©cupÃ©rÃ© l'oeuf !")
                stage+=1#on arrÃªte le jeu
            else :#si le joueur meurt
                print('Game Over')
                if input('Reprendre le stage ? 1:Oui 2:Non') == '1' :#on lui demande s'il souhaite reprendre
                    perso.PV=perso.PVmax#on remet ses stats au maximum
                    perso.stamina=perso.staminamax
                else :
                    print('ÃŠtes-vous sÃ»r de vouloir quitter ? Votre progression sera perdue.')
                    print('1: Oui')
                    print('2: Non')
                    verif = False
                    while not verif :#tant que la rÃ©ponse n'est pas valide
                        rep=input()#on redemande au joueur
                        if rep in ['1','2'] :#sinon  on confirme qu'il veuille bien quitter
                            if rep=='1' :
                                stop=True#on arrÃªte le jeu
                            else :#sinon on remet ses stats au maximum
                                perso.PV=perso.PVmax
                                perso.stamina=perso.staminamax
                                verif=True
                        else :
                            print('Format invalide !')

        stop=True#on arrÃªte le jeu






