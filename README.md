# qr_maker
This program creates QR images either plain QR or with a logo.

## Requirements

- Python 3.10+
- pip
- Running requirements.txt `pip3 install -r requirements.txt`

## Compiling

1. Run the following to include the logo:

   ```bash
   pyinstaller qr_maker.py --noconsole --onefile --add-data "res/logo.png:res"
   ```

2. Get the runner in dist folder

## Resources

- Grok chat Programming about running pyinstaller

