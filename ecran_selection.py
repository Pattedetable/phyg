#
# Copyright 2017-2018 Manuel Barrette
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

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/pattedetable/Python/Projet/Interface/ecran_selection.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, Dialog, Window_Onde, Window_Interference):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(374*2, 261*2) # (374, 261)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 3, 2, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 1, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setPixmap(QtGui.QPixmap("diffraction.png"))
        self.label.setScaledContents(True)
        self.label.setMinimumSize(1, 1)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 2, 1, 1)
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setPixmap(QtGui.QPixmap("son.png"))
        self.label2.setScaledContents(True)
        self.label2.setMinimumSize(1, 1)
        self.label2.setObjectName("label2")
        self.gridLayout.addWidget(self.label2, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 374, 25))
        self.menubar.setObjectName("menubar")
        self.menuAide = QtWidgets.QMenu(self.menubar)
        self.menuAide.setObjectName("menuAide")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_propos = QtWidgets.QAction(MainWindow)
        self.action_propos.setObjectName("action_propos")
        self.menuAide.addAction(self.action_propos)
        self.menubar.addAction(self.menuAide.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.action_propos.triggered.connect(lambda: Dialog.show())
        self.pushButton_2.clicked.connect(lambda: self.cacherEtAfficher(MainWindow, Window_Onde))
        self.pushButton.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.pushButton_3.clicked.connect(lambda: self.cacherEtAfficher(MainWindow, Window_Interference))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Physique au Cégep"))
        self.pushButton_2.setText(_translate("MainWindow", "Onde sonore stationnaire"))
        self.pushButton.setText(_translate("MainWindow", "Quitter"))
        self.pushButton_3.setText(_translate("MainWindow", "Interférence et diffraction"))
        self.menuAide.setTitle(_translate("MainWindow", "Aide"))
        self.action_propos.setText(_translate("MainWindow", "À propos"))

# import ressources_rc

    def cacherEtAfficher(self, MainWindow, window_autre):
        window_autre.show()
        MainWindow.hide()
