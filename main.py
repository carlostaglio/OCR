
from ocr import OCR

if __name__ == '__main__':
    img_name = "2.jpg"
    try:
        ocr=OCR(img_name)
        ocr.reconocerTexto()
        tarifa = ocr.tarifa()
        if tarifa:
            print("Tipo de tarifa:", tarifa)
    except AssertionError:
        print("Error al instanciar la clase OCR: No se encontró un archivo con el nombre indicado")