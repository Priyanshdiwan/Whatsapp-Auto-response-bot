import pyautogui as pt#locates mouse pointer and gets me its color
from time import sleep


while True:
    posyXY=pt.position()
    print(posyXY,pt.pixel(posyXY[0],posyXY[1]))
    sleep(1)
    if posyXY[0]==0:
        break
