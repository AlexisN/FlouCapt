#!/bin/env python2
# -*-coding:UTF-8 -*

from datetime import date, timedelta, datetime
import shutil, time
import zipfile, glob, os

class Cleaner:
        """This class allows to delete the oldest picture and allows to archive the new ones"""

        def __init__(self):
            self.oldDate = time.strftime("%d")



        def run(self, floucaptFolder):

            folderPictures = floucaptFolder + "/pictures/"

            #Si la date a changée
            today = time.strftime("%d")
            if self.oldDate != today:
                self.oldDate = today
                self.zipper(folderPictures)
                self.delete(folderPictures)



        def delete(self, folderPictures):
            """Delete the folder which contains the old pictures. Here, it deletes the pictures which are older than 4 days"""



            for truc in os.listdir(folderPictures):

                if os.path.isfile(folderPictures + truc) :
                    try:
                        dateObj = datetime.strptime(truc, '%Y-%m-%d.zip')
                    except:
                        continue

                    if datetime.now() - dateObj > timedelta(days=4):
                        try:
                            os.remove( folderPictures + truc )
                        except:
                            pass



        def zipper(self, folderPictures):
            """Archive pictures of the same day in the same folder"""


            # List folders
            for truc in os.listdir(folderPictures):
                if os.path.isdir(folderPictures + truc) :

                    #Ici, on a un dossier contenant des images
                    try:
                        dateObj = datetime.strptime(truc, '%Y-%m-%d')
                    except:
                        continue
                    if datetime.now() - dateObj > timedelta(days=1):
                        # Donc
                        folder = folderPictures + truc

                        f = zipfile.ZipFile(folderPictures + truc + ".zip",'w', zipfile.ZIP_DEFLATED)

                        for filename in glob.glob(folder+"/*"):
                            f.write(filename)
                            os.remove(filename)
                        f.close()

                        try:
                            shutil.rmtree(folder)
                        except:
                            pass

