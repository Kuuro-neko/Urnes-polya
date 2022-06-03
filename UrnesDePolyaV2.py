import random
import matplotlib.pyplot as plt

def tracerUrnes(nbIt, nbSim, bPiochéAddBleu,bPiochéAddRouge,rPiochéAddBleu, rPiochéAddRouge, operation) :
    for j in range(nbSim):
        nbBleu=int(1)
        nbRouge=int(1)
        tauxBleuList=list()
        tauxBleuList.append(100*nbBleu/(nbBleu+nbRouge))
        for i in range(1,nbIt+1):
            if
            num=random.randint(1,nbBleu+nbRouge)
            if(num<=nbBleu) :
              nbBleu+=1
              nbRouge+=1
            else :
                nbRouge+=0
                nbBleu+=1
            tauxBleuList.append(100*nbBleu/(nbBleu+nbRouge))
        
        plt.plot(tauxBleuList)
        tauxBleuesliste=list()