import qrcode
from PIL import ImageColor


filename = input("Enter the filename to save for the QR code image: ")
data = input("Enter the text or URL you want to encode in the QR code: ")
qr_color = input("Enter the color for the QR code (e.g., black, #0000FF for blue): ")
background_color = input("Enter the background color for the QR code (e.g., white, #FFFF00 for yellow): ")


def validate_color(color):
    try:
        ImageColor.getrgb(color)
        return color
    except ValueError:
        print(f"Invalid color '{color}', defaulting to black or white.")
        return "black" if color == qr_color else "white"


qr_color = validate_color(qr_color)
background_color = validate_color(background_color)


qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill=qr_color, back_color=background_color)
img.save(f"{filename}.png")

print(f"QR code saved as {filename}.png")
