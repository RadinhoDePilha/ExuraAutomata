from get_status import StatusGetter
from exception_decorators import runtime_pass, valueerror_pass
import pyautogui
import pymsgbox
from logs import make_log
import threading
from pynput import keyboard
from time import sleep
from pynput.keyboard import Listener

class AutoMana(StatusGetter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.case1 = 8
        self.case2 = 8
        self.case3 = 8
        
        self.keyse1 = 'F2'
        self.keyse2 = 'F4'
        self.keyse3 = 'F2'
        
        # self.locker1 = threading.Lock()
    
    
    def bot(self):
        """
        Compare the cases configurations with the value returned by get_status
        to use the respective key
        """
        try:
            if self.status > self.case1:
                make_log('Mana Case 1, K:', self.keyse1 ) 
                pyautogui.press(self.keyse1)
            
            elif self.status > self.case2:
                make_log('Mana Case 1, K:', self.keyse1 ) 
                pyautogui.press(self.keyse2)
                
            elif self.status > self.case3:
                make_log('Mana Case 1, K:', self.keyse1 ) 
                pyautogui.press(self.keyse3)
        
        except TypeError:
            sleep(1)
                
        except Exception as error:
            make_log('ERROR: ' + str(error))
            pymsgbox.alert(
                text="Ocorreu um erro. Por favor, encerre o programa.",
                title="ERROR",)
            
    
                
if __name__ == "__main__":
    pass