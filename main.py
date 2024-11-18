import qrcode

def generate_qr(data, filename):
    """
    Generates a QR code from the provided data and saves it to a file.

    :param data: The data to encode in the QR code.
    :param filename: The filename where the QR code image will be saved.
    """
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR Code (1 is 21x21)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
        box_size=8,  # Size of each box in pixels
        border=4,  # Thickness of the border
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

def main():
    """
    Main function to generate a QR code.
    """
    data = input("Enter the data for the QR code: ")
    filename = input("Enter the filename to save the QR code (e.g., qrcode.png): ")
    generate_qr(data, filename)
    print(f"QR code generated and saved as {filename}")

if __name__ == "__main__":
    main()
