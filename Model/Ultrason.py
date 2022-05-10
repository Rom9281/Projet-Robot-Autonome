from Model.PeripheriqueCarte import PeripheriqueCarte

class Ultrason(PeripheriqueCarte):
    def __init__(self,carte):
        super().__init__(carte)
    
    def recupererDistance(self):
        pass