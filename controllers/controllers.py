from gui.views import Form, View
from abc import ABC, abstractmethod
from cloudflare.cflare import CFlare

class Controller(ABC):
    
    def __init__(self, master=None):
        super().__init__(master)
        self.cflare = CFlare()


    @abstractmethod
    def bind(view: View):
        raise NotImplementedError

class ZoneController(Controller):

    def __init__(self) -> None:
        self.view = None
        self.zones = self.cflare.show_zones()

    def bind(self, view: Form):
        self.view = view
        self.view.create_view(self.zones)
