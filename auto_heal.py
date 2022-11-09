from time import sleep
from get_status import StatusGetter
from exception_decorators import runtime_pass, typeerror_pass, valueerror_pass
from threading import Thread, Lock
import pyautogui
import threading
import pymsgbox
from logs import make_log

class AutoHeal(StatusGetter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.case1 = 8
        self.case2 = 8
        self.case3 = 8
        
        self.keyse1 = 'F1'
        self.keyse2 = 'F3'
        self.keyse3 = 'F4'
    

    def bot(self):
        """
        Compare the cases configurations with the value returned by get_status
        to use the respective key
        """
        try:
            if self.status > self.case1:
                make_log('Healing Case 1, K:', self.keyse1 )
                pyautogui.press(self.keyse1)
                
            
            elif self.status > self.case2:
                make_log('Healing Case 2, K:', self.keyse2 )
                pyautogui.press(self.keyse2)
                
            elif self.status > self.case3:
                make_log('Healing Case 2, K:', self.keyse2 )
                pyautogui.press(self.keyse3)
        except TypeError:
            sleep(1)
                
        except Exception as error:
            make_log('ERROR HEAL: ' + str(error))
            pymsgbox.alert(
                text="Ocorreu um erro. Por favor, encerre o programa.",
                title="ERROR",)
            

if __name__ == "__main__":
    pass
