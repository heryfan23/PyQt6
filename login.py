from PyQt6.QtWidgets import QWidget,QApplication,QLabel,QLineEdit,QPushButton
from PyQt6.QtGui import QPixmap
import sys
from signup import Signup

class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(800,500)
        # self.setGeometry(0,0,800,500)

        self.photo = QLabel(self)
        fond = QPixmap("images/python.png")
        taille_images = fond.scaled(800,500)
        self.photo.setPixmap(taille_images)
        self.photo.setGeometry(0,0,800,500)

        self.espace_log = QLabel(self)
        self.espace_log.setGeometry(200,50,400,400)
        self.espace_log.setStyleSheet("background-color:rgba(1,1,0.5,0.7);border-radius:15px")

        style = "color:white;font-size:20px"
        style_btn = "color:black;font-size:15px;border-radius:10px;padding-left:5px"

        self.email = QLabel(self,text="Email :")
        self.email.setGeometry(220,150,150,40)
        self.email.setStyleSheet(style)

        self.input_email = QLineEdit(self)
        self.input_email.setGeometry(350,150,200,40)
        self.input_email.setStyleSheet(style_btn)

        self.mdp = QLabel(self,text="Password :")
        self.mdp.setGeometry(220,220,150,40)
        self.mdp.setStyleSheet(style)

        self.input_mdp = QLineEdit(self)
        self.input_mdp.setGeometry(350,220,200,40)
        self.input_mdp.setStyleSheet(style_btn)
        self.input_mdp.setEchoMode(QLineEdit.EchoMode.Password)

        self.btn = QPushButton(self,text="Se Connecter")
        self.btn.setGeometry(330,280,150,50)
        self.btn.setStyleSheet("""
            QPushButton{
                color:black;
                border-radius:15px;
                font-size:20px;
                background-color:blueviolet;
            }
            QPushButton:hover{
                color:red;
                background-color:aqua;
            }
        """)

        self.btn_to_signup = QPushButton(self,text="Si pas de Compte !! cliquer ici")
        self.btn_to_signup.setGeometry(300,340,180,50)
        self.btn_to_signup.setStyleSheet("border:none;border-bottom:1px solid black;color:white")
        self.btn_to_signup.clicked.connect(self.inscription)

    def inscription(self):
        # print("ok")
        self.close()
        self.ouvrir_fen = Signup()
        self.ouvrir_fen.show()
        










if __name__ == "__main__":
    app = QApplication(sys.argv)
    connex = Login()
    connex.show()
    sys.exit(app.exec())