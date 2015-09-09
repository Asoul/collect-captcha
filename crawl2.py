# -*- coding: utf-8 -*-

import shutil
import requests
from lxml import html
from time import sleep
from random import randint
from datetime import datetime
from os import listdir
from os.path import join, isfile

counter = len([f for f in listdir('img2') if isfile(join('img', f))])

url = "http://www.tpex.org.tw/web/inc/authnum.php"

while counter < 10000:
    try:
        image = requests.get(url, stream = True)
        if image.ok:
            print datetime.now().strftime('%H:%M:%S'), counter
            f = open('img2/{}.jpg'.format(str(counter).zfill(4)), 'wb')
            shutil.copyfileobj(image.raw, f)

        counter += 1
    except Exception as e:
        print e
    finally:
        f.close()
        sleep(1 + randint(0, 2))