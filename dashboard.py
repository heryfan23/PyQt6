import sys
from PyQt6.QtWidgets import QApplication,QMainWindow,QWidget,QVBoxLayout,QHBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy 

class GrapheCanvas(FigureCanvas):
    def __init__(self, parent=None,width=5,height=4,dpi=100):
        fig = Figure(figsize=(width,height),dpi=dpi)
        self.axes = fig.add_subplot(111)
        super().__init__(fig)
        
class Graph_donner(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setFixedSize(1200,600)
        self.setWindowTitle("Afficher graphe")

        fenetre_widget = QWidget()
        self.setCentralWidget(fenetre_widget)

        layout = QVBoxLayout(fenetre_widget)
        layout_1 = QHBoxLayout()
        layout_2 = QHBoxLayout()

        self.fig_1 = GrapheCanvas(self, width=5,height=4,dpi=100)
        self.fig_2 = GrapheCanvas(self, width=5,height=4,dpi=100)
        self.fig_3 = GrapheCanvas(self, width=5,height=4,dpi=100)
        self.fig_4 = GrapheCanvas(self, width=5,height=4,dpi=100)

        layout_1.addWidget(self.fig_1)
        layout.addLayout(layout_1)

        layout_1.addWidget(self.fig_2)
        layout.addLayout(layout_1)

        layout_2.addWidget(self.fig_3)
        layout.addLayout(layout_2)

        layout_2.addWidget(self.fig_4)
        layout.addLayout(layout_2)

        self.plot()

    def plot(self):
        t = numpy.linspace(0,10,500)
        y = numpy.sin(t)

        self.fig_1.axes.plot(t,y)
        self.fig_1.draw()

        mois = ["Janvier","Fevrier","Mars","Avril"]
        valeur = [40,5,10,20]

        self.fig_2.axes.bar(mois,valeur)
        self.fig_2.draw()

        taille = [10,50,20,30]
        mot = ["A","B","C","D"]

        self.fig_3.axes.pie(taille,labels=mot,autopct='%1.1f%%')
        self.fig_3.draw()

        x = [1,2,3,4,5]
        n = [3,2,5,1,9]
        
        self.fig_4.axes.plot(x,n,linestyle="dashed",marker="o")
        self.fig_4.draw()


        

        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    graphe = Graph_donner()
    graphe.show()
    sys.exit(app.exec())
