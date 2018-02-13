from PIL import ImageGrab
import time
import win32api, win32con
from cord import Cord
from PIL import ImageOps
from numpy import *
import sys

# Globals
# ------------------
 
x_pad = 15#38
y_pad = 15#29


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

def grab2(w,x,y,z):
    box = (w,x,y,z)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    return a  
    
def grab_ready_to_duel(): #42525
    box = (1442,945,1690,990)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    #print("ready2duel")
    #print(a)
    if a==42623:
        return True
    else:
        return False

def grab_pick_ban_left(): #9347 neutral wait
    box = (423,125,529,160)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    #print("left")
    #print(a)
    if(a!=8660):
        return True
    else:
        return False

def grab_pick_ban_right(): #1873
    box = (1360,125,1400,160)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    #print("right")
    #print(a)
    if(a!=1828):
        return True
    else:
        return False
    
    
def grab_mail_status(): #nomail 23543
    box = (1525,55,1586,92)
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
    print(x, y)

    
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

def sell_all():
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

def get_number_of_bans_left():
    leftleft=grab2(323,948,323+33,948+33) #1099 is empty
    leftright=grab2(410,948,410+33,948+33)
    result_left_bans = 0
    if leftleft != 1099:
        result_left_bans = result_left_bans+1
    if leftright != 1099:
        result_left_bans = result_left_bans+1
    return result_left_bans

def get_number_of_bans_right():
    rightleft=grab2(1438,948,1438+33,948+33)
    rightright=grab2(1525,948,1525+33,948+33)
    result_right_bans = 0
    if rightleft != 1099:
        result_right_bans = result_right_bans+1
    if rightright != 1099:
        result_right_bans = result_right_bans+1
    return result_right_bans

    
def start_loh():
    while True:
        moveClickSleep(Cord.loh_ready_to_duel,0.75)
        moveClickSleep(Cord.loh_disconnect_warning,5)
        started_pick_ban = False
        ban_toggle=True
        while not grab_ready_to_duel():
            time.sleep(1)
                
            if grab_pick_ban_left() and grab_pick_ban_right():
                print("not in pickban")
                if started_pick_ban:
                    moveClickSleep(Cord.loh_exit,1)
            elif not grab_pick_ban_left():
                print("opponent turn")
            else:
                print("my turn")
                started_pick_ban = True
                if ban_toggle:
                    print("banning")
                    moveClickSleep(Cord.loh_wizard,0.21)
                    moveClickSleep(Cord.loh_wizard_nyx,0.21)
                    moveClickSleep(Cord.loh_select,0.21)
                    moveClickSleep(Cord.loh_wizard_artemia,0.21)
                    moveClickSleep(Cord.loh_select,0.21)
                    moveClickSleep(Cord.loh_wizard_aisha,0.21)
                    moveClickSleep(Cord.loh_select,0.21)
                    moveClickSleep(Cord.loh_wizard_cleo,0.21)
                    moveClickSleep(Cord.loh_select,0.21)
                    moveClickSleep(Cord.loh_all,0.21)

                    ban_toggle = not ban_toggle
                else:
                    print("picking")
                    moveClickSleep(Cord.loh_epis,0.23)
                    moveClickSleep(Cord.loh_select,0.23)
                    moveClickSleep(Cord.loh_jane,0.23)
                    moveClickSleep(Cord.loh_select,0.23)
                    moveClickSleep(Cord.loh_clause,0.23)
                    moveClickSleep(Cord.loh_select,0.23)
                    moveClickSleep(Cord.loh_gau,0.23)
                    moveClickSleep(Cord.loh_select,0.23)
                    moveClickSleep(Cord.loh_arch,0.23)
                    moveClickSleep(Cord.loh_select,0.23)
                    moveClickSleep(Cord.loh_roy,0.23)
                    moveClickSleep(Cord.loh_select,0.23)
                    
                    moveClickSleep(Cord.loh_kaulah,0.23)
                    moveClickSleep(Cord.loh_select,0.23)
                    moveClickSleep(Cord.loh_frey,0.23)
                    moveClickSleep(Cord.loh_select,0.23)


def main():
    start_loh()
    pass
 
if __name__ == '__main__':
    main()