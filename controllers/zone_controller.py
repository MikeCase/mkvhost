from controllers.controllers import Controller
from gui.tree_view import TreeViewForm
from models.models import CloudFlare

class ZoneController(Controller):

    def __init__(self) -> None:
        self.view = None
        self.model = None

    def bind(self, view: TreeViewForm, model: CloudFlare):
        view.model = model
        self.view = view
        self.model = model
        self.zones = self.model.get_zones()
        zone_data = []
        headings = ['id', 'name', 'status']
        for zone in self.zones:
            zone_data.append((zone['id'], zone['name'], zone['status']))

        self.view.create_view(headings, zone_data)