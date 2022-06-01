# pyqt-ani-button
PyQt QPushButton for animation

## Requirements
* PyQt5 >= 5.8

## Setup
`python -m pip install pyqt-ani-button`

## Included Package
* <a href="https://github.com/yjg30737/pyqt-ani-abstractbutton.git">pyqt-ani-abstractbutton</a>

## Example
```python
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout
from pyqt_ani_button import AniButton


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        lay = QHBoxLayout()
        for i in range(5):
            btn = AniButton()
            btn.setFixedSize(30, 15)
            lay.addWidget(btn)
        self.setLayout(lay)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ex = Widget()
    ex.show()
    sys.exit(app.exec_())
```

Result

https://user-images.githubusercontent.com/55078043/171344503-f092e025-8329-447a-a02e-a7ca88b5c859.mp4


