import os
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication,QWidget,QPushButton,QLabel,
QListWidget,
QLineEdit,QTextEdit,QInputDialog,
QHBoxLayout,QVBoxLayout,QFormLayout,QMessageBox,QFileDialog)
import json
from PIL import Image
from PIL.ImageQt import ImageQt # для перевода графики из Pillow в Qt 
from PIL import ImageFilter
from PIL.ImageFilter import (
   BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
   EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN,
   GaussianBlur, UnsharpMask
) 
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

#создание окна
app = QApplication([])
win = QWidget()
win.setWindowTitle('Фотошоп братан фотошоп')
win.resize(900,600)

#создание виджетов
label = QLabel('Картинка')
list_widget = QListWidget()
pb_papka = QPushButton('Папка')
pb_left = QPushButton('Лево')
pb_right = QPushButton('Право')
pb_miror = QPushButton('Зеркало')
pb_rezkozt = QPushButton('Резкость')
pb_hb = QPushButton('Ч/Б')

#создание лайаутов
main_h_layout = QHBoxLayout()
h_layout_1 = QHBoxLayout()
v_layout_1 =QVBoxLayout()
v_layout_2 =QVBoxLayout()

#вывод лайаутов
v_layout_1.addWidget(pb_papka)
v_layout_1.addWidget(list_widget)

h_layout_1.addWidget(pb_left)
h_layout_1.addWidget(pb_right)
h_layout_1.addWidget(pb_miror)
h_layout_1.addWidget(pb_rezkozt)

v_layout_2.addWidget(label)
v_layout_2.addLayout(h_layout_1)

main_h_layout.addLayout(v_layout_1,20)
main_h_layout.addLayout(v_layout_2,80)

win.setLayout(main_h_layout)

#создание функции
def choseeWorkdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()

def filter(files,extension):
    result = []
    for filename in files:
        for ext in extension:
            if filename.endswith(ext):
                result.append(filename)
    return result

def showDileNamelist():
    extension = ['.jpg','.png','.jpeg','.gif','.bmp']
    choseeWorkdir()
    filenames = filter(os.listdir(workdir),extension)
    list_widget.clear()
    for filename in filenames:
        list_widget.addItem(filename)

class ImageProcessor():
    def __init__(self,):
        self.image = None
        self.dir = None
        self.filename = None
        self.save_dir = 'Modfiled/'

    def loadImage(self,filename):
        self.filename = filename
        fullname = os.path.join(workdir,filename)
        self.image = Image.open(fullname)

    def showImage(self,path):
        label.hide()
        pixmapimage = QPixmap(path)
        w,h = label.width(),label.height()
        pixmapimage = pixmapimage.scaled(w,h,Qt.KeepAspectRatio)
        label.show()

    def save_image():
        path = os.path.join(workdir,self.save_dir)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        fullname = os.path.join(path,self.filename)
        self.image.save(fullname)

def showchosenimage():  
   if list_widget.currentRow() >= 0:
       filename = list_widget.currentItem().text()
       workimage.loadImage(filename)
       workimage.showImage(os.path.join(workdir,workimage.filename))

workimage = ImageProcessor()
list_widget.currentRowChanged.connect(showchosenimage)
pb_papka.clicked.connect(showDileNamelist)

win.show()
app.exec_()