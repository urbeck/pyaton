from PyQt5.QtWidgets import*
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import*
from PIL import Image
import os

app = QApplication([])
okno = QWidget()
okno.resize(500,300)
opa = QPushButton(okno)
opa.move(10,10)
opa.setText("open")
chos = QListWidget(okno)
chos.resize(150,200)
chos.move(10,70)
pica = QLabel(okno)

pica.move(200,100)
pica.setText("Здесь будет лес")
chebe = QPushButton(okno)
chebe.move(100,10)

wd = ""
def op1():
    global wd
    wd = QFileDialog.getExistingDirectory()
    files = os.listdir(wd)
    exty = ['.jpg', ".png",".bmp"]
    chos.clear()
    files2 = filter2(files, exty)
    for f in files2:
        chos.addItem(f)
def filter2(files, exty):
    res = []
    for f in files:
        for e in exty:
            if f.endswith(e):
                res.append(f)
    return res
opa.clicked.connect(op1)

path1 = "" #путь к файлу

def pokaz(item):
    global wd, path1 # wd -переменная с адресом папки
    f = chos.currentItem().text() #узнаем имя файла
    path1 = os.path.join(wd, f) #создаем полный путь к файлу, склеив адрес папки и имя
    pix = QPixmap(path1)
    pica.resize(200,200) #ваш QLabel
    pix = pix.scaled(200,200, Qt.KeepAspectRatio) #растягиваем картинку, сохраняя пропорции
    pica.setPixmap(pix) #ваш QLabel
chos.itemClicked.connect(pokaz) #ваш листвиджет

def naming(text):
    global path1,wd
    fin =  path1.rfind('.') #узнаем индекс точки
    okon = path1[fin:] #по индексу "отрезаем" расширение
    nach = path1[:fin] #по индексу получаем адрес файла без расширения
    itog = nach + "-bw" + okon #вклиниваем какой-то свой текст в название
    return itog
def p2(itog):
    global wd, path1
    pix = QPixmap(itog)
    pica.resize(200,200) #ваш QLabel
    pix = pix.scaled(200,200, Qt.KeepAspectRatio) #растягиваем картинку, сохраняя пропорции
    pica.setPixmap(pix) #ваш QLabel
    files = os.listdir(wd)
    exty = ['.jpg', ".png",".bmp"]
    chos.clear()
    files2 = filter2(files, exty)
    for f in files2:
        chos.addItem(f)
def ocern():
    global wd, path1
    imag = Image.open(path1) #открываем файл
    itog = naming(path1) #вынос повторяющейся части кода в отдельную функцию
    mod = imag.convert("L") #накладываем эффект - эту часть нужно менять //в гугле наберите PIL imagefilter
    mod.save(itog) #сохраняем с новым именем
    p2(itog)
chebe.clicked.connect(ocern)


okno.show()
app.exec_()
