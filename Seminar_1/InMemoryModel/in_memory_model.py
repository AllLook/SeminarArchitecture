from abc import ABC
from SeminarArchitecture.Seminar_1.ModelElements.model_elements import Scene, Flash, PoligonalModel, Camera


class IModelChangedObserver(ABC):
    def _apply_update_model(self):  # '_' Вначале названия метода или переменной делает его приватным
        pass


class IModelChanger(ABC):
    def NotifyChange(self, sender):  # нельзя задать переменную этого же класса при его создании
        pass


class ModelStore(IModelChanger):
    models: PoligonalModel
    scenes: Scene
    flashes: Flash
    cameras: Camera
    _change_observers: IModelChangedObserver

    def getscena(self, num: int):
        return Scene

    def notifychange(IModelChanger):
        pass
