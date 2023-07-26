import cv2
from pyzbar import pyzbar
def lire_code_barre(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    barcodes = pyzbar.decode(gray) # Détecter les codes-barres dans l'image 
    code_serie = []
    if len(barcodes) > 0:
        barcode = barcodes[0]
        serial = barcode.data.decode("utf-8")
        code_serie=serial
    elif serial in code_serie:
        serial ="ce code existe déjà"
    else:
        serial="Aucun code-barre n'a été détecté."
    return serial

image = cv2.imread('static/code.jpg')
code_serie = None
if image is not None:
    code_serie=lire_code_barre(image)
    print(code_serie)
    print("done")
else:
    print("Impossible de charger l'image")


