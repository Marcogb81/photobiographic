# import modules
from aqt import mw
from aqt.qt import *
from aqt import editor
from anki import notes
from anki.importing import TextImporter
import sys
from PyQt4 import QtCore, QtGui, uic
import os
from os import listdir
from os.path import isfile, join

#class main window
# Cargar nuestro archivo .ui
form_class = uic.loadUiType("dialog.ui")[0]


# charge .ui archive
class MyWindowClass(QtGui.QMainWindow):
    def __init__(self, parent = None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.btnfolder.clicked.connect(self.btnfolder_clicked)
        self.btnimport.clicked.connect(self.btnimport_clicked)
        self.btncancel.clicked.connect(self.btncancel_clicked)
        self.lineRoot = None
        self.exec_()

    # function button folder
    def btnfolder_clicked(self):
        """Show the directory selection dialog."""
        path = unicode(QFileDialog.getExistingDirectory(mw, "Import Directory"))
        if not path:
            return
        self.lineRoot = path
        self.form.mediaDir.setText(self.mediaDir)
        self.form.mediaDir.setStyleSheet("")

    # funtion button ok
    def btnimport_clicked(self):
        # this get path, list and ordered images from directory
        path = self.lineEdit #raw_input('Introduce the path: ')
        directory = [f for f in listdir(path) if isfile(join(path, f))]  # get list from dir, empty because in dir
        directory.sort(key=lambda x: os.path.getmtime(x))  # this order by date
        images = ["<img src='{}/{}'>".format(path, elem) for elem in directory]  # give format html for flashcard
        previous_img = images[0]  # variable for array of images
        with open('output.csv', 'w') as f:
            for image in images[1:]:
                f.write(",".join([previous_img, image]) + "\n")
                previous_img = image
        file = path + 'output.csv'
        #funtion found or create deck
        did = mw.col.decks.id('Photobiographic')
        mw.col.decks.select(did)
        # set note type for deck
        m = mw.col.models.byName("Basic")
        deck = mw.col.decks.get(did)
        deck['mid'] = m['id']
        mw.col.decks.save(deck)
        # import into the collection
        ti = TextImporter(mw.col, file)
        ti.initMapping()
        ti.run()



#function call main window
# create a new menu item, "test"
action = QAction("Photobiographic", mw)
# set it to call testFunction when it's clicked
action.triggered.connect(MyWindowClass)
# and add it to the tools menu
mw.form.menuTools.addAction(action)
