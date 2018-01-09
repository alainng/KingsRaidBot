from PIL import ImageGrab
import os
import time
import win32api, win32con
from cord import Cord
from PIL import ImageOps
from numpy import *

# Globals
# ------------------
 
x_pad = 38
y_pad = 29

#Prepare battle 1678 910
#Get Ready For battle 1402 929

def screenGrab():
    box = (x_pad+1,y_pad+1,x_pad+1808,y_pad+1018)
    im = ImageGrab.grab(box)
    ##im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +'.png', 'PNG')
    return im

def grab():
    box = (x_pad+1,y_pad+1,x_pad+1808,y_pad+1018)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    return a

def grab_end_repeat():
    box = (926,114,928,135)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    return a
    
def grab_insufficient_stamina(): #99937
    box = (500,530,1100,650)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    return a
    
def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    print("Click.")          #completely optional. But nice for debugging purposes.
    
def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    prin('left Down')
         
def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(.1)
    print('left release')

def mousePos(cord):
    win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))

def get_cords():
    x,y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    print(x,y)

def start_repeat_fight():
    repeat_counter=2
    mousePos(Cord.prepare_battle)
    leftClick()
    time.sleep(.75)
    mousePos(Cord.get_ready_for_battle)
    leftClick()
    time.sleep(.75)
    mousePos(Cord.auto_repeat)
    leftClick()
    time.sleep(.75)
    mousePos(Cord.auto_repeat_ok)
    leftClick()
    time.sleep(5)
    #Repeat the following block
    while (repeat_counter>0):
        while (grab_insufficient_stamina()!=100182 and grab_insufficient_stamina()!=99937):
            print('Still have stamina')
            time.sleep(5)
        print('No more stamina')
        mousePos(Cord.insufficient_stamina_ok)
        leftClick()
        time.sleep(1)
        mousePos(Cord.middle_stamina_potion)
        leftClick()
        time.sleep(1)
        mousePos(Cord.middle_stamina_potion_ok)
        leftClick()
        time.sleep(1)
        mousePos(Cord.middle_stamina_potion_ok_yes)
        leftClick()
        time.sleep(1)
        mousePos(Cord.middle_stamina_potion_ok_yes_repeat)
        leftClick()
        time.sleep(1)
        mousePos(Cord.middle_stamina_potion_ok_yes_repeat_ok)
        leftClick()
        time.sleep(3)
        #repeat ends
        repeat_counter = repeat_counter-1
        print('repeat counter left')
        print(repeat_counter)
    print('Done')
    
    
    
def sell_all():
    mousePos(Cord.inventory)
    leftClick()
    time.sleep(.75)
    mousePos(Cord.i_sell)
    leftClick()
    time.sleep(.75)
    mousePos(Cord.i_sellgrind_all)
    leftClick()
    time.sleep(.75)
    mousePos(Cord.i_sellgrind_all_confirmation)
    leftClick()
    time.sleep(.75)
    mousePos(Cord.i_sellgrind_all_confirmation_confirm)
    leftClick()
    time.sleep(1.25)
    mousePos(Cord.back)
    leftClick()
    time.sleep(0.75)

def collect_mail(): #untested
    mousePos(Cord.mail)
    leftClick()
    time.sleep(2)
    mousePos(Cord.m_claim_all)
    leftClick()
    time.sleep(2)
    mousePos(Cord.m_confirm)
    leftClick()
    time.sleep(2)

    
def main():
    start_repeat_fight()
    #sell_all()
    pass
 
if __name__ == '__main__':
    main()