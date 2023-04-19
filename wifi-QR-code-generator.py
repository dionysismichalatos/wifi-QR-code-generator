import qrcode
from PIL import Image

# Ask the user for WiFi name and password
wifi_name = input("Enter WiFi name: ")
wifi_password = input("Enter WiFi password: ")

# Generate QR code data
qr_data = f"WIFI:S:{wifi_name};T:WPA;P:{wifi_password};;"

# Create a QR code object
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Add the QR code data
qr.add_data(qr_data)
qr.make(fit=True)

# Generate the QR code image
img = qr.make_image(fill_color="black", back_color="white")

# Save the QR code image to a file
file_name = "wifi_qrcode.png"
img.save(file_name, "PNG")

print(f"QR code saved as {file_name}")
