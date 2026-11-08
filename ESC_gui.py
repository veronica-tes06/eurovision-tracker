# -*- coding: utf-8 -*-
import os

# Eurovision 2025 Tracker - main window.
# The layout was first generated with Qt Designer / pyuic5 (PyQt5 5.15.11)
# and the application logic was then added by hand.

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow

from ESC_country import Country, RatedCountry, CountryInputError

# Resolve data files relative to this script, so the app works no matter which folder it is launched from.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
COUNTRY_FILE = os.path.join(BASE_DIR, "countryFile.txt")
SCOREBOARD_FILE = os.path.join(BASE_DIR, "scoreBoard.txt")
IMAGES_DIR = os.path.join(BASE_DIR, "images")

class ScoreBoardError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def scoreBoard():
    if len(ratedCountrylist) < 10:
        raise ScoreBoardError("Use all Points!")

    ratedCountrylist.sort(key=lambda x: x.getPoints(), reverse=True)
    separator = "=" * 62

    with open(SCOREBOARD_FILE, "w", encoding="utf-8") as outfile:
        print(separator, file=outfile)
        print(f"| {'My Eurovision Scoreboard':<58} |", file=outfile)
        print(separator, file=outfile)
        print(f"| {'Points':<6} | {'Country':<20} | {'Contestant':<26} |", file=outfile)
        print(separator, file=outfile)

        for el in ratedCountrylist:
            print(f"| {el.getPoints():<6} | {el.getName():<20} | {el.getContestant():<26} |", file=outfile)

        print(separator, file=outfile)


def archiveCmd():
    with open(COUNTRY_FILE, "w", encoding="utf-8") as outfile:
        for el in countrylist:
            fields = [
                el.getName(),
                el.getContestant(),
                str(el.getWins()),
                el.getPlacement(),
                str(el.getParticipations()),
                str(el.getQualifications()),
                str(el.getAutomaticQualification()),
                str(el.getSemifinal()),
            ]
            print(":".join(fields) + ":", file=outfile)
    print("Archived!")

def addCountriesFromFile(countrylist):

    with open(COUNTRY_FILE, "r", encoding="utf-8") as infile:
        for line in infile:
            line = line.rstrip()
            if not line:
                continue
            fields = line.split(':')
            name = fields[0]
            contestant = fields[1]
            wins = int(fields[2])
            placement = fields[3]
            parts = int(fields[4])
            quals = int(fields[5])
            autoqual = fields[6] == 'True'
            semifinal = int(fields[7])
            new_country = Country(name, contestant, wins, placement, parts, quals, autoqual, semifinal)
            countrylist.append(new_country)

countrylist = []
ratedCountrylist = []
addCountriesFromFile(countrylist)

