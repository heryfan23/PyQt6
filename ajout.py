from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QPushButton, QSpinBox, QDateEdit, QRadioButton, QComboBox, QFileDialog, QMessageBox
import sys
from PyQt6.QtCore import QDate, Qt
import os
from req_sql import Inserer_pers, prend_postes, prend_idposte
import shutil


class Ajout(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(800, 700)

        style_text = "color:red;font-size:20px"
        style_input = "color:red;border:2px solid black;border-radius:15px;font-size:15px;padding-left:10px"

        self.nom = QLabel("nom :", self)
        self.nom.setGeometry(100, 50, 150, 40)
        self.nom.setStyleSheet(style_text)

        self.input_nom = QLineEdit(self)
        self.input_nom.setGeometry(250, 50, 250, 40)
        self.input_nom.setStyleSheet(style_input)

        self.pseudo = QLabel("Pseudo :", self)
        self.pseudo.setGeometry(100, 100, 150, 40)
        self.pseudo.setStyleSheet(style_text)

        self.input_pseudo = QLineEdit(self)
        self.input_pseudo.setGeometry(250, 100, 250, 40)
        self.input_pseudo.setStyleSheet(style_input)

        self.age = QLabel("Age :", self)
        self.age.setGeometry(100, 150, 150, 40)
        self.age.setStyleSheet(style_text)

        self.input_age = QSpinBox(self)
        self.input_age.setGeometry(250, 150, 250, 40)
        self.input_age.setStyleSheet(style_input)

        self.email = QLabel("Email :", self)
        self.email.setGeometry(100, 200, 150, 40)
        self.email.setStyleSheet(style_text)

        self.input_email = QLineEdit(self)
        self.input_email.setGeometry(250, 200, 250, 40)
        self.input_email.setStyleSheet(style_input)

        self.contact = QLabel("Contact :", self)
        self.contact.setGeometry(100, 250, 150, 40)
        self.contact.setStyleSheet(style_text)

        self.input_contact = QLineEdit(self)
        self.input_contact.setGeometry(250, 250, 250, 40)
        self.input_contact.setStyleSheet(style_input)

        self.date = QLabel("Date :", self)
        self.date.setGeometry(100, 300, 150, 40)
        self.date.setStyleSheet(style_text)

        self.input_date = QDateEdit(self)
        self.input_date.setGeometry(250, 300, 250, 40)
        self.input_date.setStyleSheet(style_input)
        self.input_date.setCalendarPopup(True)
        self.input_date.setDate(QDate.currentDate())
        self.input_date.installEventFilter(self)

        self.password = QLabel("Password :", self)
        self.password.setGeometry(100, 350, 150, 40)
        self.password.setStyleSheet(style_text)

        self.input_password = QLineEdit(self)
        self.input_password.setGeometry(250, 350, 250, 40)
        self.input_password.setStyleSheet(style_input)
        self.input_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.input_password.setPlaceholderText("entrer votre mdp")

        self.password_conf = QLabel("Password conf :", self)
        self.password_conf.setGeometry(100, 400, 150, 40)
        self.password_conf.setStyleSheet(style_text)

        self.input_password_conf = QLineEdit(self)
        self.input_password_conf.setGeometry(250, 400, 250, 40)
        self.input_password_conf.setStyleSheet(style_input)
        self.input_password_conf.setEchoMode(QLineEdit.EchoMode.Password)
        self.input_password_conf.setPlaceholderText("entrer votre mdp")

        self.sexe = QLabel("sexe :", self)
        self.sexe.setGeometry(100, 450, 150, 40)
        self.sexe.setStyleSheet(style_text)

        self.sexe_h = QRadioButton("Homme", self)
        self.sexe_h.setGeometry(200, 450, 150, 40)

        self.sexe_f = QRadioButton("Femme", self)
        self.sexe_f.setGeometry(300, 450, 150, 40)

        self.nat = QLabel("Nation :", self)
        self.nat.setGeometry(100, 500, 150, 40)
        self.nat.setStyleSheet(style_text)

        self.input_nat = QComboBox(self)
        self.input_nat.setGeometry(250, 500, 250, 40)
        self.input_nat.addItems(["Choisir", "Malagasy", "Français", "Chinois"])
        self.input_nat.setStyleSheet(style_input)

        self.images = QLabel("Images :", self)
        self.images.setGeometry(100, 550, 150, 40)
        self.images.setStyleSheet(style_text)

        self.btn_parcourir = QPushButton("selectionner", self)
        self.btn_parcourir.setGeometry(250, 550, 150, 40)
        self.btn_parcourir.setStyleSheet("""
            QPushButton{
                border-radius:15px;
                font-size:15px;
                background-color:blue;
                color:white;
            }
        """)
        self.btn_parcourir.clicked.connect(self.prendre_image)

        self.chemin_photo = QLabel(self)
        self.chemin_photo.setGeometry(430, 550, 500, 40)

        valeur = []
        postes = prend_postes()
        for poste in postes:
            valeur.append(poste[0])

        self.postes = QLabel("Postes :", self)
        self.postes.setGeometry(100, 620, 150, 40)
        self.postes.setStyleSheet(style_text)

        self.input_postes = QComboBox(self)
        self.input_postes.setGeometry(250, 620, 250, 40)
        self.input_postes.setStyleSheet(style_input)
        self.input_postes.addItems(valeur)

        self.btn_enregistrer = QPushButton("Enregistrer", self)
        self.btn_enregistrer.setGeometry(600, 620, 200, 40)
        self.btn_enregistrer.setStyleSheet("""
            QPushButton{
                border-radius:15px;
                font-size:20px;
                background-color:red;
                color:white;
            }
        """)
        self.btn_enregistrer.clicked.connect(self.enregistrer)

    def prendre_image(self):
        chemin_fichier = QFileDialog()
        chemin_fichier.setNameFilter(
            "Images (*.png *.jpg *.gif *.jpeg *.jfif)")
        if chemin_fichier.exec():
            select_fich = chemin_fichier.selectedFiles()
            if select_fich:
                image_path = select_fich[0]
                che_relative = os.path.basename(image_path)
                self.chemin_photo.setText(che_relative)

                dest = "images_pers"
                if not os.path.exists(dest):
                    os.makedirs(dest)

                chemin = os.path.join(dest, che_relative)
                shutil.copy(image_path, chemin)

    def enregistrer(self):
        nom_poste = self.input_postes.currentText()

        id_poste = prend_idposte(nom_poste)

        nom = self.input_nom.text()
        pseudo = self.input_pseudo.text()
        age = self.input_age.value()
        contact = self.input_contact.text()
        date = self.input_date.text()
        mdp1 = self.input_password.text()
        mdp2 = self.input_password_conf.text()
        email = self.input_email.text()

        # if self.sexe_h.isChecked():
        #     sexe = "Homme"
        # else:
        #     sexe = "Femme"
        sexe = "Homme" if self.sexe_h.isChecked() else "Femme"
        nat = self.input_nat.currentText()
        image = self.chemin_photo.text()

        print(nom, pseudo, age, contact, date, mdp1, mdp2, sexe, nat, image)

        Inserer_pers(nom, pseudo, age, contact, email, date,
                     mdp1, sexe, image, nat, mdp2, id_poste[0])

        self.Message_info()

    def Message_info(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setWindowTitle("Informations")
        msg.setText("Donner enregistre dans base")
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    fen = Ajout()
    fen.show()
    sys.exit(app.exec())
