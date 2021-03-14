from Models.Aircrafts.Components.Engine import Engine
from Models.Aircrafts.Components.Fuselage import Fuselage
from Models.Aircrafts.Jet import Jet

class PrivateJet(Jet):
    
    def __init__(self, model) -> None:
        self._engine = Engine(model)
        self._fuselage = Fuselage(3,2)
        super().__init__(model)