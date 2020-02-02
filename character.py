import cv2 as cv
import os
import glob

class My_Image:
    def __init__(self, img_name):
        self.img = cv.imread(img_name,0)
        self.__name = img_name

    def __str__(self):
        return self.__name

def charList():
    img_dir = "Image"
    data_path = os.path.join(img_dir, '*.png')
    files = glob.glob(data_path)
    data = []
    name = []
    for img in files:
        img = My_Image(img)
        name.append(str(img))
        data.append(img.img)
    return name,data


def alif():
    alif = cv.imread("Image\\alif.png", 0)
    return alif

def aeen():
    aeen = cv.imread("Image\\aeen.png", 0)
    return aeen

def aray():
    aray = cv.imread("Image\\aray.png", 0)
    return aray

def bariya():
    bariya = cv.imread("Image\\bariya.png", 0)
    return bariya

def bay():
    bay = cv.imread("Image\\bay.png", 0)
    return bay

def chay():
    chay = cv.imread("Image\\chay.png", 0)
    return chay

def chotiya():
    chotiya = cv.imread("Image\\chotiya.png", 0)
    return chotiya

def daal():
    daal = cv.imread("Image\\daal.png", 0)
    return daal

def dhaal():
    dhaal = cv.imread("Image\\dhaal.png", 0)
    return dhaal

def dzay():
    dzay = cv.imread("Image\\dzay.png", 0)
    return dzay

def fee():
    fee = cv.imread("Image\\fee.png", 0)
    return fee

def gaaf():
    gaaf = cv.imread("Image\\gaaf.png", 0)
    return gaaf

def gaeen():
    gaeen = cv.imread("Image\\gaeen.png", 0)
    return gaeen

def gol_hay():
    gol_hay = cv.imread("Image\\gol_hay.png", 0)
    return gol_hay

def hamza():
    hamza = cv.imread("Image\\hamza.png", 0)
    return hamza

def hay():
    hay = cv.imread("Image\\hay.png", 0)
    return hay

def hey():
    hey = cv.imread("Image\\hey.png", 0)
    return hey

def jeem():
    jeem = cv.imread("Image\\jeem.png", 0)
    return jeem

def kaaf():
    kaaf = cv.imread("Image\\kaaf.png", 0)
    return kaaf

def kaf():
    kaf = cv.imread("Image\\kaf.png", 0)
    return kaf

def khay():
    khay = cv.imread("Image\\khay.png", 0)
    return khay

def lam():
    lam = cv.imread("Image\\lam.png", 0)
    return lam

def mem():
    mem = cv.imread("Image\\mem.png", 0)
    return mem

def noon():
    noon = cv.imread("Image\\noon.png", 0)
    return noon

def noon_gunah():
    noon_gunah = cv.imread("Image\\noon_gunah.png", 0)
    return noon_gunah

def pay():
    pay = cv.imread("Image\\pay.png", 0)
    return pay

def ray():
    ray = cv.imread("Image\\ray.png", 0)
    return ray

def saud():
    saud = cv.imread("Image\\saud.png", 0)
    return saud

def say():
    say = cv.imread("Image\\say.png", 0)
    return say

def seen():
    seen = cv.imread("Image\\seen.png", 0)
    return alif

def sheen():
    sheen = cv.imread("Image\\sheen.png", 0)
    return sheen

def tay():
    tay = cv.imread("Image\\tay.png", 0)
    return tay

def thay():
    thay = cv.imread("Image\\thay.png", 0)
    return thay

def toa():
    toa = cv.imread("Image\\toa.png", 0)
    return toa

def wow():
    wow = cv.imread("Image\\wow.png", 0)
    return wow

def zaal():
    zaal = cv.imread("Image\\zaal.png", 0)
    return zaal

def zawad():
    zawad = cv.imread("Image\\zawad.png", 0)
    return zawad

def zay():
    zay = cv.imread("Image\\zay.png", 0)
    return zay

def zoa():
    zoa = cv.imread("Image\\zoa.png", 0)
    return zoa