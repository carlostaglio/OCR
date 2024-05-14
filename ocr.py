import cv2
import numpy as np
import matplotlib.pyplot as plt
import easyocr
import re
import os

class OCR:
    __img_name: str
    __img: np.ndarray
    __plot: bool
    __raw: bool
    __reader: easyocr.Reader
    __texto: str

    def __init__(self, img_name: str, plot = False, raw = False):
        """Crea una isntancia de Lector OCR

Parámetros:
    img_name (str): Nombre de la imagen sobre la cual se realizará la lectura.

    plot (bool): Indica si se desea graficar la imagen. Por defecto es falso.

    raw (bool): Indica si se desea utilizar la imagen sin modificar. Por defecto la imagen se modifica para aumentar su contraste y mejorar la lectura.
"""
        assert os.path.exists(img_name)
        self.__img_name = img_name
        self.__img = cv2.imread(self.__img_name, 1)
        self.__plot = plot
        self.__raw= raw
        #Instance text detector
        self.__reader = easyocr.Reader(['es'], gpu = False)
        self.__texto = ""

    def setImgName(self, img_name: str) -> None:
        """Cambia el archivo imagen a escanear"""
        assert os.path.exists(img_name)
        self.__img_name = img_name
        self.__img = cv2.imread(self.__img_name, 1)
        self.__texto = ""
    
    def togglePlot(self) -> None:
        """Cambia el valor de plot"""
        self.__plot = not self.__plot

    def toggleRaw(self) -> None:
        """Cambia el valor de raw"""
        self.__raw = not self.__raw
    
    def __aumentarContraste(self) -> np.ndarray:
        """Retorna la imagen con el contraste modificado"""
        lab= cv2.cvtColor(self.__img, cv2.COLOR_BGR2LAB)
        l_channel, a, b = cv2.split(lab)
        # Applying CLAHE to L-channel
        clahe = cv2.createCLAHE(clipLimit=0.5, tileGridSize=(1,1))
        cl = clahe.apply(l_channel)
        # Merge the CLAHE enhanced L-channel with the a and b channel
        limg = cv2.merge((cl,a,b))
        # Converting image from LAB Color model to BGR color spcae
        enhanced_img = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
        return enhanced_img
    
    def __plotImagen(self, img: np.ndarray) -> None:
        """Muestra la imagen con los cuadros de texto detectados"""
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        plt.show()

    def reconocerTexto(self) -> None:
        """Reconoce el texto completo de la imagen y lo almacena en la instancia de clase"""
        img = self.__img
        print("Reconociendo el texto de la imagen  .  .  .")
        if self.__raw:
            readerText = self.__reader.readtext(img)
        else:
            enhanced_img = self.__aumentarContraste()
            readerText = self.__reader.readtext(enhanced_img)
        texto=""
        for t in readerText:
            bbox, lectura, score = t
            if type(bbox[0][0]) == np.int32:
                if self.__plot:
                    if self.__raw:
                        cv2.rectangle(img, bbox[0], bbox[2], (0, 255, 0), 2)
                    else:
                        cv2.rectangle(enhanced_img, bbox[0], bbox[2], (0, 255, 0), 2)
                #print(lectura)
                texto += lectura
        if self.__plot:
            if self.__raw:
                self.__plotImagen(img)
            else:
                self.__plotImagen(enhanced_img)
        self.__texto = texto


    def tarifa(self) -> str | None:
        """Retorna el tipo de tarifa en formato 'T*-R*' o None en caso de error"""
        if self.__texto:
            x = re.search(r"T[1,i,I,l,L,T]-*R.", self.__texto)
            if x:
                found = x.group().replace("I","1").replace("l","1").replace("TT","T1").replace("L","1")
                found = found.replace("}","3")
                found = found.replace("T1R","T1-R")
                return found
            else:
                print("No se encontró el tipo de tarifa en la imagen")
                return None
        else:
            print("Primero debe realizarse la lectura del texto de la imagen")
            return None
