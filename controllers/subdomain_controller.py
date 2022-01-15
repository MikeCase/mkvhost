from gui.subdomain_view import SubdomainView
from controllers.controllers import Controller
from models.models import CloudFlare

class SubdomainController(Controller):
    def __init__(self):
        self.view = None
        self.model = None

    def bind(self, view: SubdomainView, model: CloudFlare):
        view.model = model
        self.view = view
        self.model = model
        self.view.create_view()

