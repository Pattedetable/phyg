#
# Copyright 2017-2022 Manuel Barrette
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from PyQt6 import QtCore, QtGui, QtWidgets
import interference_main_window
import onde_stationnaire_main_window
import harmonique_main_window
import modes_main_window
import dialog_onde
import dialog_interference
import dialog_harmonique
import dialog_modes
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, Dialog, ui_Dialog):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(374, 261) # (374, 261)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)

        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 2, 1, 1)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 3, 3, 1, 1)

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 1, 3, 1, 1)

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 1, 0, 1, 1)

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 1, 1, 1, 1)

        directory = "images"

        self.label = QtWidgets.QLabel(self.centralwidget)
        image = os.path.join(directory, "diffraction.png")
        self.label.setPixmap(QtGui.QPixmap(image))
        self.label.setScaledContents(True)
        self.label.setMinimumSize(200, 200)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 3, 1, 1)

        self.label2 = QtWidgets.QLabel(self.centralwidget)
        image = os.path.join(directory, "son.png")
        self.label2.setPixmap(QtGui.QPixmap(image))
        self.label2.setScaledContents(True)
        self.label2.setMinimumSize(200, 200)
        self.label2.setObjectName("label2")
        self.gridLayout.addWidget(self.label2, 0, 2, 1, 1)

        self.label3 = QtWidgets.QLabel(self.centralwidget)
        image = os.path.join(directory, "pendule.png")
        self.label3.setPixmap(QtGui.QPixmap(image))
        self.label3.setScaledContents(True)
        self.label3.setMinimumSize(200, 200)
        self.label3.setObjectName("label3")
        self.gridLayout.addWidget(self.label3, 0, 0, 1, 1)

        self.label4 = QtWidgets.QLabel(self.centralwidget)
        image = os.path.join(directory, "corde.png")
        self.label4.setPixmap(QtGui.QPixmap(image))
        self.label4.setScaledContents(True)
        self.label4.setMinimumSize(200, 200)
        self.label4.setObjectName("label4")
        self.gridLayout.addWidget(self.label4, 0, 1, 1, 1)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 374, 25))
        self.menubar.setObjectName("menubar")
        self.menuAide = QtWidgets.QMenu(self.menubar)
        self.menuAide.setObjectName("menuAide")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_propos = QtGui.QAction(MainWindow)

        self.action_translate = QtWidgets.QMenu(MainWindow)
        self.action_translate.setObjectName("action_translate")
        self.menuAide.addMenu(self.action_translate)

        self.action_fr = QtGui.QAction(MainWindow)
        self.action_fr.setObjectName("action_fr")
        self.action_translate.addAction(self.action_fr)
        self.action_en = QtGui.QAction(MainWindow)
        self.action_en.setObjectName("action_en")
        self.action_translate.addAction(self.action_en)

        self.action_propos.setObjectName("action_propos")
        self.menuAide.addAction(self.action_propos)
        self.menubar.addAction(self.menuAide.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.action_propos.triggered.connect(lambda: Dialog.show())
        self.action_fr.triggered.connect(lambda: self.traduire(MainWindow, Dialog, ui_Dialog, "fr_CA"))
        self.action_en.triggered.connect(lambda: self.traduire(MainWindow, Dialog, ui_Dialog, "en_CA"))
        self.pushButton_2.clicked.connect(lambda: self.lancerOnde(MainWindow))
        self.pushButton.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.pushButton_3.clicked.connect(lambda: self.lancerInterference(MainWindow))
        self.pushButton_4.clicked.connect(lambda: self.lancerMHS(MainWindow))
        self.pushButton_5.clicked.connect(lambda: self.lancerModes(MainWindow))


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Phyg"))
        self.pushButton_2.setText(_translate("MainWindow", "Onde sonore stationnaire"))
        self.pushButton.setText(_translate("MainWindow", "Quitter"))
        self.pushButton_3.setText(_translate("MainWindow", "Interférence et diffraction"))
        self.pushButton_4.setText(_translate("MainWindow", "Mouvement harmonique"))
        self.pushButton_5.setText(_translate("MainWindow", "Modes propres"))
        self.menuAide.setTitle(_translate("MainWindow", "Options"))
        self.action_translate.setTitle(_translate("MainWindow", "Langue"))
        self.action_fr.setText(_translate("MainWindow", "Français"))
        self.action_en.setText(_translate("MainWindow", "English"))
        self.action_propos.setText(_translate("MainWindow", "À propos"))

    def traduire(self, MainWindow, Dialog, ui_Dialog, langue):
        directory = "locales"
        self.translator = QtCore.QTranslator()
        self.translator.load(langue, directory)
        QtCore.QCoreApplication.installTranslator(self.translator)
        self.retranslateUi(MainWindow)
        ui_Dialog.retranslateUi(Dialog)

# import ressources_rc

    def lancerOnde(self, MainWindow):
        window = QtWidgets.QMainWindow()
        dialog = QtWidgets.QDialog()
        ui = onde_stationnaire_main_window.Ui_MainWindow()
        ui_Dial = dialog_onde.Ui_Dialog()
        ui_Dial.setupUi(dialog)
        ui.setupUi(window, dialog, MainWindow)
        window.show()
        MainWindow.close()
#        MainWindow.hide()

    def lancerInterference(self, MainWindow):
        window = QtWidgets.QMainWindow()
        dialog = QtWidgets.QDialog()
        ui = interference_main_window.Ui_MainWindow()
        ui_Dial = dialog_interference.Ui_Dialog()
        ui_Dial.setupUi(dialog)
        ui.setupUi(window, dialog, MainWindow)
        window.show()
        MainWindow.close()
#        MainWindow.hide()

    def lancerMHS(self, MainWindow):
        window = QtWidgets.QMainWindow()
        dialog = QtWidgets.QDialog()
        ui = harmonique_main_window.Ui_MainWindow()
        ui_Dial = dialog_harmonique.Ui_Dialog()
        ui_Dial.setupUi(dialog)
        ui.setupUi(window, dialog, MainWindow)
        window.show()
        MainWindow.close()
#        MainWindow.hide()

    def lancerModes(self, MainWindow):
        window = QtWidgets.QMainWindow()
        dialog = QtWidgets.QDialog()
        ui = modes_main_window.Ui_MainWindow()
        ui_Dial = dialog_modes.Ui_Dialog()
        ui_Dial.setupUi(dialog)
        ui.setupUi(window, dialog, MainWindow)
        window.show()
        MainWindow.close()
#        MainWindow.hide()
