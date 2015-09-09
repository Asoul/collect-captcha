# -*- coding: utf-8 -*-

import shutil
import requests
from lxml import html
from time import sleep
from random import randint
from datetime import datetime
from os import listdir
from os.path import join, isfile

counter = len([f for f in listdir('img') if isfile(join('img', f))])

url = "http://bsr.twse.com.tw/bshtm"

while counter < 10000:
    try:
        req = requests.session()
        page = req.get("{}/bsMenu.aspx".format(url))
        if page.ok:
            tree = html.fromstring(page.text)
            for imgNode in tree.xpath('//img'):
                if imgNode.values()[0].startswith('Captcha'):
                    print datetime.now().strftime('%H:%M:%S'), counter, imgNode.values()[0]
                    image = req.get("{}/{}".format(url, imgNode.values()[0]), stream = True)
                    if image.ok:
                        f = open('img/{}.jpg'.format(str(counter).zfill(4)), 'wb')
                        shutil.copyfileobj(image.raw, f)

        counter += 1
    except Exception as e:
        print e
    finally:
        f.close()
        sleep(1 + randint(0, 2))