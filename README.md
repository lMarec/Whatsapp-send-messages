# WhatsApp Message Sender Script

![Python](https://img.shields.io/badge/language-python-blue)
![License](https://img.shields.io/github/license/lMarec/Whatsapp-send-messages)
![Last Commit](https://img.shields.io/github/last-commit/lMarec/Whatsapp-send-messages)

## Overview

This Python script lets you send WhatsApp messages to any of your contacts directly from your computer using your phone number. It's ideal for automating reminders, greetings, or notifications via WhatsApp Web.  
It uses the [`pywhatkit`](https://github.com/Ankit404butfound/PyWhatKit) and [`pyautogui`](https://github.com/asweigart/pyautogui) libraries for automation.

## Features

- Send WhatsApp messages automatically
- Easy-to-use terminal interface
- Messages delivered through WhatsApp Web
- Cross-platform (Windows, MacOS, Linux)

## Requirements

- Python 3.x
- [pywhatkit](https://pypi.org/project/pywhatkit/)
- [pyautogui](https://pypi.org/project/PyAutoGUI/)
- pip
- WhatsApp Web account (be ready to scan the QR code if you aren't logged in)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/lMarec/Whatsapp-send-messages.git
   cd Whatsapp-send-messages
   ```
2. Install dependencies:
   ```bash
   pip install pywhatkit pyautogui
   ```
3. Make sure you are logged into [WhatsApp Web](https://web.whatsapp.com).

## Usage

1. Run the script:
   ```bash
   python whatsapp_message.py
   ```
2. Choose an option from the menu:
   ```
   1. Send WhatsApp Message
   2. Exit
   -->
   ```
3. Enter the recipient's international phone number (without the "+" symbol) and follow the instructions.

> **Note:**  
> Phone number format examples:  
> - `+1 (234) 567 890` → `1234567890`  
> - `+44 7123 456789` → `447123456789`

> **Tip:**  
> It’s best to log into WhatsApp Web before running the script. If not, you will be prompted to log in.

### Example Session

```bash
python whatsapp_message.py
```
_Menu appears..._

```
1. Send WhatsApp Message
2. Exit
-->
```
_Choose 1, enter target phone number and message text, follow on-screen instructions!_

_![screenshot of example run](screenshot.png)_  
*(Consider adding a real screenshot here!)*

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
