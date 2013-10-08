# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'W:\COM\gene\ple\projectVFX\timelog\UI_timelog\mainWindow.ui'
#
# Created: Wed Apr 24 00:57:00 2013
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindowTimelog(object):
    def setupUi(self, MainWindowTimelog):
        MainWindowTimelog.setObjectName(_fromUtf8("MainWindowTimelog"))
        MainWindowTimelog.resize(537, 393)
        self.centralwidget = QtGui.QWidget(MainWindowTimelog)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        MainWindowTimelog.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindowTimelog)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 537, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuTimeLog = QtGui.QMenu(self.menubar)
        self.menuTimeLog.setObjectName(_fromUtf8("menuTimeLog"))
        MainWindowTimelog.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindowTimelog)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindowTimelog.setStatusBar(self.statusbar)
        self.toolBar_3 = QtGui.QToolBar(MainWindowTimelog)
        self.toolBar_3.setObjectName(_fromUtf8("toolBar_3"))
        MainWindowTimelog.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_3)
        MainWindowTimelog.insertToolBarBreak(self.toolBar_3)
        self.toolBar_2 = QtGui.QToolBar(MainWindowTimelog)
        self.toolBar_2.setObjectName(_fromUtf8("toolBar_2"))
        MainWindowTimelog.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_2)
        MainWindowTimelog.insertToolBarBreak(self.toolBar_2)
        self.actionAbout = QtGui.QAction(MainWindowTimelog)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionLogToday = QtGui.QAction(MainWindowTimelog)
        self.actionLogToday.setObjectName(_fromUtf8("actionLogToday"))
        self.actionLogYesterday = QtGui.QAction(MainWindowTimelog)
        self.actionLogYesterday.setObjectName(_fromUtf8("actionLogYesterday"))
        self.actionGotoToday = QtGui.QAction(MainWindowTimelog)
        self.actionGotoToday.setObjectName(_fromUtf8("actionGotoToday"))
        self.menuTimeLog.addAction(self.actionAbout)
        self.menuTimeLog.addSeparator()
        self.menubar.addAction(self.menuTimeLog.menuAction())
        self.toolBar_3.addAction(self.actionLogToday)
        self.toolBar_3.addAction(self.actionLogYesterday)
        self.toolBar_2.addAction(self.actionGotoToday)

        self.retranslateUi(MainWindowTimelog)
        QtCore.QMetaObject.connectSlotsByName(MainWindowTimelog)

    def retranslateUi(self, MainWindowTimelog):
        MainWindowTimelog.setWindowTitle(QtGui.QApplication.translate("MainWindowTimelog", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.menuTimeLog.setTitle(QtGui.QApplication.translate("MainWindowTimelog", "TimeLog", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar_3.setWindowTitle(QtGui.QApplication.translate("MainWindowTimelog", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar_2.setWindowTitle(QtGui.QApplication.translate("MainWindowTimelog", "toolBar_2", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindowTimelog", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLogToday.setText(QtGui.QApplication.translate("MainWindowTimelog", "logToday", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLogYesterday.setText(QtGui.QApplication.translate("MainWindowTimelog", "logYesterday", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLogYesterday.setToolTip(QtGui.QApplication.translate("MainWindowTimelog", "logYesterday", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGotoToday.setText(QtGui.QApplication.translate("MainWindowTimelog", "gotoToday", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGotoToday.setToolTip(QtGui.QApplication.translate("MainWindowTimelog", "gotoToday", None, QtGui.QApplication.UnicodeUTF8))

