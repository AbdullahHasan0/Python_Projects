# QR Code Generator

A simple Python script to generate QR codes for URLs using the `qrcode` library and `PIL` (Pillow).

## Features

- Customizable QR code appearance (background color and lines color).
- Easy-to-use command-line interface.
- Uses the `qrcode` library for QR code generation and `PIL` for image manipulation.

## Prerequisites

Make sure you have Python installed on your machine. You can install the required libraries using:

pip install qrcode[pil]

##Usage

Clone the repository:
git clone https://github.com/AbdullahHasan0/Python_Projects
Navigate to the project directory:
cd QR_Code_Generator

Run the script:
python QR_Code_Generator.py

##Customization
You can customize the QR code appearance by providing background color and lines color during execution. If no colors are provided, default values (white background and black lines) will be used.

Enter Background Color (default is white):
Enter Color of Lines (default is black):
Enter Output File Name (without extension):

Output
The generated QR code will be saved as a PNG file in the project directory with the specified output file name.

##Example
Paste any URL you want to convert to QR Code:
https://example.com
Enter Background Color (default is white):
Enter Color of Lines (default is black):
Enter Output File Name (without extension):output
QR Code saved successfully as output.png