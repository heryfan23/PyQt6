from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QPushButton, QTableWidget, QTableWidgetItem, QAbstractItemView, QFrame, QMessageBox,QFileDialog
import sys
from PyQt6.QtCore import QDate, Qt
from PyQt6.QtGui import QPixmap, QColor
import os
from req_sql import affficher_pers, suppression, modifier, faire_rechercher, prend_postes,pred_selectionner
from openpyxl import Workbook
import pdfkit


class Affichage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tableau affichage")
        self.setFixedSize(1000, 600)

        self.listes_pers = QLabel(self, text="Nbr Pers :")
        self.listes_pers.setGeometry(100, 50, 200, 50)
        self.listes_pers.setStyleSheet("color:red;font-size:25px")

        donner_pers = affficher_pers()

        self.nbr = QLabel(self, text=str(len(donner_pers)))
        self.nbr.setGeometry(230, 50, 100, 50)
        self.nbr.setStyleSheet("font-size:25px")

        self.input_recherche = QLineEdit(self)
        self.input_recherche.setGeometry(400, 50, 200, 35)
        self.input_recherche.setStyleSheet(
            "border:2px solid red;border-radius:15px;font-size:15px;padding-left:10px")

        self.btn_rech = QPushButton(self, text="Rechercher")
        self.btn_rech.setGeometry(620, 50, 100, 35)
        self.btn_rech.setStyleSheet(
            "background-color:red;color:white;border-radius:10px")
        self.btn_rech.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_rech.clicked.connect(self.rechercher)

        nbr_ligne = len(donner_pers)
        nbr_colonne = 15

        self.table = QTableWidget(nbr_ligne, nbr_colonne, self)
        # self.table.setRowCount(10)
        # self.table.setColumnCount(13)
        self.table.setGeometry(100, 150, 850, 400)
        self.table.setHorizontalHeaderLabels(["id", "Nom", "pseudo", "age", "contact", "email", "date",
                                             "password", "sexe", "image", "nationaliter", "matricule","postes", "modifier", "supprimer"])

        self.table.setStyleSheet("""
            QTableWidget{
                background-color:gray; 
                border:1px solid black;
                font-size:15px;          
            }
            QTableWidget::item{
                padding:2px;
            }
            QTableWidget::item:selected{
                background-color:red;
                color:white;
            }
        """)
        header = self.table.horizontalHeader()
        header.setStyleSheet("""
            QHeaderView::section{
                background-color:red;
                color:white;
                font-weight:bolder;
            }
        """)
        header.setDefaultAlignment(Qt.AlignmentFlag.AlignCenter)

        self.table.setColumnWidth(0, 0)
        self.table.setColumnWidth(1, 150)

        self.table.itemClicked.connect(self.affiche_image)

        for i in range(nbr_ligne):
            btn_modifier = QPushButton("Modifier")
            btn_modifier.setStyleSheet("background-color:aqua")
            self.table.setCellWidget(i, 13, btn_modifier)
            btn_modifier.clicked.connect(self.modifier(i))

            btn_supr = QPushButton("Supprimer")
            btn_supr.setStyleSheet("background-color:aqua")
            self.table.setCellWidget(i, 14, btn_supr)
            btn_supr.clicked.connect(self.supprimer(i))

        for ligne, liste in enumerate(donner_pers):
            for col, value in enumerate(liste):
                if col == 9:
                    if value:
                        label = QLabel()
                        pixmap = QPixmap(f"images_pers/{value}")
                        taille_image = pixmap.scaled(50, 50)
                        label.setPixmap(taille_image)
                        self.table.setCellWidget(ligne, col, label)
                        item = QTableWidgetItem(f"images_pers/{value}")
                        self.table.setItem(ligne, 9, item)

                        item.setForeground(QColor(240, 248, 255, 0))
                else:
                    item = QTableWidgetItem(str(value))
                    self.table.setItem(ligne, col, item)

        self.fenetre_popup = QFrame(self)
        self.fenetre_popup.setGeometry(100, 150, 850, 400)
        self.fenetre_popup.setStyleSheet(
            "background-color:gray;border-radius:15px")

        self.label_image = QLabel(self.fenetre_popup)
        self.label_image.setGeometry(0, 0, 850, 400)

        self.btn_close = QPushButton(self.fenetre_popup, text="X")
        self.btn_close.setGeometry(800, 10, 50, 50)
        self.btn_close.setStyleSheet(
            "color:white;background-color:red;font-size:20px")
        self.btn_close.clicked.connect(self.fermer)

        self.fenetre_popup.setVisible(False)
        
        self.btn_excel = QPushButton(self,text="Imprimer Excel")
        self.btn_excel.setGeometry(300,550,200,30)
        self.btn_excel.clicked.connect(self.importer_excel)
        
        self.btn_pdf = QPushButton(self,text="Imprimer pdf")
        self.btn_pdf.setGeometry(500,550,200,30)
        self.btn_pdf.clicked.connect(self.importer_pdf)
    def affiche_image(self, item):
        res = self.table.selectedItems()
        res.sort(key=lambda x: x.row())
        valeurs = [item.text() for item in res]
        # print(valeurs)

        col = item.column()
        row = item.row()
        chemin_images = item.text()

        # print(col, row, chemin_images)

        if col == 9:
            self.images = QPixmap(chemin_images)
            self.label_image.setPixmap(self.images.scaled(850, 400))

            self.fenetre_popup.setVisible(True)
            
        
        self.id = self.table.item(row,0).text()
        # print(self.id)
        
        self.resultats = pred_selectionner(self.id)
        print(self.resultats)
        
        
       
    def importer_pdf(self):
        chemin_pdf,_ = QFileDialog.getSaveFileName(self,"Enregistrer","","Fichiers pdf(*.pdf)")
        
        if chemin_pdf:
            html_pdf = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="UTF-8">
                <title>Facture Proforma</title>
            </head>
            <body style="font-family: Arial, sans-serif; margin: 20px;">
                <div style="text-align: center; margin-bottom: 30px;">
                    <h1>FACTURE PROFORMA</h1>
                </div>

                <div style="float: left; width: 50%;">
                    <h3>Votre Entreprise</h3>
                    <p>Adresse de l'entreprise<br>
                    Téléphone: {self.resultats[0][4]}<br>
                    Email: {self.resultats[0][5]}</p>
                </div>

                <div style="float: right; width: 50%; text-align: right;">
                    <h3>Client</h3>
                    <p>{self.resultats[0][1]}<br>
                    {self.resultats[0][11]}<br>
                    Facture N°: PRO-{self.resultats[0][7]}<br>
                    Date: {self.resultats[0][6]}</p>
                </div>

                <div style="clear: both;"></div>

                <table style="width: 100%; border-collapse: collapse; margin: 20px 0;">
                    <thead>
                        <tr>
                            <th style="border: 1px solid #ddd; padding: 8px; text-align: left; background-color: #f2f2f2;">Description</th>
                            <th style="border: 1px solid #ddd; padding: 8px; text-align: left; background-color: #f2f2f2;">Quantité</th>
                            <th style="border: 1px solid #ddd; padding: 8px; text-align: left; background-color: #f2f2f2;">Prix unitaire</th>
                            <th style="border: 1px solid #ddd; padding: 8px; text-align: left; background-color: #f2f2f2;">Total</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td style="border: 1px solid #ddd; padding: 8px; text-align: left;">Produit/Service 1</td>
                            <td style="border: 1px solid #ddd; padding: 8px; text-align: left;">1</td>
                            <td style="border: 1px solid #ddd; padding: 8px; text-align: left;">100.00 €</td>
                            <td style="border: 1px solid #ddd; padding: 8px; text-align: left;">100.00 €</td>
                        </tr>
                        <tr>
                            <td style="border: 1px solid #ddd; padding: 8px; text-align: left;">Produit/Service 2</td>
                            <td style="border: 1px solid #ddd; padding: 8px; text-align: left;">2</td>
                            <td style="border: 1px solid #ddd; padding: 8px; text-align: left;">50.00 €</td>
                            <td style="border: 1px solid #ddd; padding: 8px; text-align: left;">100.00 €</td>
                        </tr>
                    </tbody>
                </table>

                <div style="text-align: right; margin-top: 20px;">
                    <p><strong>Total HT: </strong>200.00 €</p>
                    <p><strong>TVA (20%): </strong>40.00 €</p>
                    <p><strong>Total TTC: </strong>240.00 €</p>
                </div>

                <div style="margin-top: 40px;">
                    <p><em>Cette facture proforma n'a pas valeur de facture définitive</em></p>
                </div>
            </body>
            </html>

            """
            try:
                path_html_pdf = r"C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"
                config = pdfkit.configuration(wkhtmltopdf=path_html_pdf)
                pdfkit.from_string(html_pdf,chemin_pdf,configuration=config)
            except Exception as e:
                print(f"erreur {e}")
        
    def importer_excel(self):
        try:
            donner = affficher_pers()
            ouvr_excel = Workbook()
            fenetre_excel = ouvr_excel.active
            
            header = ["Numero","nom","pseudo","age","contact","email","date","password","sexe","images","nationalites","matricule","nom_poste"]
            
            fenetre_excel.append(header)
            
            for listes in donner:
                fenetre_excel.append(listes)
            
            dest,_ = QFileDialog.getSaveFileName(self,"Enregistrer","","Fichiers Excle(*.xslx)")
            
            ouvr_excel.save(dest)
            
        except ValueError as e:
            print(f"erreur {e}")
            
    def fermer(self):
        self.fenetre_popup.setVisible(False)

    def rechercher(self):
        mot_rechercher = self.input_recherche.text()

        res_rechercher = faire_rechercher(mot_rechercher)
        self.table.setRowCount(len(res_rechercher))

        for i in range(len(res_rechercher)):
            btn_modifier = QPushButton("Modifier")
            btn_modifier.setStyleSheet("background-color:aqua")
            self.table.setCellWidget(i, 12, btn_modifier)
            btn_modifier.clicked.connect(self.modifier(i))

            btn_supr = QPushButton("Supprimer")
            btn_supr.setStyleSheet("background-color:aqua")
            self.table.setCellWidget(i, 13, btn_supr)
            btn_supr.clicked.connect(self.supprimer(i))
        for ligne, liste in enumerate(res_rechercher):
            for col, value in enumerate(liste):
                if col == 9:
                    if value:
                        label = QLabel()
                        pixmap = QPixmap(f"images_pers/{value}")
                        taille_image = pixmap.scaled(50, 50)
                        label.setPixmap(taille_image)
                        self.table.setCellWidget(ligne, col, label)
                        item = QTableWidgetItem(f"images_pers/{value}")
                        self.table.setItem(ligne, 9, item)

                        item.setForeground(QColor(240, 248, 255, 0))
                else:
                    item = QTableWidgetItem(str(value))
                    self.table.setItem(ligne, col, item)

    

    def supprimer(self, row):
        return lambda: self.action_suppr(row)

    def action_suppr(self, row):
        self.id = self.table.item(row, 0).text()
        self.table.removeRow(row)
        # print(self.id)
        suppression(self.id)

    def modifier(self, row):
        return lambda: self.action_modif(row)

    def action_modif(self, row):
        self.id = self.table.item(row, 0).text()
        # print(self.id)
        nom = self.table.item(row, 1).text()
        pseudo = self.table.item(row, 2).text()
        age = self.table.item(row, 3).text()
        contact = self.table.item(row, 4).text()
        email = self.table.item(row, 5).text()
        date = self.table.item(row, 6).text()
        sexe = self.table.item(row, 8).text()
        nation = self.table.item(row, 10).text()
        matr = self.table.item(row, 11).text()
        print(self.id, nom, pseudo, age, contact,
              email, date, sexe, nation, matr)
        try:
            modifier(self.id, nom, pseudo, age, contact,
                     email, date, sexe, nation, matr)
            QMessageBox.information(
                self, "Succès", "Personnel Modifier avec succès")
        except Exception as e:
            QMessageBox.critical(self, "Erreur", f"erreur de modification {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    fen = Affichage()
    fen.show()
    sys.exit(app.exec())
