
import pyautogui as pt
from time import sleep
import pyperclip



sleep(5)


position1=pt.locateOnScreen("whatsapp_autoresponse/smile&paperclip.png",confidence=.8)
x = position1[0]
y = position1[1]


# get message 
def get_message():
    global x,y

    position=pt.locateOnScreen("whatsapp_autoresponse/smile&paperclip.png",confidence=.8)
    x = position[0]
    y = position[1]
    pt.moveTo(x,y, duration=.5)
    pt.moveTo(x+80,y-54, duration=.5)
    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(25,-150)
    sleep(2)
    pt.click()
    whatsapp_message=pyperclip.paste()
    pt.click
    print("message recived"+whatsapp_message)
    return whatsapp_message

# post my response
def post_response(message):
    position1=pt.locateOnScreen("whatsapp_autoresponse/smile&paperclip.png",confidence=.8)
    x = position1[0]
    y = position1[1]
    pt.moveTo(x+200,y+20,duration=.5)
    pt.click()
    pt.typewrite(message,interval=0.01)

    # pt.typewrite("\n",interval=0.1) UNCOMMENT IT TO SEND 


    
#  PROCESS RESPONSE
def process_response(message):
    if "?" in str(message):
        return "Ask no questions hear no lies"
    elif "morning" in str(message):
        return "Good morning!"
    elif "hello" in str(message):
        return "Hey!"
    elif "help" in str(message):
        return "please call me and let me know"
    else:
        return "Hey! i am ASUS! Priyansh is not here Please call him if its urgent or hell reply you asap"
    



# calling functions 
post_response(process_response(get_message()))