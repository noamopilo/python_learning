import qrcode

data = input('Enter text or URL: ').strip()
fileName = input('Enter the file name (without extension): ').strip()
img = qrcode.make(data)
type(img)  # qrcode.image.pil.PilImage
img.save(f"{fileName}.png")
print(f"QR code saved as {fileName}.png")