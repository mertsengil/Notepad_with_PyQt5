import sys
from PyQt5 import QtWidgets
import os

class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: #434343;")
        self.resize(614, 449)
        self.init_ui()


    def init_ui(self):
        #menu islemleri

        self.menu = QtWidgets.QMenuBar()
        self.menu.setStyleSheet("background-color: #ffaa00;\n"
                                "color: rgb(33, 33, 33);\n"
                                "selection-background-color: rgb(67, 67, 67);\n"
                                "selection-color: rgb(255, 170, 0);")


        dosya = self.menu.addMenu("Dosya")


        #dosya
        yeni = QtWidgets.QAction("Yeni",self)
        dosya_ac = QtWidgets.QAction("Dosya aç",self)
        dosya_ac.setShortcut("Ctrl+o")
        dosya_kaydet = QtWidgets.QAction("Kaydet",self)
        dosya_kaydet.setShortcut("Ctrl+s")
        exit = QtWidgets.QAction("Çıkış",self)
        exit.setShortcut("Ctrl+q")

        dosya.addAction(yeni)
        dosya.addAction(dosya_ac)
        dosya.addAction(dosya_kaydet)
        dosya.addAction(exit)

        #düzenle


        #-------------------------- end of menu --------------------------------


        #---------------------- notepad -----------------------------------------

        self.not_defteri = QtWidgets.QTextEdit()
        self.not_defteri.setStyleSheet("background-color: rgb(255, 170, 0);\n"
                                    "color: #313131;\n"
                                       "font: 75 14pt 'MS Shell Dlg 2';")

        self.temizle = QtWidgets.QPushButton("Temizle")
        self.temizle.setStyleSheet("background-color: rgb(255, 170, 0);\n"
                                      "color: black;\n"
                                      "font: 75 10pt 'MS Shell Dlg 2';\n")

        h_box = QtWidgets.QHBoxLayout()

        h_box.addWidget(self.temizle)
        h_box.addStretch()

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.menu)
        v_box.addWidget(self.not_defteri)
        v_box.addLayout(h_box)
        self.setLayout(v_box)
        self.setWindowTitle("Notepad - Made By Mert Sengil V0.1")

        yeni.triggered.connect(self.newone)
        dosya_ac.triggered.connect(self.open)
        dosya_kaydet.triggered.connect(self.save)
        exit.triggered.connect(self.exit)

        self.temizle.clicked.connect(self.delete_all)
        self.show()

    def newone(self):
        self.not_defteri.clear()
    def open(self):
        dosya_ismi = QtWidgets.QFileDialog.getOpenFileName(self,"Dosya aç",os.getenv("Desktop"))
        with open(dosya_ismi[0],"r") as file:
            self.not_defteri.setText(file.read())
    def save(self):
        dosya_ismi = QtWidgets.QFileDialog.getSaveFileName(self,"Dosya Kaydet",os.getenv("Desktop"))
        with open(dosya_ismi[0],"w") as file:
            file.write(self.not_defteri.toPlainText())
    def exit(self):
        QtWidgets.qApp.quit()
    def delete_all(self):
        self.not_defteri.clear()

app = QtWidgets.QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())