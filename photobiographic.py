# Auothor: Reset Reboot
# Collaborator: Marco garcia Baturan
# Date: 2017-2-8-W
# Theme: Education
# Licence: Open Source
# import modules
import os
from os import listdir
from os.path import isfile, join
from aqt import mw
from aqt.utils import showInfo
from aqt.qt import *
from aqt import editor
from anki import notes
import dialog
from anki.importing import TextImporter

# here place the main script for create the main and unique deck
# named 'photobiographic', where we create a new deck from zero
# based in a folder plenty of randomm personal photo
# This give function in ani OS

def doPhotoBiographic():
    # Raise the main dialog for the add-on and retrieve its result when closed.
    (path) = ImportSettingsDialog().getDialogResult()
    # Get the PhotoBiographic deck id (auto-created if it doesn't exist)
    did = mw.col.decks.id('photobiographic')
    # this get path, list and ordered images from directory
    # path = raw_input('Introduce the path: ')
    directory = [f for f in listdir(path) if isfile(join(path, f))]  # get list from dir, empty because in dir
    directory.sort(key=lambda x: os.path.getmtime(x))  # this order by date
    images = ["<img src='{}/{}'>".format(path, elem) for elem in directory]  # give format html for flashcard
    previous_img = images[0]  # variable for array of images
    with open('output.csv', 'w') as f:
        for image in images[1:]:
            f.write(",".join([previous_img, image]) + "\n")
            previous_img = image

    file = path
    # select deck
    did = mw.col.decks.id("photobiographic")
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

class ImportSettingsDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self, mw)
        self.form = dialog.Ui_Dialog()
        self.form.setupUi(self)
        self.form.buttonBox.accepted(self.accept)
        self.form.buttonBox.rejected.connect(self.reject)
        # The path to the media directory chosen by user
        self.mediaDir = None
        self.exec_()

    def getDialogResult(self):
        if self.result() == QDialog.Rejected:
            return (None)


def showCompletionDialog(newCount):
    QMessageBox.about(mw, "Import Complete")

# create a new menu item, "Photobiographic"
action = QAction("Photobiographic", mw)
# set it to call Msgbox when it's clicked
action.triggered.connect(doPhotoBiographic)
# and add it to the tools menu
mw.form.menuTools.addAction(action)
