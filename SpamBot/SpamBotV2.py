from pynput.keyboard import Key, Controller
from time import sleep

keyboard = Controller()

message = input("Type a message to repeat: ")
attempts = int(input("Number of attempts: "))
delay = float(input("Delay between messages: "))

print("""
MESSAGES WILL BE SENT IN 10 SECONDS.
OPEN AND PLACE YOUR CURSOR ON THE APPLICATION
YOU WISH TO SPAM WITH.
""")

sleep(10)

for i in range(attempts):
    keyboard.type(message)
    keyboard.press(Key.enter)
    sleep(delay)