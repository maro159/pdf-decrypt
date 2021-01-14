# -*- coding: utf-8 -*-
import os
from PyPDF2 import PdfFileReader

# TODO: set where your pdf file in
fileDir = ""
# TODO: set password of your password
password = ""

for r, d, f in os.walk(fileDir):
    for file in f:
        if file.endswith(".pdf"):
            filepath = os.path.join(r, file)
            pdfFile = PdfFileReader(filepath)
            if pdfFile.isEncrypted:
                print("[Processing]", filepath)
                cmd = "copy \"" + filepath + "\" temp.pdf >nul"
                print(cmd)
                os.system(cmd)
                cmd = "qpdf --password=" + password + " --decrypt temp.pdf \"" + filepath + "\""
                print(cmd)
                os.system(cmd)
                cmd = "del temp.pdf /s /q"
                print(cmd)
                os.system(cmd)
                print("[Finished]", filepath, 'File Decrypted (qpdf)')
            else:
                pass
                # print("[Finished]", filepath, 'File Not Encrypted')
