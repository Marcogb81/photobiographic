# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pbmenu.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(477, 163)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 441, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.browseLine = QtGui.QLineEdit(Dialog)
        self.browseLine.setGeometry(QtCore.QRect(10, 60, 451, 27))
        self.browseLine.setObjectName(_fromUtf8("browseLine"))
        self.btnBrowse = QtGui.QPushButton(Dialog)
        self.btnBrowse.setGeometry(QtCore.QRect(10, 110, 151, 27))
        self.btnBrowse.setObjectName(_fromUtf8("btnBrowse"))
        self.btnImport = QtGui.QPushButton(Dialog)
        self.btnImport.setGeometry(QtCore.QRect(290, 110, 171, 27))
        self.btnImport.setObjectName(_fromUtf8("btnImport"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Photobiographic", None))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Please, select the folder where place your memories like photos.</p></body></html>", None))
        self.btnBrowse.setText(_translate("Dialog", "Found the folder", None))
        self.btnImport.setText(_translate("Dialog", "Import your memories", None))

