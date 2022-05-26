from PyQt5.QtWidgets import QPushButton
from pyqt_ani_abstractbutton import AniAbstractButton


class AniButton(QPushButton, AniAbstractButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)