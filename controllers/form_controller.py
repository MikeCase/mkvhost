from controllers.controllers import Controller
from gui.form_view import Form
from models.models import CloudFlare


class FormController(Controller):
    def __init__(self):
        self.view = None
        self.model = None

    def bind(self, view: Form, model: CloudFlare):
        view.model = model
        self.view = view
        self.view.create_view()
