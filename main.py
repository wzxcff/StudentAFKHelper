import os
import telebot
from dotenv import load_dotenv
from telebot import types
import pyautogui
import time
import webbrowser
from pyperclip import copy

# IMPORTANT: All sensitive data and config should be stored in .env file!


# Load values from .env file
load_dotenv()

# Initialize variables from .env file
# If windows being used instead, flip this lever to False
macos = os.getenv("MACOS")
dock_hidden = os.getenv("DOCK_HIDDEN")

# Load admin ID
admin = os.getenv("USER_ID")

# Load token from to initialize bot
bot = telebot.TeleBot(os.getenv("TOKEN"))

# Button builder function to more easily build buttons
def button_builder(markup, labels):
    buttons = []
    for label in labels:
        button = types.KeyboardButton(label)
        buttons.append(button)
    markup.add(*buttons)

# Building main keyboard using button_builder
main_keyboard = types.ReplyKeyboardMarkup(row_width=2)
main_labels = ["Screenshot", "Close app", "Join Zoom", "Agree with recording message", "Send mark message", "View chat"]
button_builder(main_keyboard, main_labels)

# Button cords with original res
chat_button_cords = (678, 866)
chat_button_cords_dock = (666, 784)

# Function to scale cords
def scale_cords(cords, ref_width, ref_height, curr_width, curr_height):
    # Unpack original cords
    x, y = cords

    # Calculate scaled cords
    scaled_x = (x / ref_width) * curr_width
    scaled_y = (y / ref_height) * curr_height

    # Return new cords
    return int(scaled_x), int(scaled_y)

# Calculate cords based on dock_hidden parameter in .env
current_width, current_height = pyautogui.size()
if dock_hidden:
    scaled = scale_cords(chat_button_cords, 1440, 900, current_width, current_height)
else:
    scaled = scale_cords(chat_button_cords_dock, 1440, 900, current_width, current_height)

join_btn_cords = (840, 281)
join_btn = scale_cords(join_btn_cords, 1440, 900, current_width, current_height)

# Ask for link to join
def join_to_link(message):
    link = message.text
    bot.send_message(message.chat.id, "Send me a password to join link!\nIf meeting without password, send '-'.")
    bot.register_next_step_handler(message, join_to_link_password, link)

# Ask for password to link
def join_to_link_password(message, link):
    password = message.text
    webbrowser.open(link)
    time.sleep(3)
    pyautogui.moveTo(join_btn)
    pyautogui.click()

    if password != "-":
        time.sleep(6)
        pyautogui.write(password)
        pyautogui.press('enter')

    time.sleep(2)
    bot.send_message(message.chat.id, "View screenshot to see result.")

close_button_cords = scale_cords((1415, 94), 1440, 900, current_width, current_height)

# Message and command handler
@bot.message_handler(content_types=['text'])
def command_handler(message):
    global scaled, macos
    if str(message.from_user.id) == admin:
        if message.text == "/start":
            bot.send_message(message.chat.id, "Hello! Student AFK Helper working properly!", reply_markup=main_keyboard)
        elif message.text == "Screenshot":
            screenshot = pyautogui.screenshot()
            bot.send_photo(message.chat.id, photo=screenshot)
        elif message.text == "Close app":
            if macos:
                pyautogui.hotkey('command', 'q', interval=0.25)
            else:
                pyautogui.hotkey('ctrl', 'alt', 'f4', interval=0.25)
            time.sleep(1)
            pyautogui.press('enter')
            bot.send_message(message.chat.id, "App was closed!")
        elif message.text == "Send mark message":
            # Open chat
            pyautogui.moveTo(scaled)
            pyautogui.click()

            # Get message to send mark
            mark_message = os.getenv("MARK_MESSAGE")

            # Send message
            copy(mark_message)
            if macos:
                pyautogui.hotkey('command', 'v', interval=0.25)
            else:
                pyautogui.hotkey('ctrl', 'v', interval=0.25)
            pyautogui.press('enter')
            pyautogui.moveTo(close_button_cords)
            pyautogui.click()

            bot.send_message(message.chat.id, "Mark message was sent successfully.")
        elif message.text == "Send mark +":
            # Open chat
            pyautogui.moveTo(scaled)
            pyautogui.click()

            # Send message
            pyautogui.write("+")
            pyautogui.press('enter')
            pyautogui.click()

            bot.send_message(message.chat.id, "Mark + was sent successfully.")
        elif message.text == "Join Zoom":
            bot.send_message(message.chat.id, "Send me a zoom link to join!")
            bot.register_next_step_handler(message, join_to_link)
        elif message.text == "Agree with recording message":
            pyautogui.press('enter')
            bot.send_message(message.chat.id, "Agreed with recording message!")
        elif message.text == "View chat":
            pyautogui.moveTo(scaled)
            pyautogui.click()
            screenshot = pyautogui.screenshot()
            bot.send_photo(message.chat.id, photo=screenshot)

            pyautogui.moveTo(close_button_cords)
            pyautogui.click()

    else:
        bot.send_message(message.chat.id, "Restricted access bot.\nIf this bot being hosted by you, check user ID in .env file!")

# If hit cmnd + q twice to exit enabled, turn it off, or program wouldn't be working properly in browser

# Send message to admin when started
bot.send_message(int(admin), "This message indicates that your AFK Helper started properly!")

# Start bot
bot.polling(none_stop=True)