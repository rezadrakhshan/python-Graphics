import pyqrcode
import png
from pyqrcode import QRCode

text = input("Enter your sample text: ")
filename = input("Enter filename: ")
make_extension = f"{filename}"+".png"
url = pyqrcode.create(text)
url.show()
url.png(make_extension,scale=2)


