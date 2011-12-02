# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../projects/www.fhnw.ch/src/mainwindow.ui'
#
# Created by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(410, 250)
        MainWindow.setMinimumSize(QtCore.QSize(410, 250))
        MainWindow.setMaximumSize(QtCore.QSize(410, 250))
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Zync - ZODB Syncer", None, QtGui.QApplication.UnicodeUTF8))
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 391, 211))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.button_sync = QtGui.QPushButton(self.tab)
        self.button_sync.setGeometry(QtCore.QRect(140, 110, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.button_sync.setFont(font)
        self.button_sync.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_sync.setText(QtGui.QApplication.translate("MainWindow", "Sync!", None, QtGui.QApplication.UnicodeUTF8))
        self.button_sync.setObjectName(_fromUtf8("button_sync"))
        self.target = QtGui.QLineEdit(self.tab)
        self.target.setGeometry(QtCore.QRect(80, 40, 301, 20))
        self.target.setText(QtGui.QApplication.translate("MainWindow", "", None, QtGui.QApplication.UnicodeUTF8))
        self.target.setObjectName(_fromUtf8("target"))
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 51, 16))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Zielhost:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.source = QtGui.QLineEdit(self.tab)
        self.source.setGeometry(QtCore.QRect(50, 10, 331, 20))
        self.source.setText(QtGui.QApplication.translate("MainWindow", "", None, QtGui.QApplication.UnicodeUTF8))
        self.source.setObjectName(_fromUtf8("source"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 10, 41, 16))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Quelle:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.checkBox_2 = QtGui.QCheckBox(self.tab_2)
        self.checkBox_2.setGeometry(QtCore.QRect(20, 50, 101, 17))
        self.checkBox_2.setText(QtGui.QApplication.translate("MainWindow", "Backup", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.checkBox = QtGui.QCheckBox(self.tab_2)
        self.checkBox.setGeometry(QtCore.QRect(20, 30, 111, 17))
        self.checkBox.setText(QtGui.QApplication.translate("MainWindow", "Send Mail", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.textBrowser = QtGui.QTextBrowser(self.tab_3)
        self.textBrowser.setGeometry(QtCore.QRect(5, 10, 331, 161))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Allgemein", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindow", "Aktionen", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtGui.QApplication.translate("MainWindow", "Debug", None, QtGui.QApplication.UnicodeUTF8))

