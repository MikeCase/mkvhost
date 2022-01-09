from gui.views import View
from abc import ABC, abstractmethod

class Controller(ABC):
    
    @abstractmethod
    def bind(view: View):
        raise NotImplementedError





