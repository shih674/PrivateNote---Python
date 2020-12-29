# pdf_encrypt.py 試作版本 - 確認可用
from PyPDF2 import PdfFileWriter, PdfFileReader

def add_encryption(input_pdf, output_pdf, password):
    '''
    對單一pdf檔案加密
    :param input_pdf: 要加密的pdf的檔案路徑
    :param output_pdf: 加密完成的pdf的檔案路徑
    :param password: 加密的密碼
    :return: None
    '''
    pdf_writer = PdfFileWriter()
    # 讀取PDF內容
    pdf_reader = PdfFileReader(input_pdf)
    # 將PDF內容轉移到PdFileWriter物件中
    pdf_writer.appendPagesFromReader(pdf_reader)
    # 加密
    pdf_writer.encrypt(user_pwd=password, owner_pwd=None,
                       use_128bit=True)

    # 將pdf_writer另存新檔
    with open(output_pdf, 'wb') as fh:
        pdf_writer.write(fh)

if __name__ == '__main__':
    pdf_path = input('::請輸入完整的pdf路徑\n\t>>')
    new_pdf_path = pdf_path.replace('.pdf', '_encrypt.pdf')
    password = input('::請輸入加密用密碼\n\t>>')
    add_encryption(input_pdf=pdf_path,
                   output_pdf=new_pdf_path,
                   password=password)
    print('加密完成~~')
    print('資料路徑：', new_pdf_path)
    print('加密密碼：', password)
