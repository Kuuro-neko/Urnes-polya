import random
import matplotlib.pyplot as plt

class IllegalArgumentError(Exception):
    pass

def tracerUrnes(nbIt, nbSim, bPiochéAddBleu,bPiochéAddRouge,rPiochéAddBleu, rPiochéAddRouge, operation, nbBstart, nbRstart) :
    plt.clf()
    for j in range(nbSim):
        nbBleu=int(nbBstart)
        nbRouge=int(nbRstart)
        tauxBleuList=list() 
        tauxBleuList.append(100*nbBleu/(nbBleu+nbRouge))
        for i in range(1,nbIt+1):
            num=random.randint(1,nbBleu+nbRouge)
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
            else :
                raise IllegalArgumentError("Operation impossible")
            tauxBleuList.append(100*nbBleu/(nbBleu+nbRouge))
        
        
        graph=plt.plot(tauxBleuList,linewidth=0.5)
        
    plt.xlabel("Nombre d'itérations")
    plt.ylabel("% Bleues")
    plt.savefig("simul.png", format='png', dpi=100)
        

graph=tracerUrnes(400, 20, 1, 0, 0, 1, "Additionner", 1,1)