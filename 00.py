#create a qr code
import qrcode
qr=qrcode.make("https://web.whatsapp.com/")
qr.save("My_qrcode.png")
print("qrcode generated successfully")