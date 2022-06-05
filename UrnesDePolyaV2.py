import random
import matplotlib.pyplot as plt

class IllegalArgumentError(Exception):
    pass

def tracerUrnes(nbIt:int, nbSim:int, bPiochéAddBleu:int,bPiochéAddRouge:int,rPiochéAddBleu, rPiochéAddRouge, operation, nbBstart, nbRstart):
    if nbIt<1 or nbSim <1 or nbBstart<1 or nbRstart <1 :
        raise IllegalArgumentError("1 paramètre de simulation ou plus est negatif ou nul")
    if bPiochéAddBleu<0 or bPiochéAddRouge<0 or rPiochéAddBleu<0 or rPiochéAddRouge <0 :
        raise IllegalArgumentError("Impossible d'ajouter un nombre négatif de boules")
    if operation=="Multiplier"and (bPiochéAddBleu<=0 or rPiochéAddRouge <=0) :
        raise IllegalArgumentError("Multiplication par 0 impossible pour la boule de couleur piochée")
    plt.clf()
    fig, ax = plt.subplots(1, 1)
    for j in range(nbSim):
        nbBleu=int(nbBstart)
        nbRouge=int(nbRstart)
        tauxBleuList=list() 
        tauxBleuList.append(100*nbBleu/(nbBleu+nbRouge))
        for i in range(1,nbIt+1):
            num=random.randint(1,nbBleu+nbRouge)
            rdm=random.randint(1,2)
            if operation=="Additionner": 
                if(num<=nbBleu) :
                  nbBleu+=bPiochéAddBleu
                  nbRouge+=bPiochéAddRouge
                else :
                    nbRouge+=rPiochéAddRouge
                    nbBleu+=rPiochéAddBleu
            elif operation=="Multiplier":
                if(num<=nbBleu) :
                  nbBleu*=bPiochéAddBleu
                  nbRouge*=bPiochéAddRouge
                else :
                    nbRouge*=rPiochéAddRouge
                    nbBleu*=rPiochéAddBleu
            elif operation=="Aléatoire":
                if(rdm==1) :
                  nbBleu+=bPiochéAddBleu
                  nbRouge+=bPiochéAddRouge
                else :
                    nbRouge+=rPiochéAddRouge
                    nbBleu+=rPiochéAddBleu
            else :
                raise IllegalArgumentError("Operation lors du tirage impossible")
            tauxBleuList.append(100*nbBleu/(nbBleu+nbRouge))
        
        
        ax.plot(tauxBleuList,linewidth=0.5)
        
    plt.setp(ax, ylim=(0,100))
    plt.xlabel("Nombre d'itérations")
    plt.ylabel("% Bleues")
    fig.savefig("simul.png", format='png', dpi=100)
        

graph=tracerUrnes(400, 20, 1, 0, 8, 1, "Aléatoire", 1,1)
