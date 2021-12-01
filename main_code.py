
import pyautogui as pt
from time import sleep
import pyperclip



sleep(5)#as we need to time to switch to whatsapp tab after clicking run


# position1=pt.locateOnScreen("whatsapp_autoresponse/smile&paperclip.png",confidence=.8)
# x = position1[0]
# y = position1[1]


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

    pt.typewrite("\n",interval=0.1) 


    
#  PROCESS RESPONSE
def process_response(message):
    if "?" in str.lower(message):
        return "Ask no questions hear no lies"
    elif "morning" in str.lower(message):
        return "Good morning!"
    elif "mhm" in str.lower(message):
        return "You seem bored! type:songs or poems"
    elif "hello" in str.lower(message):
        return "Hey!"
    elif str.lower(message)=="poem":
        return "well you idiot you are talking to a chatbot i hope you understand the word CHATBOT!"
    elif str.lower(message)=="song":
        return "well you idiot you are talking to a chatbot i hope you understand the word CHATBOT!"
    elif "help" in str.lower(message):
        return "please call me and let me know"
    elif "fuck" in str.lower(message):
        return "i hope someday you devlop Self-cannibalistic traits and eat yourself to death!"
    else:
        return "mhmm👀! i am a chatbot so, i can't get you and Priyansh is not here, Please call him if its urgent or he will reply you asap! if you are bored type 'song' or 'poem'"
    

#  CHECKING FOR NEW MESSAGES
def check_for_new_text():
        
    while True:#continuesly checks for new message 
        try:
             posi_of_greenmark=pt.locateOnScreen("whatsapp_autoresponse/green_dot.png", confidence=.8)#identifies new message tags 
             if posi_of_greenmark is not None:   
                    pt.moveTo(posi_of_greenmark,duration=0.5)
                    pt.moveRel(-100,0)
                    pt.click()#this helps you to open the new message
                    post_response(process_response(get_message()))#these are the function to get message-process it and post the response
                    pt.moveTo(506,395,duration=0.25)
                    pt.click()
                    sleep(6)#you can call this refresh rate adjust the value to toggle time between the program repling your new messages

        except(Exception): 
            print("no new messages")         
        sleep(6)#you can call this refresh rate adjust the value to toggle the time after which it searches for new messages  
     

        
check_for_new_text()



