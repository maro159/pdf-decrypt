# -*- coding: utf-8 -*-
import os
import sys
from PyPDF2 import PdfFileReader

def process(filepath):
    if filepath.endswith(".pdf"):
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


fileDir = "./"
password = ""
recursive = False

if len(sys.argv) > 1:
    fileDir = sys.argv[1]
if len(sys.argv) > 2:
    password = sys.argv[2]
if len(sys.argv) > 3:
    if sys.argv[3] == "recursive":
        recursive = True

if (recursive):
    for r, d, f in os.walk(fileDir):
        for file in f:
            filepath = os.path.join(r, file)
            process(filepath)   
else:
    for item in os.scandir():
            if item.is_file():
                process(item.path)


