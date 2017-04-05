#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
This add on was initially develope like a script for generate a csv archive
to import in a previous create deck, actually this is an add on in menu of
Anki, and browse, create csv and create/import/actualized deck for improve
the episodic memory in humans by re-learn photos of past episodes of own life.

Then this become in a peg system who work like a chain of clues where you can
found a semantic hook for call and reinforce episodic memory.

The initial objective is help to people with mental/brain problems and improve
the social and emotional skills in general.

Original idea: Marco García Baturan
Developers: Marco garcía Baturan, José Carlos "Reset Reboot" Cuevas Albadalejo
Date: 2017/04/05/03
Place: Spain
Licence: Open Source, Free, GNU Licence, SLUC.
"""

# Import for Anki
from aqt import mw
from aqt.qt import *
from aqt import editor
from anki import notes
from anki.importing import TextImporter

# import for sys
import sys
import os
from os import listdir
from os.path import isfile, join

# import for Qt
from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtGui import QAction
import pbmenu
# charge archive ui


# Main class
class pbfunction(QDialog):
    def __init__(self):
        pbmenu.Ui_Dialog
        QDialog.__init__(self, mw)
        self.setupUi(self)
        self.btnBrowse.clicked.connect(self.btnBrowse_clicked)
        self.btnImport.clicked.connect(self.btnImport_clicked)
        # The path to the media directory chosen by user
        self.mediaDir = None

    # Event button btnBrowse
    def btnBrowse_clicked(self):
        """Show the directory selection dialog."""
        pathf = unicode(
            QtGui.QFileDialog.getExistingDirectory(mw, "Select Directory"))
        if not pathf:
            return
        self.mediaDir = pathf
        self.mediaDir.setText(self.mediaDir)
        self.mediaDir.setStyleSheet("")
        self.browseLine.setText(str(pathf))

    # Event button btnImport
    def btnImport_clicked(self, pathf):
        # this get path, list and ordered images from directory
        path = pathf
        directory = [f for f in listdir(path) if isfile(join(path, f))]  # get list from dir, empty because in dir
        directory.sort(key=lambda x: os.path.getmtime(x))  # this order by date
        images = ["<img src='{}/{}'>".format(path, elem) for elem in directory]  # give format html for flashcard
        previous_img = images[0]  # variable for array of images
        with open('output.csv', 'w') as f:
            for image in images[1:]:
                f.write(",".join([previous_img, image]) + "\n")
                previous_img = image
        file = path + 'output.csv'
        # funtion found or create deck
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


# function call main window
# create a new menu item, "test"
action = QAction("Photobiographic", mw)
# set it to call testFunction when it's clicked
action.triggered.connect(pbfunction)
# and add it to the tools menu
mw.form.menuTools.addAction(action)



