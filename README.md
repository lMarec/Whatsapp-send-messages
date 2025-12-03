# WhatsApp Message Sender Script
![Top Language](https://img.shields.io/github/languages/top/lMarec/Whatsapp-send-messages)
![License](https://img.shields.io/github/license/lMarec/Whatsapp-send-messages)
![Last Commit](https://img.shields.io/github/last-commit/lMarec/Whatsapp-send-messages)

## Overview

This Python script lets you send WhatsApp messages to any of your contacts directly from your computer using your phone number. It's ideal for automating reminders, greetings, or notifications via WhatsApp.
It uses the [`pywhatkit`](https://github.com/Ankit404butfound/PyWhatKit) and [`pyautogui`](https://github.com/asweigart/pyautogui) libraries for automation.

## Features

- Send WhatsApp messages automatically
- Easy-to-use terminal interface
- Messages delivered through WhatsApp Web
- Cross-platform: Windows, macOS, Linux

## Requirements

- Python 3.x ([Download here](https://www.python.org/downloads/))
- pip (Python package manager; see instructions below if not installed)
-    [pywhatkit](https://pypi.org/project/pywhatkit/)
-    [pyautogui](https://pypi.org/project/PyAutoGUI/)
-    The modules above will automatically be installed if not already
- WhatsApp Web account (be ready to scan the QR code if you aren't logged in)

## Installing pip (if not already installed)

**Check if pip is installed:**
```bash
pip --version
```
If pip is not found, follow these steps for your operating system:

### **Windows**
Python 3 usually includes pip. If you need to install pip manually:
1. Download `get-pip.py` from https://bootstrap.pypa.io/get-pip.py.
2. Open Command Prompt and run:
   ```bash
   python get-pip.py
   ```

### **macOS**
Python 3 comes with pip, but if not:
1. Open Terminal and run:
   ```bash
   curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
   python3 get-pip.py
   ```

### **Linux**
It may be included, but if not:
- **Debian/Ubuntu:**
  ```bash
  sudo apt update
  sudo apt install python3-pip
  ```
- **Fedora:**
  ```bash
  sudo dnf install python3-pip
  ```
- Or using the direct way:
  ```bash
  curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
  python3 get-pip.py
  ```

More instructions: [Official pip installation guide](https://pip.pypa.io/en/stable/installation/)

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/lMarec/Whatsapp-send-messages.git
   cd Whatsapp-send-messages
   ```
2. **Install dependencies**
   ```bash
   pip install pywhatkit pyautogui
   ```
   If you have multiple versions of Python, you may need to use:
   ```bash
   python3 -m pip install pywhatkit pyautogui
   ```

3. **Login to WhatsApp Web**  
   Open [WhatsApp Web](https://web.whatsapp.com) in your browser and scan the QR code with your mobile app.

## Usage

1. **Run the script**
   ```bash
   python whatsapp_message.py
   ```
   If you are using macOS/Linux, you may need:
   ```bash
   python3 whatsapp_message.py
   ```

2. **Choose an option from the menu:**
   ```
   1. Send WhatsApp Message
   2. Exit
   -->
   ```
3. **Enter the recipient's international phone number (without the "+" symbol) and follow the instructions.**

> **Note:**  
> Phone number format examples:  
> - `+1 (234) 567 890` → `1234567890`  
> - `+44 7123 456789` → `447123456789`

> **Tip:**  
> It’s best to log into WhatsApp Web before running the script. If not, you will be prompted to log in.

## Troubleshooting

- **QR code not scanning:**  
  Use your phone to log into WhatsApp Web or restart the script if login fails.

- **Message not sent at scheduled time:**  
  Ensure your system clock is correct and synchronized.

- **Library errors:**  
  Double-check all dependencies are installed. Run:
  ```bash
  pip install --upgrade pywhatkit pyautogui
  ```

## Limitations and Disclaimer

- This script interacts directly with WhatsApp Web and is intended for legitimate, personal use only.
- Please respect WhatsApp’s terms of service; misuse may result in account restriction.

## Contributing

Contributions, issues, and feature requests are welcome!  
Feel free to [open an issue](https://github.com/lMarec/Whatsapp-send-messages/issues) or a pull request.

## License

This repository is licensed under the GNU Affero General Public License.  
See the [LICENSE](LICENSE) file for details.

## Credits

- [pywhatkit](https://github.com/Ankit404butfound/PyWhatKit)
- [pyautogui](https://github.com/asweigart/pyautogui)
