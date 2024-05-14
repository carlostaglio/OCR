# OCR
Repositorio de Reconocimiento Óptico de Caracteres

## Procedimiento para ejecutar el proyecto
Se debe crear un entorno virtual con el comando:
`python -m venv .env`

Activar el entorno virtual con el comando (en bash):
`source .env/Scripts/activate`

Activar el entorno virtual con el comando (en powershell):
`.env/Scripts/activate.ps1`


instalación de requerimientos:
`pip install -r requirements.txt`

## Comando para ejecutar

`python main.py`

## Descripción de la clase OCR

La clase OCR recibe los siguientes parámetros al momento de ser instanciada: 
 - img_name (str): Nombre de la imagen sobre la cual se realizará la lectura.

 - plot (bool) (Opcional): Indica si se desea graficar la imagen. Por defecto es falso.

 - raw (bool) (Opcional): Indica si se desea utilizar la imagen sin modificar. Por defecto la imagen se modifica para aumentar su contraste y mejorar la lectura.

Los métodos públicos definidos en la clase son:
 - setImgName, que recibe como parámetro img_name (str): Nombre de la imagen sobre la cual se realizará la lectura.
    
 - togglePlot, para cambiar el valor de plot y habilitar/inhabilitar la impresión de la imagen luego de la lectura.
    
 - toggleRaw, para cambiar el valor de raw y habilitar/inhabilitar el cambio de contraste de la imagen.

 - reconocerTexto, para ejecutar la lectura de texto de la imagen y almacenarlo en un atributo interno.

 - tarifa, para retornar el valor del tipo de tarifa eléctrica en formato 'T*-R*'. Previo a utilizar este método debe ejecutarse el método reconocerTexto.
