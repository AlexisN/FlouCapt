#!/bin/env python2
# -*-coding:UTF-8 -*

from datetime import date, timedelta, datetime
import shutil, time
import zipfile, glob, os




class Cleaner:
        """This class allows to delete the oldest picture (after 4 days) and allows to archive the new ones"""

        def __init__(self):
            self.oldDate = time.strftime("%d")



        def run(self, floucaptFolder):
            """ Method called by the main loop
                It's determines if the date changed :
                if the date changed, then run zipper method and delete method
            """

            folderPictures = floucaptFolder + "/pictures/"

            # If the date changed
            # The cleaner started
            today = time.strftime("%d")
            if self.oldDate != today:
                self.oldDate = today
                self.zipper(folderPictures)
                self.delete(folderPictures)



        def zipper(self, folderPictures):
            """Archive pictures of the same day in the same folder"""


            # List files and directorys all in folder
            # And check it's is a folder
            for truc in os.listdir(folderPictures):
                if os.path.isdir(folderPictures + truc) :

                    # Verifying that this is an folder that concerns us (containing images)
                    try:
                        dateObj = datetime.strptime(truc, '%Y-%m-%d')
                    except:
                        continue

                    if datetime.now() - dateObj > timedelta(days=1):
                        #
                        folder = folderPictures + truc


                        # Archive the folder in a zip file
                        # after, remove the folder
                        f = zipfile.ZipFile(folderPictures + truc + ".zip",'w', zipfile.ZIP_DEFLATED)

                        for filename in glob.glob(folder+"/*"):
                            f.write(filename)
                            os.remove(filename)
                        f.close()

                        try:
                            shutil.rmtree(folder)
                        except:
                            pass



        def delete(self, folderPictures):
            """Delete the archive (.zip) which contains the old pictures. Here, it deletes the pictures which are older than 4 days"""


            # List all the files in folder that contains pictures
            for truc in os.listdir(folderPictures):

                if os.path.isfile(folderPictures + truc) :
                    try:
                        # It determines whether the file name of the file matches the format
                        # (if it is a file that interests us)
                        dateObj = datetime.strptime(truc, '%Y-%m-%d.zip')
                    except:
                        continue

                    # If the file is older than 4 days, it removes the zip file
                    if datetime.now() - dateObj > timedelta(days=4):
                        try:
                            os.remove( folderPictures + truc )
                        except:
                            pass



