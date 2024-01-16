import qrcode
from PIL import Image

def generate_qr_code(input_data, output_file, background_color="white", lines_color="black"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )

    qr.add_data(input_data)
    qr.make(fit=True)

    img = qr.make_image(fill_color=background_color, back_color=lines_color)

    img.save(f"{output_file}.png")

if __name__ == "__main__":
    try:
        input_data = input("Paste any URL you want to convert to QR Code:\n")
        background_color = input("Enter Background Color (default is white): ") or "white"
        lines_color = input("Enter Color of Lines (default is black): ") or "black"
        output_file = input("Enter Output File Name (without extension): ") or "output"

        generate_qr_code(input_data, output_file, background_color, lines_color)
        print(f"QR Code saved successfully as {output_file}.png")

    except Exception as e:
        print(f"An error occurred: {e}")
