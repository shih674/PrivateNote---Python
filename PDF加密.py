# *** coding:utf-8 ***
# pdf加密範本(未加密pdf→加密pdf)
# https://laplacetw.github.io/python-pdf-batch-encrypt/

import os
import glob
from PyPDF2 import PdfFileReader as pdfReader # 讀取PDF
from PyPDF2 import PdfFileWriter as pdfWriter # 寫入PDF


def find_id_by_code(code, table):
    pswd = "123456"  # default password
    for i in table:
        if code in i:
            pswd = str(i).split()[1]
            print(code, "-->", pswd)

    return pswd

# 讀取ID表
id = open("ID.txt")
ID_table = list(id)
id.close()

# 取得資料夾內所有的pdf檔之檔案路徑
pdf_files = glob.glob(r"*.pdf")
for path in pdf_files:
    # code只取檔名，作為後續的id
    code = path.replace(".pdf", "")
    # 把目標pdf改名為tmp.pdf
    os.rename(path, "tmp.pdf")
    # 讀入pdf檔案內容
    in_file = open("tmp.pdf", "r+b")
    # 建立物件pdfReader
    in_pdf = pdfReader(in_file)

    # 建立物件pdfWriter
    out_pdf = pdfWriter()
    out_pdf.appendPagesFromReader(in_pdf)
    pswd = find_id_by_code(code, ID_table)  # 找到id對應的密碼丟到pswd中
    out_pdf.encrypt(pswd)  # 對pdf加上密碼，密碼:pswd

    # 建立加密完成的pdf檔
    out_file = open(path, "wb")
    out_pdf.write(out_file)

    # 關閉寫入暫存檔，移除中繼pdf
    in_file.close()
    out_file.close()
    os.remove("tmp.pdf")

# 釋放兩個物件記憶體
del in_pdf, out_pdf
input("Encrypt Complete! Now you can close the window.")