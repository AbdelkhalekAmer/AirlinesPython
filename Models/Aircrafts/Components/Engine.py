from Models.Aircrafts.Components.Errors.EngineError import EngineError

class Engine:
    
    def __init__(self,jet_model):
        self._jet_model = jet_model
        self._isStarted = False

    def start(self):
        if not self._isStarted: 
            self._isStarted = True
            print(f"{self._jet_model}'s engine is started successfully.")
        else: raise EngineError("Engine is already started.")
    
    def stop(self):
        if self._isStarted:
            self._isStarted = False
            print(f"{self._jet_model}'s engine is stopped successfully.")
        else: raise EngineError("Engine is already stopped.")