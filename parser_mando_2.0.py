import requests
import os
from bs4 import BeautifulSoup
import openpyxl
import time
from time import sleep

_BSDIR = os.path.dirname(os.path.abspath(__file__))

def parser_mando_foto():
    base = openpyxl.open(os.path.join(_BSDIR, 'price_ads.xlsx'))
    sheet_base = base.active
    book_rez = openpyxl.Workbook()
    sheet_rez = book_rez.active
    x = []
    for s in sheet_base.iter_rows(max_row=None):
        x.append(s[0].value)

    sheet_rez.append(['Артикул', 'Ссылка на фото'])
    o = []
    for x1 in x:
        try:
            r = requests.get(f'https://hlmandoaftermarket.com/product/{x1}')
            soup = BeautifulSoup(r.text, 'lxml')
            picture_d = soup.find('a', class_='product-image-zoom-link')

            if 'product-image-zoom-link' in soup1:
                picture_watermark = picture_d.find('img').get('src').replace(' ', '')
                o = [x1, picture_watermark]
                sheet_rez.append(o)
            else:
                o = [x1, 'no foto']
                sheet_rez.append(o)

        except TimeoutError or TypeError:
            sleep(10)

        book_rez.save(f'parser_rez.xlsx')
        book_rez.close()

start_time = time.time()
parser_mando_foto()
print(f'отработала за {int(time.time() - start_time)} секунд или {(int(time.time() - start_time)) // 60} минут')
