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

""" Initialize windows and make the main window appear """
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
import interference_main_window
import onde_stationnaire_main_window
import dialog_onde
import dialog_interference
import dialog_bienvenue
import ecran_selection


# Initialize windows
app = QApplication(sys.argv)
window_Interference = QMainWindow()
window_Onde = QMainWindow()
dialog = QDialog()
dialog_son = QDialog()
dialog_inter = QDialog()
window = QMainWindow()

ui_Interference = interference_main_window.Ui_MainWindow()
ui_Onde_Sonore_Stat = onde_stationnaire_main_window.Ui_MainWindow()
ui_Dial_Bienvenue = dialog_bienvenue.Ui_Dialog()
ui_Dial_Onde = dialog_onde.Ui_Dialog()
ui_Dial_Inter = dialog_interference.Ui_Dialog()
ui_selection = ecran_selection.Ui_MainWindow()

ui_Dial_Bienvenue.setupUi(dialog)
ui_Dial_Onde.setupUi(dialog_son)
ui_Dial_Inter.setupUi(dialog_inter)
ui_Onde_Sonore_Stat.setupUi(window_Onde, dialog_son, window)
ui_Interference.setupUi(window_Interference, dialog_inter, window)
ui_selection.setupUi(window, dialog, window_Onde, window_Interference)

# Make main window appear
window.show()
sys.exit(app.exec_())
