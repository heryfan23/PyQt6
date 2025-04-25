from PyQt6.QtWidgets import QWidget, QApplication, QLabel, QLineEdit, QPushButton
import sys
from PyQt6.QtGui import QIcon, QCursor
from PyQt6.QtCore import Qt


class Fenetre(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 1000, 500)
        # self.setFixedHeight(300)
        # self.setFixedWidth(500)

        self.setFixedSize(1000, 500)
        self.setWindowTitle("Python App")
        self.setWindowIcon(QIcon("images/python.png"))

        style_text = "color:white;background-color:red;border-radius:15px;padding-left:100px;font-size:30px;"

        self.titre = QLabel(self, text="Application Bureau")
        self.titre.setGeometry(300, 20, 500, 70)
        self.titre.setStyleSheet(style_text)

        self.search = QLabel(self, text="Recherche :")
        self.search.setGeometry(200, 95, 150, 50)
        self.search.setStyleSheet("""
            QLabel{
                color:red;
                font-size:20px;
            }
        """)

        self.input_search = QLineEdit(self)
        self.input_search.setGeometry(320, 100, 250, 40)
        self.input_search.setPlaceholderText("Entrer mot")

        self.btn = QPushButton(self, text="Rechercher")
        self.btn.setGeometry(600, 100, 150, 40)
        self.btn.setStyleSheet("""
            QPushButton{
                color:red;
                background-color:black;
                font-size:20px;
                border-radius:15px;
            }
            QPushButton:hover{
                color:white;
                background-color:red;
            }
        """)
        self.btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    fen = Fenetre()
    fen.show()
    sys.exit(app.exec())
