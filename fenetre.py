from PyQt6.QtWidgets import QWidget,QApplication,QPushButton,QLineEdit,QLabel
import sys
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QSize,Qt

class Fenetre(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Accueil")
        self.setFixedSize(800,600)

        self.btn = QPushButton(self)
        self.btn.setGeometry(100,100,150,150)
        self.btn.setIcon(QIcon("images/python.png"))
        self.btn.setIconSize(QSize(120,120))
        self.btn.setStyleSheet("border:2px solid black;border-radius:15px")
        self.btn.setCursor(Qt.CursorShape.PointingHandCursor)

        self.btn_cliquer = QPushButton(self,text="Dashboard")
        self.btn_cliquer.setGeometry(270,100,150,50)
        self.btn_cliquer.setIcon(QIcon("images/python.png"))
        self.btn_cliquer.setIconSize(QSize(30,30))
        self.btn_cliquer.setStyleSheet("border:2px solid black;border-radius:15px;color:red;font-size:20px")





if __name__ == "__main__":
    app = QApplication(sys.argv)
    fenetre = Fenetre()
    fenetre.show()
    sys.exit(app.exec())