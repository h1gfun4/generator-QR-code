import qrcode 

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=16,
    border=2,
)

qr.add_data('https://pandaeyes.ru')

qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
print(type(img))

img.save('link.png')