#!/bin/env python2

from datetime import date, timedelta
import shutil
import zipfile

class Cleaner:
        """This class allows to delete the oldest picture and allows to archive the new ones"""

        @staticmethod
        def run():
            delete()
            zipper()


        @staticmethod
        def delete():
            """Delete the folder which contains the old pictures. Here, it deletes the pictures which are older than 4 days"""

            d = date.today() - timedelta(days=4)
            dd = d.strftime('%Y-%m-%d')
            folder = "out/"+ dd
            shutil.rmtree(folder)

        @staticmethod
        def zipper():
            """Archive pictures of the same day in the same folder"""

            d = date.today()-timedelta(days=1)
            dd = d.strftime('%Y-%m-%d')
            f = zipfile.ZipFile(dd+".zip",'w',zipfile.ZIP_DEFLATED)
            for filename in glob.glob(r"out/"+dd+"/*"):
                f.write(filename)
                os.remove(filename)
            f.close()




