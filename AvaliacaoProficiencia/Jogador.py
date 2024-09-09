class Jogador:

    def __init__(self, vida, energia) :
        self._vida=vida
        self._energia=energia

    def getVida(self):
        return self._vida
    
    def setVida(self,vida):
        self._vida=vida

    def getEnergia(self):
        return self._energia    
    
    def setEnergia(self,energia):
        self._energia=energia

        