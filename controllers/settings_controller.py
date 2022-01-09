import os
from gui.settings_view import SettingsView
from controllers.controllers import Controller
from models.models import CloudFlare

class SettingsController(Controller):

    def __init__(self):
        self.view = None
        self.model = None
        

    def bind(self, view: SettingsView, model: CloudFlare):
        view.model = model
        self.view = view
        self.model = model
        self.view.create_view()