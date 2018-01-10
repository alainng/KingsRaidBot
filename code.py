from PIL import ImageGrab
import os
import time
import win32api, win32con
from cord import Cord
from PIL import ImageOps
from numpy import *
import sys

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

def grab_mail_status(): #nomail 23543
    box = (1525,55,1586,92)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    return a
    
def grab_session_expired(): #to be fixed
    box = (483,240,1400,834)
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
    
def mousePos(cord):
    win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))

def get_cords():
    x,y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    print(x,y)

def start_repeat_fight():
    repeat_counter=150
    while(repeat_counter>0):
        #if mail, get mail stuff
        if(grab_mail_status()!=23543):
            collect_mail()
        #start fight sequence
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
        #in fight
        stamina_check_counter=0
        while (grab_insufficient_stamina()!=100182 and grab_insufficient_stamina()!=99937):
            if(stamina_check_counter > 360):
                sys.exit()
            time.sleep(5)
            stamina_check_counter = stamina_check_counter +1
        mousePos(Cord.insufficient_stamina_ok)
        leftClick()
        time.sleep(2)
        mousePos(Cord.middle_stamina_potion) #make sure that stamina recovery items > 1 run
        leftClick()
        time.sleep(2)
        mousePos(Cord.middle_stamina_potion_ok)
        leftClick()
        time.sleep(1)
        mousePos(Cord.middle_stamina_potion_ok_yes)
        leftClick()
        time.sleep(1)
        mousePos(Cord.middle_stamina_potion_ok_yes_x)
        leftClick()
        time.sleep(1)
        sell_all_post_fight()
        repeat_counter=repeat_counter-1
    print(repeat_counter)
    
  
    
def sell_all_post_fight():
    mousePos(Cord.post_fight_inventory)
    leftClick()
    time.sleep(15)
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
    time.sleep(3)

def collect_mail(): #untested
    mousePos(Cord.mail)
    leftClick()
    time.sleep(2)
    mousePos(Cord.m_claim_all)
    leftClick()
    time.sleep(3)
    mousePos(Cord.m_claim_all)
    leftClick()
    time.sleep(1)
    mousePos(Cord.m_x)
    leftClick()
    time.sleep(1)
    

    
def main():
    start_repeat_fight()
    #sell_all()
    pass
 
if __name__ == '__main__':
    main()