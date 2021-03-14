from Models.Aircrafts.Components.Errors.JetError import JetError
from Models.Aircrafts.Components.Fuselage import Fuselage
from Models.Aircrafts.Components.Engine import Engine


class Jet:
    
    def __init__(self, model) -> None:
        self._model = model
        
        if not hasattr(self, '_engine') or self._engine is None:
            raise JetError(f'Jet model {self._model} must have engine configurations.')

        if not hasattr(self, '_fuselage') or self._fuselage is None:
            raise JetError(f'Jet model {self._model} must have fuselage configurations.')
    
    def get_model(self) -> str: return self._model
    
    def get_seats(self): return self._fuselage.get_seats()

    def start_engine(self) -> None: self._engine.start()

    def stop_engine(self) -> None: self._engine.stop()