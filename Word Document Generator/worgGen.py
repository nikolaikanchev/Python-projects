import docx             # python -m pip install python-docx --user
from docx.shared import Pt
from docx.shared import Cm, Inches
import pandas as pd
import os
from printTableInFile import printTableInFile

doc = docx.Document()

df = pd.read_csv('bank.csv',encoding="cp1251")

for index, row in df.iterrows():
    printTableInFile(row, doc)

doc.save('table.docx')
os.system("start table.docx")