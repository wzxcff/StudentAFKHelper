# StudentAFKHelper
StudentAFKHelper is a tool, to make your student life easier. If you need to stay AFK, but also need to mark in the chat, this tool is perfect for you!

## Installation
1) Clone repo or download code.
2) Make sure you have [python](https://www.python.org/) installed.
3) Initialize a virtual environment ([venv](https://docs.python.org/uk/3/library/venv.html)).
4) Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.
5) Make sure you've allowed all necessary accesses to program to correctly work.
```bash
pip install -r requirements.txt
```
## What can program do
* **Capture a screenshot** of the screen instantly.
* **Close current opened app** (using alt f4).
* **Join Zoom**. You'll be asked for link and password for link, if needed. Then program should automatically connect to meeting.
* **Agree with recording message**. Closes "Recording in progress" message by hitting enter.
* **Send mark message**. Your specified mark message (from .env) will be sent in the chat.
* **View chat**. Gives you a screenshot of chat.

## Getting started
### Configuration
**All sensitive data should be stored in .env file! Do not hardcode token.**

**Obtain your bot token from @BotFather**

Modify the .env configuration to suit your needs.
* **TOKEN** – Put your telegram bot token in here.
* **MARK_MESSAGE** – Put here your message to mark, for example "John Doe KS-32".
* **MACOS** – Set this variable to False if you are using Windows.
* **DOCK_HIDDEN** – No need to touch if you're on Windows or if your dock on macOS stays hidden. If your dock always showed up, change this to False.
* **USER_ID** – Put here your telegram id, it will be used for security purposes only, so that only you can access your bot.

### Start script
1. Configure .env file.
2. Change to your program directory using cd.
3. Create and activate a virtual environment ([venv](https://docs.python.org/uk/3/library/venv.html)).
4. Install all requirements using 
    ```bash
   pip install -r requirements.txt
   ```
5. Start script
    
    **Linux (macOS)**
    ```bash
    python3 main.py
    ```
    **Windows**
    ```bash
    python main.py
    ```

6. Enjoy!



#### Keep in mind that the developer is not responsible for errors or misconfigurations. Use script at your own risk.