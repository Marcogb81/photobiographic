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

# Import for system
import os
from os import listdir
from os.path import isfile, join
# Import for Qt
from PyQt4.QtGui import QAction, QDialog
# Import for Qt and Anki
from aqt import mw
from aqt.qt import *
from aqt import editor
from aqt.utils import showInfo
# Import for get the GUI
from pbmenu import *



# Main class
class pbfunction(QDialog, Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self, mw)
        self.setupUi(self)
        self.btnBrowse.clicked.connect(self.btnBrowse_clicked)
        self.btnImport.clicked.connect(self.btnImport_clicked)
        # The path to the media directory chosen by user
        self.browseLine
        self.pathf = None
        self.exec_()

    # Event button btnBrowse
    def btnBrowse_clicked(self, Ui_Dialog):
        """Show the directory selection dialog."""
        pathf = unicode(QtGui.QFileDialog.getExistingDirectory(mw, "Select Directory"))
        if not pathf:
            return
        self.browseLine.setText(pathf)
        self.pathf = pathf
        self.browseLine.setStyleSheet("")

    # Event button btnImport
    def btnImport_clicked(self):
        # this get path, list and ordered images from directory
        pathf = self.pathf
        directory = [f for f in listdir(pathf) if isfile(join(pathf, f))]  # get list from dir, empty because in dir
        directory.sort(key=lambda x: os.path.getmtime(os.path.join(pathf, x)))  # this order by date
        images = ["<img src='{}/{}' WIDTH=180 HEIGHT=180 >".format(pathf.encode('utf-8'), elem.encode('utf-8')) for elem in directory]  # give format html for flashcard
        previous_img = images[0]  # variable for array of images with specific format of size
        with open(os.path.join(pathf, 'output.csv'), 'w') as f:
            """Create or open a file in CSV format, where store the lines with
            reference in archive"""
            for image in images[1:]:
                f.write(",".join([previous_img, image]) + "\n") # create side 1 and 2 of card,and pass img of side 2 to side 1 of next card
                previous_img = image
        pathf2 = pathf + '/' + 'output.csv' # close and put de output file in the same folder of photos
        # function found or create deck
        did = mw.col.decks.id('Photobiographic')
        mw.col.decks.select(did)
        # set note type for deck
        m = mw.col.models.byName("Basic")
        deck = mw.col.decks.get(did)
        deck['mid'] = m['id']
        mw.col.decks.save(deck)
        # import into the collection by instructions
        showInfo("""Your deck was created. Please, proceed to reset Anki and follow the instructions :
            1. Select the deck Photobiographic.
            2. Archive > import.
            3. Select the folder of your photos.
            4. Double click in archive output.csv.
            5. Validate option 'Allow HTML in fields'.
            6. Click in Import.
            7. Enjoy your memories.""")


# function call main window
# create a new menu item, "test"
action = QAction("Photobiographic", mw)
# set it to call pbfunction when it's clicked
action.triggered.connect(pbfunction)
# and add it to the tools menu
mw.form.menuTools.addAction(action)



