'''
This program uses qrcode package to create a QR image. Also, the user
has the option to either add or not a picture to be included in the QR
image. The advantage of this program is that it has a GUI using PyQt5.
'''

import sys
import os
import platform
import subprocess
import qrcode

from os import environ
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtWidgets, QtGui
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask

#---------------------Clears the screen at start------------------------
operating_system = platform.system()
if operating_system == "Linux":
    bash_cmd = 'clear'
elif operating_system == "Windows":
    bash_cmd = 'cls'
subprocess.call(bash_cmd, shell=True)
#-----------------------------------------------------------------------

# Used to include the logo into the executable
resource_path = os.path.join(os.path.dirname(__file__), 'res')
logo_path = os.path.join(resource_path, 'logo.png')

class xQR_GEN_GUI(QMainWindow):

    version = "Ver 1.1"
    user_home = os.path.expanduser('~')

    def __init__(self):
        QMainWindow.__init__(self)

        #--------------Labels-------------------

        self.title_lbl = QtWidgets.QLabel(self)
        self.title_lbl.setGeometry(QtCore.QRect(60, 30, 131, 16))
        self.title_lbl.setObjectName("titleLbl")
        self.contents_lbl = QtWidgets.QLabel(self)
        self.contents_lbl.setGeometry(QtCore.QRect(30, 70, 81, 16))
        self.contents_lbl.setObjectName("contentsLbl")
        self.picture_lbl = QtWidgets.QLabel(self)
        self.picture_lbl.setGeometry(QtCore.QRect(30, 120, 161, 16))
        self.picture_lbl.setObjectName("pictureLbl")

        #--------------Text box-------------------

        self.contents_txt_box = QtWidgets.QLineEdit(self)
        self.contents_txt_box.setGeometry(QtCore.QRect(30, 90, 161, 20))
        self.contents_txt_box.setObjectName("contentsTxtBox")
        self.picture_txt_box = QtWidgets.QLineEdit(self)
        self.picture_txt_box.setGeometry(QtCore.QRect(30, 140, 121, 20))
        self.picture_txt_box.setObjectName("pictureTxtBox")

        #--------------Buttons-------------------

        self.about_btn = QtWidgets.QPushButton(self)
        self.about_btn.setGeometry(QtCore.QRect(30, 230, 161, 23))
        self.about_btn.setObjectName("aboutBtn")
        self.how_to_use_btn = QtWidgets.QPushButton(self)
        self.how_to_use_btn.setGeometry(QtCore.QRect(30, 200, 161, 23))
        self.how_to_use_btn.setObjectName("howToUseBtn")
        self.generate_qr_btn = QtWidgets.QPushButton(self)
        self.generate_qr_btn.setGeometry(QtCore.QRect(30, 170, 161, 23))
        self.generate_qr_btn.setObjectName("generateBtn")
        self.picture_select_btn = QtWidgets.QPushButton(self)
        self.picture_select_btn.setGeometry(QtCore.QRect(160, 140, 31, 23))
        self.picture_select_btn.setObjectName("pictureSelectBtn")

        #-------------Buttons actions------------

        self.about_btn.clicked.connect(self.aboutFunc)
        self.how_to_use_btn.clicked.connect(self.howToUseFunc)
        self.generate_qr_btn.clicked.connect(self.check_for_img)
        self.picture_select_btn.clicked.connect(self.picture_browse)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, xQR_GEN_GUI):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("xQR_GEN_GUI", "QRMaker"))

        #--------------Labels-------------------

        self.title_lbl.setText(_translate("xQR_GEN_GUI", "QRMaker - " + self.version))
        self.contents_lbl.setText(_translate("Dialog", "Texto o URL"))
        self.picture_lbl.setText(_translate("xQR_GEN_GUI", "Foto para QR (Opcional)"))

        #--------------Buttons-------------------

        self.about_btn.setText(_translate("xQR_GEN_GUI", "Info"))
        self.how_to_use_btn.setText(_translate("xQR_GEN_GUI", "Como usar"))
        self.generate_qr_btn.setText(_translate("xQR_GEN_GUI", "Generar"))
        self.picture_select_btn.setText(_translate("xQR_GEN_GUI", "..."))

    def generate_qr_with_picture(self, text, pic, save_loc="qr.png"):

        qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
        qr.add_data(text)

        img = qr.make_image(image_factory=StyledPilImage, embeded_image_path=pic)
        img.save(save_loc)

        QMessageBox.information(self, "Listo", f"QR generado en {save_loc}")

    def generate_qr_no_picture(self, text, save_loc="qr.png"):

        img = qrcode.make(text)
        # print(type(img))  # qrcode.image.pil.PilImage
        img.save(save_loc)

        QMessageBox.information(self, "Listo", f"QR generado en {save_loc}")

    def check_for_img(self):

        picture_path = self.picture_txt_box.text()

        if picture_path == "":
            # QMessageBox.information(self, "Listo", "no picture")
            self.generate_qr_no_picture(self.contents_txt_box.text(), self.check_path())
        else:
            # QMessageBox.information(self, "Listo", "picture")
            self.generate_qr_with_picture(self.contents_txt_box.text(), picture_path, self.check_path())

    def check_path(self):
        if operating_system == "Linux":
            return self.user_home + "/Pictures/qr.png"
        elif operating_system == "Windows":
            return self.user_home + "\\Pictures\\qr.png"

    def picture_browse(self):
        """
        
        """
        picture_to_embed = QFileDialog.getOpenFileNames(self, "Seleccione files")[0]

        if not picture_to_embed:
            # This message can be replaced with pass because it would interrupt
            # the user when cancelling the selection
            QMessageBox.information(self, "Aviso", "No se ha seleccionado ningún archivo")
        else:
            # Set text to textbox
            self.picture_txt_box.setText(picture_to_embed[0])

    def aboutFunc(self):
        QMessageBox.information(self, 
            "Informacion", 
            "Hola! Gracias por usar este programa.\n" +
            "Este programa genera una foto de QR con el texto que quieras.\n" +
            "Hecho por Rafael Pippen Moreno")

    def howToUseFunc(self):
        QMessageBox.information(self, 
            "Como usar", 
            "1. Copia y pasa el link o texto que quieras a la barra de Texto o URL.\n" +
            "2. Seleccione los 3 puntos y busque una foto si quieres una en el QR.\n" +
            "Nota: La foto es opcional, si no escoges una el QR se genera sin una.\n" +
            "3. Presiona generar y listo.")


#Turns off QT warnings
def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"

if __name__ == "__main__":

    suppress_qt_warnings()
    app = QApplication(sys.argv)
    ui = xQR_GEN_GUI()
    ui.setObjectName("xQR_GEN_GUI")
    ui.resize(222, 270)
    ui.setWindowIcon(QtGui.QIcon(logo_path))
    ui.show()

    sys.exit(app.exec_())
