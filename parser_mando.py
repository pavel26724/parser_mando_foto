import requests
import openpyxl
import time
import os
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
            link = str(r.content)
            # link1 = link.lower()
            link1 = link.replace(' ', '')
            if '.jpg' in link1:
                a = link1.index('.jpg')
                b = link1.rindex('<imgsrc="', 0, a)
                c = link1[b + 9: a + 4]
                o = [x1, c]
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
print('отработала за', "%s секунд" % int(time.time() - start_time))
