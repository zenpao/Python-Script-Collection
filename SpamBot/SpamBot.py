import time, pyautogui

def SendScript():

    time.sleep(10) #wait for 10s before it starts
    textFile = open('message.txt')
    for each_line in textFile:
        pyautogui.typewrite(each_line)
        pyautogui.press('enter')

SendScript()