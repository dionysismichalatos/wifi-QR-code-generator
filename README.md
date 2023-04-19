# WiFi QR Code Generator

This simple Python script allows you to generate a QR code containing WiFi connection details. Users can scan the QR code to connect to the specified WiFi network automatically without having to enter the network name and password manually.

## Requirements

- Python 3.6 or higher
- qrcode library
- PIL (Python Imaging Library)

## Installation

1. Install Python 3.6 or higher if you don't have it already.
2. Install the required libraries using pip:

```bash
pip install qrcode
pip install pillow

## Usage
Run the script in your terminal or command prompt:

python wifi_qrcode_generator.py
Follow the prompts to enter your WiFi name (SSID) and password.

The script will generate a QR code image and save it as "wifi_qrcode.png" in the same directory.

Share the "wifi_qrcode.png" image with users who need to connect to your WiFi network. They can scan the QR code using their phone or a QR code scanning app to connect automatically.
