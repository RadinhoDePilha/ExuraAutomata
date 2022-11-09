from threading import Thread
from typing import Any, Callable, ClassVar, Optional, Tuple
from pynput import mouse
from pynput.mouse import Button


class MouseCapture():
    def __init__(self, *args, **kwargs) -> None:
        self.x = 0
        self.y = 0
        self.w = 0
        self.h = 0
    
    def capture(
        self,
        callback: Callable=None) -> Tuple:
        """
        Listen the mouse Left button to return a box position and
        measurements

        Args:
            callback (Callable, optional): Call a function before return.

        Returns:
            Tuple: ( x, y, width, height)
        """
        def on_click(x, y, button, pressed) -> None:
            if button == Button.left and pressed == True:
                self.x, self.y = x, y
            
            if button == Button.left and pressed == False:
                self.w, self.h = x, y
                
            if not pressed:
                return False
            
        with mouse.Listener(
                on_click=on_click,
                ) as listener:
            listener.join()
            
            if callback != None:
                callback()
            
            print((self.x, self.y, self.w, self.h))
            return (self.x, self.y, self.w, self.h)
        
        
if __name__ == "__main__":
    mouse_capture = MouseCapture()
    print(mouse_capture.capture())




    
