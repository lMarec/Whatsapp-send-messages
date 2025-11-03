# WhatsApp Message Sender Script
## Description
A Python script uses the `pywhatkit` and `pyautogui` libraries to send WhatsApp messages. This script allows you to send messages to a specific phone number
from your WhatsApp account.
## Requirements
-Python 3.x\
-`pywhatkit` library\
-`pyautogui` library\
-`pip`\
-WhatsApp Web Authentication
## Installation
1. Clone the repository:
   ```
   git clone https://github.com/Github444444/Whatsapp-send-messages.git
   cd Whatsapp-send-messages
   ```
3. Install the required Python libraries:
   ```
   pip install pywhatkit pyautogui
   ```
5. Ensure your web browser is ready:
   - Make sure you are logged into [Whatsapp Web](web.whatsapp.com)
## Usage
1. Open a terminal inside the cloned directory and run:
   ```
   python whatsapp_message.py
   ```
2. You will be presented with two options:
   ```
   1. Send Whatsapp Message
   2. Exit
   --> 
   ```
   Select option 1 and follow the instructions to send a WhatsApp message to your desired contact
> [!NOTE]
> You will need to input your recipient's international phone number, omitting the plus ("+")\
> For example, the phone number +1 (234) 567890 would become 1234567890

> [!TIP]
> It is advised to log into WhatsApp Web before running the script.\
> If you aren't logged in, the script will direct you to log into WhatsApp Web, after which, the script will continue

## Troubleshooting
- **QR code not scanning**: If the QR code is not scanning, please use the option to log in using your phone number. If this fails, please restart the script by using:
    Ctrl + Z for Windows/Linux
    Command + Z for Mac
    and run:
    `python whatsapp_message.py`
- **Message not sending at the right time**: Please make sure your system clock is synchronised
## License
This repository is licensed under the GNU Affero General Public License - Please see the [License](LICENSE.txt) file for more details.
