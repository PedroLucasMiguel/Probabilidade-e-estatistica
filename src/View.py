from PyQt5 import QtCore, QtGui, QtWidgets
from Exponential import Exponential_UI
from Normal import Normal_UI
from Greeter import Greeter_UI
from Results import Results_UI
import sys


class View:
    def __init__(self):
        self.guis_dict = {
            "Greeter": Greeter_UI(),
            "Exponential": Exponential_UI(),
            "Normal": Normal_UI(),
            "Results": Results_UI()
        }

    def get_raw_gui(self, name: str):
        if name in self.guis_dict:
            return self.guis_dict[name]
        else:
            raise Exceptions.GUI_Not_Found
