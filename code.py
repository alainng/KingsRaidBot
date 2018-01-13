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

def moveClickSleep(cord,seconds):
    win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))
    leftClick()
    time.sleep(seconds)

    
def get_cords(): #debug function
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
        moveClickSleep(Cord.prepare_battle,0.75)
        moveClickSleep(Cord.get_ready_for_battle,0.75)
        moveClickSleep(Cord.auto_repeat,0.75)
        moveClickSleep(Cord.auto_repeat_ok,5)

        #in fight
        stamina_check_counter=0
        while (grab_insufficient_stamina()!=100182 and grab_insufficient_stamina()!=99937):
            if(stamina_check_counter > 360):
                sys.exit()
            time.sleep(5)
            stamina_check_counter = stamina_check_counter +1
        
        moveClickSleep(Cord.insufficient_stamina_ok,2)
        #make sure that stamina recovery items > 1 run
        moveClickSleep(Cord.middle_stamina_potion,2)
        moveClickSleep(Cord.middle_stamina_potion_ok,1)
        moveClickSleep(Cord.middle_stamina_potion_ok_yes,3)
        moveClickSleep(Cord.middle_stamina_potion_ok_yes_x,1)
        
        sell_all_post_fight()
        repeat_counter=repeat_counter-1
    print(repeat_counter)

def start_natural_fight():
    repeat_counter=150
    stamina_to_gain=36
    time_per_stamina=49
    time_to_wait=stamina_to_gain*time_per_stamina
    while(repeat_counter>0):
        if(grab_mail_status()!=23543):
            collect_mail()
        #start fight sequence
        moveClickSleep(Cord.prepare_battle,0.75)
        moveClickSleep(Cord.get_ready_for_battle,0.75)
        moveClickSleep(Cord.auto_repeat,0.75)
        moveClickSleep(Cord.auto_repeat_ok,5)
        
        #in fight
        stamina_check_counter=0
        while (grab_insufficient_stamina()!=100182 and grab_insufficient_stamina()!=99937):
            if(stamina_check_counter > 360):
                sys.exit()
            time.sleep(5)
            stamina_check_counter = stamina_check_counter +1
        moveClickSleep(Cord.insufficient_stamina_ok,2)
        moveClickSleep(Cord.middle_stamina_potion_x,1)
        moveClickSleep(Cord.post_fight_exit,1)
        time.sleep(time_to_wait)
        
        repeat_counter=repeat_counter-1
    print(repeat_counter)
    
def sell_all_post_fight():
    moveClickSleep(Cord.post_fight_inventory,15)
    moveClickSleep(Cord.i_sell,1)
    moveClickSleep(Cord.i_sellgrind_all,1)
    moveClickSleep(Cord.i_sellgrind_all_confirmation,1)
    moveClickSleep(Cord.i_sellgrind_all_confirmation_confirm,1.25)
    moveClickSleep(Cord.back,3)
   

def collect_mail():
    moveClickSleep(Cord.mail,3)
    moveClickSleep(Cord.m_claim_all,4)
    moveClickSleep(Cord.m_claim_all,2)
    moveClickSleep(Cord.m_x,1)
    

    
def main():
    start_repeat_fight()
    #sell_all()
    pass
 
if __name__ == '__main__':
    main()