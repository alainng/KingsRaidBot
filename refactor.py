import pyautogui
from cord import Cord
import sys
import time

pyautogui.FAILSAFE = True

def screenGrab():
    #left top width height
    box = (x_pad+1,y_pad+1,x_pad+1808,y_pad+1018)
    return pyautogui.sreenshot(region=box)

def get_cords():
    print(pyautogui.position())

def moveClickSleep(cord,time):
    pyautogui.click(x=cord[0],y=cord[1])
    time.sleep(time)

def main():
    test()
    #sell_all()
    pass
 
if __name__ == '__main__':
    main()