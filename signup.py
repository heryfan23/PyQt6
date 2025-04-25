from PyQt6.QtWidgets import QWidget,QApplication,QLabel,QLineEdit,QPushButton,QDateTimeEdit,QDateEdit,QSpinBox
from PyQt6.QtGui import QPixmap
import sys

class Signup(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(800,500)

        self.btn = QPushButton(self,text="Page login")
        self.btn.clicked.connect(self.login)
        self.btn.setGeometry(10,10,200,40)

        self.date = QDateTimeEdit(self)
        self.date.setGeometry(10,50,200,40)


    
    def login(self):
        self.close()
        from login import Login
        self.log = Login()
        self.log.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    inscrit = Signup()
    inscrit.show()
    sys.exit(app.exec())