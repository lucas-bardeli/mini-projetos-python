
from pyqrcode import *
from png import *
# Caso não tenha, é preciso baixar a biblioteca PyQRCode e pypng

url = input("\nCole aqui a url ou texto para o QR Code: ")

qr = pyqrcode.create(url, error="L")

qr.png('qrcode.png', scale=5, module_color=(0, 0, 0), background=(255, 255, 255))