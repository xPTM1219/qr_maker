# QRMaker

This program uses `qrcode` package to create a QR image. Also, the user
has the option to either add or not a picture to be included in the QR
image. The advantage of this program is that it has a GUI using PyQt5.

I used Grok to generate the logo.

Currently, the program GUI is on Spanish, I have planned to update this
and add English as an option in future updates. All code and documentation
is on English.

## Requirements

- Python 3.10+
- pip
- Running requirements.txt `pip3 install -r requirements.txt`

## Compiling

1. Run the following to include the logo from the root directory:

   ```bash
   # In Linux
   pyinstaller qr_maker.py --noconsole --onefile --add-data "res/logo.png:res"
   
   # In Windows, the difference is the semicolon in the img path
   pyinstaller qr_maker.py --noconsole --onefile --add-data "res/logo.png;res"
   ```

2. Get the executable in `dist` folder

## Running the program

> If you already have the executable, you don't need to do the compilation step

1. Once you compiled (generated the executable above), go into the `dist`
   folder and run the file according to your OS.
   - qr_make.exe for Windows
   - qr_make for Linux
2. Generate the QR image!

## Contributing

Please see [contributing.md](docs/contributing.md) for the guidelines

## Old code or discarded methods

```python
img_1 = qr.make_image(image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer())
img_2 = qr.make_image(image_factory=StyledPilImage, color_mask=RadialGradiantColorMask())
```

## Resources

- [qrcode Python module](https://pypi.org/project/qrcode/)
- [X's Grok](https://x.com/i/grok)