global current
current = 0
global country
country = countrylist[0]
global ratedCountry

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(601, 610)
        # Explicit colours for every kind of widget, so the text stays readable
        # even when the computer is in dark mode.
        MainWindow.setStyleSheet(
            "QMainWindow, QWidget#centralwidget { background-color: lightyellow; }\n"
            "QLabel, QCheckBox, QRadioButton { color: black; background: transparent; }\n"
            "QLabel#label { color: rgb(0, 85, 0); }\n"
            "QLineEdit { color: black; background-color: white;"
            " border: 1px solid #999; border-radius: 3px; }\n"
            "QLineEdit#lineEditPoints, QLineEdit#lineEditException { color: red; }\n"
            "QComboBox QAbstractItemView { color: black; background-color: white;"
            " selection-background-color: purple; selection-color: white; }\n"
        )
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 551, 61))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 140, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEditName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditName.setGeometry(QtCore.QRect(220, 140, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(14)
        self.lineEditName.setFont(font)
        self.lineEditName.setText("")
        self.lineEditName.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEditName.setObjectName("lineEditName")
        self.checkBox1 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox1.setGeometry(QtCore.QRect(200, 170, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.checkBox1.setFont(font)
        self.checkBox1.setObjectName("checkBox1")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 90, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 160, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(113, 290, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(103, 244, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(70, 210, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEditCountry = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditCountry.setGeometry(QtCore.QRect(220, 90, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(18)
        self.lineEditCountry.setFont(font)
        self.lineEditCountry.setStyleSheet("")
        self.lineEditCountry.setText("")
        self.lineEditCountry.setObjectName("lineEditCountry")
        self.lineEditWin = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditWin.setGeometry(QtCore.QRect(130, 170, 41, 35))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(22)
        self.lineEditWin.setFont(font)
        self.lineEditWin.setText("")
        self.lineEditWin.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditWin.setObjectName("lineEditWin")
        self.lineEditPlace = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditPlace.setGeometry(QtCore.QRect(320, 290, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(18)
        self.lineEditPlace.setFont(font)
        self.lineEditPlace.setText("")
        self.lineEditPlace.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditPlace.setObjectName("lineEditPlace")
        self.lineEditPart = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditPart.setGeometry(QtCore.QRect(320, 250, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(18)
        self.lineEditPart.setFont(font)
        self.lineEditPart.setText("")
        self.lineEditPart.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditPart.setObjectName("lineEditPart")
        self.lineEditQual = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditQual.setGeometry(QtCore.QRect(320, 210, 41, 35))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(20)
        self.lineEditQual.setFont(font)
        self.lineEditQual.setText("")
        self.lineEditQual.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditQual.setObjectName("lineEditQual")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(170, 340, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("QComboBox {\n"
"    background-color: lightgrey;\n"
"    color: black;  \n"
"    border-radius: 5px; \n"
"}")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setItemText(10, "")
        self.btn_win = QtWidgets.QPushButton(self.centralwidget)
        self.btn_win.setGeometry(QtCore.QRect(30, 400, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_win.setFont(font)
        self.btn_win.setStyleSheet("QPushButton {\n"
"    background-color: purple;\n"
"    color: white; \n"
"    border-radius: 5px;\n"
"}")
        self.btn_win.setObjectName("btn_win")
        self.btn_qual = QtWidgets.QPushButton(self.centralwidget)
        self.btn_qual.setGeometry(QtCore.QRect(150, 400, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_qual.setFont(font)
        self.btn_qual.setStyleSheet("QPushButton {\n"
"    background-color: purple;\n"
"    color: white;  \n"
"    border-radius: 5px; \n"
"}")
        self.btn_qual.setObjectName("btn_qual")
        self.btn_setPoints = QtWidgets.QPushButton(self.centralwidget)
        self.btn_setPoints.setGeometry(QtCore.QRect(30, 340, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_setPoints.setFont(font)
        self.btn_setPoints.setStyleSheet("QPushButton {\n"
"    background-color: green;\n"
"    color: white; \n"
"    border-radius: 5px; \n"
"}")
        self.btn_setPoints.setObjectName("btn_setPoints")
        self.btn_percent = QtWidgets.QPushButton(self.centralwidget)
        self.btn_percent.setGeometry(QtCore.QRect(360, 400, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_percent.setFont(font)
        self.btn_percent.setStyleSheet("QPushButton {\n"
"    background-color: purple;\n"
"    color: white; \n"
"    border-radius: 5px; \n"
"}")
        self.btn_percent.setObjectName("btn_percent")
        self.lineEditPercent = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditPercent.setGeometry(QtCore.QRect(480, 400, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(22)
        self.lineEditPercent.setFont(font)
        self.lineEditPercent.setText("")
        self.lineEditPercent.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditPercent.setObjectName("lineEditPercent")
        self.btn_first = QtWidgets.QPushButton(self.centralwidget)
        self.btn_first.setGeometry(QtCore.QRect(180, 500, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_first.setFont(font)
        self.btn_first.setStyleSheet("QPushButton {\n"
"    background-color: lightgrey;\n"
"    color: black;  /* Change text color */\n"
"    border-radius: 5px; \n"
"}")
        self.btn_first.setObjectName("btn_first")
        self.btn_last = QtWidgets.QPushButton(self.centralwidget)
        self.btn_last.setGeometry(QtCore.QRect(290, 500, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_last.setFont(font)
        self.btn_last.setStyleSheet("QPushButton {\n"
"    background-color: lightgrey;\n"
"    color: black; \n"
"    border-radius: 5px; \n"
"}")
        self.btn_last.setObjectName("btn_last")
        self.btn_next = QtWidgets.QPushButton(self.centralwidget)
        self.btn_next.setGeometry(QtCore.QRect(290, 460, 91, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(211, 211, 211))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(211, 211, 211))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(211, 211, 211))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(211, 211, 211))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(211, 211, 211))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(211, 211, 211))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(211, 211, 211))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(211, 211, 211))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(211, 211, 211))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        self.btn_next.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_next.setFont(font)
        self.btn_next.setStyleSheet("QPushButton {\n"
"    background-color: lightgrey;\n"
"    color: black;  \n"
"    border-radius: 5px; \n"
"}")
        self.btn_next.setObjectName("btn_next")
        self.btn_prev = QtWidgets.QPushButton(self.centralwidget)
        self.btn_prev.setGeometry(QtCore.QRect(180, 460, 91, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(211, 211, 211))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(112, 189, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(54, 227, 112))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(77, 35, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 58, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(211, 211, 211))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(211, 211, 211))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(211, 211, 211))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(112, 189, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(54, 227, 112))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(77, 35, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 58, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(211, 211, 211))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(211, 211, 211))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(211, 211, 211))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(112, 189, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(54, 227, 112))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(77, 35, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 58, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(211, 211, 211))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(211, 211, 211))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.btn_prev.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_prev.setFont(font)
        self.btn_prev.setToolTipDuration(4)
        self.btn_prev.setStyleSheet("QPushButton {\n"
"    background-color: lightgrey;\n"
"    color: black;  /* Change text color */\n"
"    border-radius: 5px; \n"
"}")
        self.btn_prev.setObjectName("btn_prev")
        self.btn_archive = QtWidgets.QPushButton(self.centralwidget)
        self.btn_archive.setGeometry(QtCore.QRect(170, 550, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_archive.setFont(font)
        self.btn_archive.setStyleSheet("QPushButton {\n"
"    background-color: orange;\n"
"    color: white; \n"
"    border-radius: 5px;\n"
"}")
        self.btn_archive.setObjectName("btn_archive")
        self.btn_score = QtWidgets.QPushButton(self.centralwidget)
        self.btn_score.setGeometry(QtCore.QRect(280, 550, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_score.setFont(font)
        self.btn_score.setStyleSheet("QPushButton {\n"
"    background-color: orange;\n"
"    color: white;  \n"
"    border-radius: 5px; \n"
"}")
        self.btn_score.setObjectName("btn_score")
        self.btn_resetPoints = QtWidgets.QPushButton(self.centralwidget)
        self.btn_resetPoints.setGeometry(QtCore.QRect(240, 340, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_resetPoints.setFont(font)
        self.btn_resetPoints.setStyleSheet("QPushButton {\n"
"    background-color: red;\n"
"    color: white; \n"
"    border-radius: 5px; \n"
"}")
        self.btn_resetPoints.setObjectName("btn_resetPoints")
        self.lineEditPoints = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditPoints.setGeometry(QtCore.QRect(420, 130, 111, 81))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.lineEditPoints.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(48)
        self.lineEditPoints.setFont(font)
        self.lineEditPoints.setText("")
        self.lineEditPoints.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditPoints.setObjectName("lineEditPoints")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(420, 90, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.btn_quit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_quit.setGeometry(QtCore.QRect(450, 550, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_quit.setFont(font)
        self.btn_quit.setStyleSheet("QPushButton {\n"
"    background-color: lightgrey;\n"
"    color: black;  \n"
"    border-radius: 5px; \n"
"}")
        self.btn_quit.setObjectName("btn_quit")
        self.radioButton1 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton1.setGeometry(QtCore.QRect(430, 460, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(14)
        self.radioButton1.setFont(font)
        self.radioButton1.setObjectName("radioButton1")
        self.radioButton2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton2.setGeometry(QtCore.QRect(430, 490, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(14)
        self.radioButton2.setFont(font)
        self.radioButton2.setObjectName("radioButton2")
        self.imageLabel = QtWidgets.QLabel(self.centralwidget)
        self.imageLabel.setGeometry(QtCore.QRect(410, 230, 161, 151))
        self.imageLabel.setText("")
        self.imageLabel.setObjectName("imageLabel")
        self.lineEditException = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditException.setGeometry(QtCore.QRect(10, 461, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(16)
        self.lineEditException.setFont(font)
        self.lineEditException.setText("")
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.lineEditException.setPalette(palette)
        self.lineEditException.setObjectName("lineEditException")
        self.btn_add = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add.setGeometry(QtCore.QRect(30, 510, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btn_add.setFont(font)
        self.btn_add.setStyleSheet("QPushButton {\n"
"    background-color: purple;\n"
"    color: white; \n"
"    border-radius: 5px;\n"
"}")
        self.btn_add.setObjectName("btn_add")
        self.btn_resetData = QtWidgets.QPushButton(self.centralwidget)
        self.btn_resetData.setGeometry(QtCore.QRect(30, 550, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btn_resetData.setFont(font)
        self.btn_resetData.setStyleSheet("QPushButton {\n"
"    background-color: purple;\n"
"    color: white; \n"
"    border-radius: 5px;\n"
"}")
        self.btn_resetData.setObjectName("btn_resetData")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.btn_add.pressed.connect(self.addCountryEvent)  # type: ignore
        self.btn_resetData.pressed.connect(self.resetData)  # type: ignore
        self.btn_archive.pressed.connect(archiveCmd)  # type: ignore
        self.btn_first.pressed.connect(self.firstCmd)  # type: ignore
        self.btn_last.pressed.connect(self.lastCmd)  # type: ignore
        self.btn_next.pressed.connect(self.nextCmd)  # type: ignore
        self.btn_percent.pressed.connect(self.percentQuals)  # type: ignore
        self.btn_prev.pressed.connect(self.prevCmd)  # type: ignore
        self.btn_qual.pressed.connect(self.incrementQuals)  # type: ignore
        self.btn_resetPoints.pressed.connect(self.resetMyPoints)  # type: ignore
        self.btn_score.pressed.connect(self.scoreBoardEvent)  # type: ignore
        self.btn_setPoints.pressed.connect(self.setMyPoints)  # type: ignore
        self.btn_win.pressed.connect(self.incrementWins)  # type: ignore
        self.btn_quit.pressed.connect(self.quitCmd)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.display(current)

    def display(self, index):
            global current
            global country
            country = countrylist[index]
            current = index
            self.lineEditCountry.setText(str(country.getName()))
            self.lineEditName.setText(str(country.getContestant()))
            self.lineEditWin.setText(str(country.getWins()))
            self.lineEditPlace.setText(str(country.getPlacement()))
            self.lineEditPart.setText(str(country.getParticipations()))
            self.lineEditQual.setText(str(country.getQualifications()))
            self.checkBox1.setChecked(country.getAutomaticQualification())
            self.lineEditPercent.setText("")
            semifinal = country.getSemifinal()
            if semifinal == 1:
                    self.radioButton1.setChecked(True)
                    self.radioButton2.setChecked(False)
            elif semifinal == 2:
                    self.radioButton2.setChecked(True)
                    self.radioButton1.setChecked(False)
            else:
                    self.radioButton1.setAutoExclusive(False)
                    self.radioButton2.setAutoExclusive(False)

                    self.radioButton1.setChecked(False)
                    self.radioButton2.setChecked(False)

                    self.radioButton1.setAutoExclusive(True)
                    self.radioButton2.setAutoExclusive(True)

            found = False
            for el in ratedCountrylist:
                    if el.getName() == country.getName():
                            self.lineEditPoints.setText(str(el.getPoints()))
                            found = True
                            break

            if not found:
                    self.lineEditPoints.setText("")

            image_path = os.path.join(IMAGES_DIR, f"{country.getName()}.png")
            if os.path.exists(image_path):
                    pixmap = QPixmap(image_path)
                    self.imageLabel.setPixmap(pixmap)
                    self.imageLabel.setScaledContents(True)
            else:
                    self.imageLabel.clear()

    def quitCmd(self):
            QApplication.quit()

    def nextCmd(self):
            global current
            if (current < (len(countrylist) - 1)):
                    current += 1
                    self.display(current)

    def prevCmd(self):
            global current
            if (current > 0):
                    current -= 1
                    self.display(current)

    def firstCmd(self):
            self.display(0)

    def lastCmd(self):
            self.display(len(countrylist) - 1)

    def incrementWins(self):
            country.addWin()
            self.display(current)

    def incrementQuals(self):
            country.addQual()
            self.display(current)

    def percentQuals(self):
            result = country.getPercentQuals()
            self.lineEditPercent.setText(str(result) + "%")

    def setMyPoints(self):

            # Store points as a number so the scoreboard sorts 12, 10, 8 ... 1
            points = int(self.comboBox.currentText())
            name = self.lineEditCountry.text()
            contestant = self.lineEditName.text()

            # Only countries already in the list can be voted for
            if name not in [c.getName() for c in countrylist]:
                    self.showErrorMessage("Pick a country!")
                    return
            self.showErrorMessage("")

            # Each score can only be given once, so take it back from any
            # other country that already has it.
            ratedCountrylist[:] = [el for el in ratedCountrylist
                                   if el.getPoints() != points or el.getName() == name]

            found = False
            for el in ratedCountrylist:
                    if el.getName() == name:
                            el.setPoints(points)
                            found = True
                            break

            if not found:
                    new_country = RatedCountry(name, contestant, points)
                    ratedCountrylist.append(new_country)

            self.display(current)

    def resetMyPoints(self):
            global ratedCountrylist
            ratedCountrylist.clear()
            self.display(current)

    def addCountry(self):
            global countrylist

            name = self.lineEditCountry.text()
            contestant = self.lineEditName.text()
            wins = self.lineEditWin.text()
            placement = self.lineEditPlace.text()
            parts = self.lineEditPart.text()
            quals = self.lineEditQual.text()
            autoqual = self.checkBox1.isChecked()
            semifinal = 0
            if self.radioButton1.isChecked():
                    semifinal = 1
            elif self.radioButton2.isChecked():
                    semifinal = 2

            # Validate the input and raise CountryInputError if anything is missing or not a number
            name = name.strip()
            contestant = contestant.strip()
            if not name or not contestant:
                    raise CountryInputError("Invalid Input!")

            # Each country can only be in the contest once (ignores capitals)
            if name.lower() in [c.getName().lower() for c in countrylist]:
                    raise CountryInputError("Already added!")

            try:
                    wins = int(wins)
                    parts = int(parts)
                    quals = int(quals)
            except ValueError:
                    raise CountryInputError("Invalid Input!")

            new_country = Country(name, contestant, wins, placement, parts, quals, autoqual, semifinal)
            countrylist.append(new_country)


    def addCountryEvent(self):
            try:
                    self.addCountry()
                    self.showErrorMessage("")
                    self.display(len(countrylist) - 1)  # jump to the new country
            except CountryInputError as e:
                    self.showErrorMessage(str(e))

    def showErrorMessage(self, message):
            self.lineEditException.setText(message)

    def scoreBoardEvent(self):
            try:
                    scoreBoard()
                    self.showErrorMessage("")
                    print("Score Board ready to share!")
            except ScoreBoardError as e:
                    self.showErrorMessage(str(e))

    def resetData(self):
        self.lineEditCountry.setText("")
        self.lineEditName.setText("")
        self.lineEditWin.setText("")
        self.lineEditPlace.setText("")
        self.lineEditPart.setText("")
        self.lineEditQual.setText("")
        self.checkBox1.setChecked(False)
        self.lineEditPercent.setText("")
        self.lineEditPoints.setText("")
        self.lineEditException.setText("")
        self.imageLabel.clear()

        self.radioButton1.setAutoExclusive(False)
        self.radioButton2.setAutoExclusive(False)
        self.radioButton1.setChecked(False)
        self.radioButton2.setChecked(False)
        self.radioButton1.setAutoExclusive(True)
        self.radioButton2.setAutoExclusive(True)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Eurovision 2025 Tracker"))
        self.label.setText(_translate("MainWindow", "Eurovision Song Contest"))
        self.label_2.setText(_translate("MainWindow", "2025 Contestant"))
        self.checkBox1.setText(_translate("MainWindow", "Automatic Qualification"))
        self.label_3.setText(_translate("MainWindow", "Country"))
        self.label_4.setText(_translate("MainWindow", "Wins"))
        self.label_5.setText(_translate("MainWindow", "Highest Placement"))
        self.label_6.setText(_translate("MainWindow", "No. of Participations"))
        self.label_7.setText(_translate("MainWindow", "No. of Qualifications"))
        self.comboBox.setItemText(0, _translate("MainWindow", "12"))
        self.comboBox.setItemText(1, _translate("MainWindow", "10"))
        self.comboBox.setItemText(2, _translate("MainWindow", "8"))
        self.comboBox.setItemText(3, _translate("MainWindow", "7"))
        self.comboBox.setItemText(4, _translate("MainWindow", "6"))
        self.comboBox.setItemText(5, _translate("MainWindow", "5"))
        self.comboBox.setItemText(6, _translate("MainWindow", "4"))
        self.comboBox.setItemText(7, _translate("MainWindow", "3"))
        self.comboBox.setItemText(8, _translate("MainWindow", "2"))
        self.comboBox.setItemText(9, _translate("MainWindow", "1"))
        self.btn_win.setText(_translate("MainWindow", "Record Win"))
        self.btn_qual.setText(_translate("MainWindow", "Record Qualification"))
        self.btn_setPoints.setText(_translate("MainWindow", "Set My Points"))
        self.btn_percent.setText(_translate("MainWindow", "% Qualified"))
        self.btn_first.setText(_translate("MainWindow", "First "))
        self.btn_last.setText(_translate("MainWindow", "Last"))
        self.btn_next.setText(_translate("MainWindow", "Next"))
        self.btn_prev.setText(_translate("MainWindow", "Prev"))
        self.btn_archive.setText(_translate("MainWindow", "Archive"))
        self.btn_score.setText(_translate("MainWindow", "My ScoreBoard"))
        self.btn_resetPoints.setText(_translate("MainWindow", "Reset My Points"))
        self.label_8.setText(_translate("MainWindow", "My Points"))
        self.btn_quit.setText(_translate("MainWindow", "Quit"))
        self.radioButton1.setText(_translate("MainWindow", "Semi Final 1"))
        self.radioButton2.setText(_translate("MainWindow", "Semi Final 2"))
        self.btn_add.setText(_translate("MainWindow", "Add Country"))
        self.btn_resetData.setText(_translate("MainWindow", "Clear Form"))

def applyLightTheme(app):
    """Always use a light theme, so text stays dark and readable even when
    the computer is in dark mode."""
    app.setStyle("Fusion")
    palette = QtGui.QPalette()
    black = QtGui.QColor(0, 0, 0)
    white = QtGui.QColor(255, 255, 255)
    palette.setColor(QtGui.QPalette.Window, QtGui.QColor(255, 255, 224))
    palette.setColor(QtGui.QPalette.WindowText, black)
    palette.setColor(QtGui.QPalette.Base, white)
    palette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(240, 240, 240))
    palette.setColor(QtGui.QPalette.Text, black)
    palette.setColor(QtGui.QPalette.Button, QtGui.QColor(211, 211, 211))
    palette.setColor(QtGui.QPalette.ButtonText, black)
    palette.setColor(QtGui.QPalette.ToolTipBase, white)
    palette.setColor(QtGui.QPalette.ToolTipText, black)
    palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(128, 0, 128))
    palette.setColor(QtGui.QPalette.HighlightedText, white)
    app.setPalette(palette)


if __name__ == "__main__":
    app = QApplication([])
    applyLightTheme(app)
    w = QMainWindow()
    ex = Ui_MainWindow()
    ex.setupUi(w)
    w.resize(601, 610)
    w.show()
    app.exec_()

