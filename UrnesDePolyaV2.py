import random
import matplotlib.pyplot as plt

class IllegalArgumentError(Exception):
    pass

def tracerUrnes(nbIt, nbSim, bPiochéAddBleu,bPiochéAddRouge,rPiochéAddBleu, rPiochéAddRouge, operation, nbBstart, nbRstart) :
    
    for j in range(nbSim):
        nbBleu=int(nbBstart)
        nbRouge=int(nbRstart)
        tauxBleuList=list() 
        tauxBleuList.append(100*nbBleu/(nbBleu+nbRouge))
        for i in range(1,nbIt+1):
            num=random.randint(1,nbBleu+nbRouge)
            if operation=="add": 
                if(num<=nbBleu) :
                  nbBleu+=bPiochéAddBleu
                  nbRouge+=bPiochéAddRouge
                else :
                    nbRouge+=rPiochéAddRouge
                    nbBleu+=rPiochéAddBleu
            elif operation=="mult":
                if(num<=nbBleu) :
                  nbBleu*=bPiochéAddBleu
                  nbRouge*=bPiochéAddRouge
                else :
                    nbRouge+=rPiochéAddRouge
                    nbBleu+=rPiochéAddBleu
            else :
                raise IllegalArgumentError("Operation impossible")
            tauxBleuList.append(100*nbBleu/(nbBleu+nbRouge))
        plt.plot(tauxBleuList)
        plt.xlabel("Nombre d'itérations")
        plt.ylabel("% Bleues")
        plt.savefig("simul.png", format='png')
    
           
        

graph=tracerUrnes(400, 90, 1, 0, 0, 1, "add", 1,1)