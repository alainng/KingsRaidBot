from PIL import ImageGrab
import os
import time

# Globals
# ------------------
 
x_pad = 38
y_pad = 29


def screenGrab():
    box = (x_pad+1,y_pad+1,x_pad+1808,y_pad+1018)
    im = ImageGrab.grab()
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +
'.png', 'PNG')
 
def main():
    screenGrab()
 
if __name__ == '__main__':
    main()