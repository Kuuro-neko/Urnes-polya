import random
import matplotlib.pyplot as plt

class IllegalArgumentError(Exception):
    pass

def tracerUrnes(nbIt, nbSim, bPiochéAddBleu,bPiochéAddRouge,rPiochéAddBleu, rPiochéAddRouge, operation, nbBstart, nbRstart) :
    
   
    if operation=="add" :
        for j in range(nbSim):
            nbBleu=int(nbBstart)
            nbRouge=int(nbRstart)
            tauxBleuList=list() 
            tauxBleuList.append(100*nbBleu/(nbBleu+nbRouge))
            for i in range(1,nbIt+1):
                num=random.randint(1,nbBleu+nbRouge)
                if(num<=nbBleu) :
                  nbBleu+=bPiochéAddBleu
                  nbRouge+=bPiochéAddRouge
                else :
                    nbRouge+=rPiochéAddRouge
                    nbBleu+=rPiochéAddBleu
                tauxBleuList.append(100*nbBleu/(nbBleu+nbRouge))
            plt.plot(tauxBleuList)
               
    elif operation=="mult":
        for j in range(nbSim):
            nbBleu=int(nbBstart)
            nbRouge=int(nbRstart)
            tauxBleuList=list() 
            tauxBleuList.append(100*nbBleu/(nbBleu+nbRouge))
            for i in range(1,nbIt+1):
                num=random.randint(1,nbBleu+nbRouge)
                if(num<=nbBleu) :
                  nbBleu*=bPiochéAddBleu
                  nbRouge*=bPiochéAddRouge
                else :
                    nbRouge+=rPiochéAddRouge
                    nbBleu+=rPiochéAddBleu
                tauxBleuList.append(100*nbBleu/(nbBleu+nbRouge))
            plt.plot(tauxBleuList)
    else :
        raise IllegalArgumentError("Operation impossible")
    
        
        
        
tracerUrnes(400, 1000, 1, 0, 0, 1, "add", 27,1)