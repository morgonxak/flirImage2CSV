'''
В классе воспроизведения попробывать исправить if status поставить перед цыклом
'''

import os
import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import QSize, Qt, pyqtSignal, QThread
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget, QTableWidgetItem, QTableWidgetSelectionRange, QSpinBox
from mainForm import Ui_MainWindow
import subprocess

def processing(pathImage, pathSaveSCV):
    '''
    ОТправляет данные в программу на С#
    :param pathImage:
    :param pathSaveSCV:
    :return:
    '''
    pathProgramm = os.getcwd()

    command = pathProgramm+"\programm\Save2CSV.exe {} {}".format(pathImage, pathSaveSCV)
    p1 = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    out = p1.stdout.read()
    print(out)

class controller():

    def __init__(self):

        self._app = QtWidgets.QApplication(sys.argv)
        self._view = mainForm()


    def run(self):
        '''
        Запускает приложение
        :return:
        '''
        self._view.show()
        return self._app.exec_()


class mainForm(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.onClick_openImages)
        self.ui.pushButton_2.clicked.connect(self.onClick_saveCSV)
        self.ui.pushButton_3.clicked.connect(self.onClick_runProcess)

        self.path_image = None
        self.path_save = None


    def onClick_openImages(self):
        fname = QtWidgets.QFileDialog.getExistingDirectory(self, 'Папка с фотографиями Flir', '/home')
        if fname != '':
            print("path", fname)
            self.path_image= fname

    def onClick_saveCSV(self):
        fname = QtWidgets.QFileDialog.getExistingDirectory(self, 'Паака для сохранения', '/home')
        if fname != '':
            print("path", fname)
            self.path_save = fname

    LIST_FORMAT = ['.jpg', '.JPG']

    def onClick_runProcess(self):
        if not self.path_image is None and not self.path_save is None:
            self.ui.progressBar.setValue(0)

            listImage = os.listdir(self.path_image)
            self.ui.progressBar.setMinimum(0)
            self.ui.progressBar.setMaximum(len(listImage)-1)
            print(len(listImage))
            processing_count_image = 0
            for count, nameImage in enumerate(listImage):
                if nameImage[nameImage.rfind('.'):] in self.LIST_FORMAT:

                    path_image = os.path.join(self.path_image, nameImage)
                    path_save = os.path.join(self.path_save, nameImage[:nameImage.rfind('.')] + '.csv')

                    print(path_image, path_save)
                    processing(path_image, path_save)

                    processing_count_image = processing_count_image + 1

                self.ui.progressBar.setValue(count*100/len(listImage))
            self.showMessage("Обработанно фотографий: "+ str(processing_count_image))

    def showMessage(self, message):
        '''
        Вывод обычного сообщения
        :param messtage:
        :return:
        '''
        messageBox = QtWidgets.QMessageBox(self)
        messageBox.setText(str(message))
        messageBox.exec_()

def main():
    controll = controller()
    controll.run()

if __name__ == '__main__':
    sys.exit(main())