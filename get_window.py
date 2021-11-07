import time
import pygetwindow as pyGW

def check_window(self):
    try:
        pyGW.getWindowsWithTitle(self)[0]
        return(True)
    except:
        print(self, 'not found')
        return(False)
        
def get_window(self):
    window = pyGW.getWindowsWithTitle(self)[0]
    if window.isMinimized:
        window.restore()
        window.activate()
        window.maximize()
        time.sleep(0.5)
    else:
        window.activate()
        window.maximize()
        time.sleep(0.5)

def minimize_window(self):
    window = pyGW.getWindowsWithTitle(self)[0]
    window.minimize()