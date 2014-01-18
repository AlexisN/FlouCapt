#!/bin/env python2

from datetime import date, timedelta
import shutil
import zipfile

class Cleaner:


        @staticmethod
        def run():
            delete()
            zipper()


        @staticmethod
        def delete():
            """delete the folder containing the old image of four days, according to the law"""

            d = date.today() - timedelta(days=4)
            dd = d.strftime('%Y-%m-%d')
            folder = "out/"+ dd
            shutil.rmtree(folder)

        @staticmethod
        def zipper():
            """archive picture of the last days to save space"""

            d = date.today()-timedelta(days=1)
            dd = d.strftime('%Y-%m-%d')
            f = zipfile.ZipFile(dd+".zip",'w',zipfile.ZIP_DEFLATED)
            for filename in glob.glob(r"out/"+dd+"/*"):
                f.write(filename)
                os.remove(filename)
            f.close()




