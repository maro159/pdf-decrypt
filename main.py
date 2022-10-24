# -*- coding: utf-8 -*-
import os
import sys
from PyPDF2 import PdfFileReader


fileDir = sys.argv[1]
if len(sys.argv) > 2:
    password = sys.argv[2]

print(fileDir)
print(password)

for r, d, f in os.walk(fileDir):
    for file in f:
        if file.endswith(".pdf"):
            filepath = os.path.join(r, file)
            pdfFile = PdfFileReader(filepath)
            if pdfFile.is_encrypted:
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
                print("[Finished]", filepath, 'File Not Encrypted')
