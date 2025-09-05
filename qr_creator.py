import qrcode

info = input(f"Please enter the data = ")
img = qrcode.make(info)
type(img)  # qrcode.image.pil.PilImage
img.save("some_file.png")