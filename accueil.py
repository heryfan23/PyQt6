from PyQt6.QtWidgets import QWidget,QApplication,QPushButton,QLabel,QLineEdit,QComboBox,QFileDialog
import sys
from tkinter import filedialog
from yt_dlp import YoutubeDL


class YoutubeDown(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(600,500)
        self.setWindowTitle("Telecharge  youtube")

        self.titre = QLabel(self,text="Telecharger video Youtube")
        self.titre.setGeometry(100,20,500,40)
        self.titre.setStyleSheet("color:red;font-size:20px")

        self.text = QLabel(self,text="Ampidiro eto ny rohy \n youtube")
        self.text.setGeometry(100,100,400,100)
        self.text.setStyleSheet("color:green;font-size:40px")

        self.lien = QLineEdit(self)
        self.lien.setGeometry(100,220,250,40)
        self.lien.setStyleSheet("border-radius:15px;border:2px solid black")

        self.btn = QPushButton(self,text="Telecharger")
        self.btn.setGeometry(100,350,150,40)
        self.btn.setStyleSheet("border-radius:15px;border:2px solid black")
        self.btn.clicked.connect(self.telecharger)

        self.format = QComboBox(self)
        self.format.addItems(["choix","mp3","mp4"])
        self.format.setGeometry(100,280,100,40)



    def telecharger(self):
        lien = self.lien.text()
        format = self.format.currentText()
        print(lien,format)
        dest_fichier = filedialog.askdirectory()

        if lien and format and dest_fichier:
            try:
                vide_down ={
                    "format":format,
                    "outtmpl" : f'{dest_fichier}/%(title)s.%(ext)s'
                }
                with YoutubeDL(vide_down) as ydl:
                    ydl.download([lien])
                    print("video bien telecharger")
            except Exception as e:
                print(f"error {e}")
                
if __name__ == "__main__":
    app = QApplication(sys.argv)
    down = YoutubeDown()
    down.show()
    sys.exit(app.exec())

    