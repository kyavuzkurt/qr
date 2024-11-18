# QR Code Generator

A simple Python script to generate QR codes from text or URLs.


## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/qr-code-generator.git
   cd qr-code-generator
   ```

2. **Install Dependencies**

   The script requires the `qrcode` and `Pillow` libraries. Install them using pip:

   ```bash
   pip install qrcode[pil]
   ```

## Usage

Run the QR code generator script using Python:

```bash
python main.py
```

### Steps:

1. **Enter the Data for the QR Code**

   Input the text or URL you want to encode.

   ```
   Enter the data for the QR code: https://www.example.com
   ```

2. **Enter the Filename to Save the QR Code**

   Specify the name of the image file (e.g., `myqr.png`).

   ```
   Enter the filename to save the QR code (e.g., qrcode.png): example_qr.png
   ```

3. **Result**

   After running, the script will generate a QR code image with the provided data and save it to the specified file.

   ```
   QR code generated and saved as example_qr.png
   ```



