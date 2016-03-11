from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys

class HelloWorld(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        self.layout = QVBoxLayout()
        self.label = QLabel("Hello World")
        line_edit = QLineEdit()
        button = QPushButton("Close")

        self.layout.addWidget(self.label)
        self.layout.addWidget(line_edit)
        self.layout.addWidget(button)

        self.setLayout(self.layout)
        self.ok_button = QPushButton("Im new here!")

        button.clicked.connect(self.close)
        line_edit.textChanged.connect(self.change_text)


    def change_text(self, text):
        self.label.setText( text )


app = QApplication(sys.argv)
dialog = HelloWorld()
dialog.show()

sys.exit( app.exec_() )


