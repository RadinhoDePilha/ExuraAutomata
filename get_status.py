
from typing import Any, Tuple
import pyautogui
from logs import make_log
import os
import pyscreeze
from threading import Lock, Thread, Event
from exception_decorators import runtime_pass, typeerror_pass, valueerror_pass
from abc import ABC, abstractclassmethod 
from time import sleep
from PyQt5.QtCore import pyqtSignal


class StatusGetter(Thread, ABC):
    

    def __init__(self, ico: str, status_bar: str, bar_folder: str,\
        y_add: int, lock: Lock, *args, region: tuple=None, **kwargs) -> None:
        """
        Args:
            ico (str): path of icon file
            status_bar (str): path of bar file
            bar_folder (str): path of bar directory
            lock (Lock): Common lock
            region (tuple, optional): A tuple box of the region to
            compare . Defaults to None.
        """
        super().__init__()
        
        self._status_bar = status_bar
        self._bar_folder = bar_folder
        
        self.palmeiras_titles = None
        self.y_add = y_add
        self.status = None
        self.on = False
        self.speed = 1
        self.lock = lock
        self.ico = ico
        
        if region != None:
            self.region = (
                region[0], 
                region[1],
                region[2] - region[0],
                region[3] - region[1])
        else:
            self.region = None
        

    @abstractclassmethod
    @runtime_pass
    @valueerror_pass
    def bot(self):
        pass
    
    
    def stop(self):
        """ Kill the process with a joke """
        self.palmeiras_titles = 1
        
        
    def run(self):
        """
        Constantly calls the comparator
        """
        while self.palmeiras_titles == None:
            try:
                if self.on:
                    if self.region == None:
                        pyautogui.alert(
                        text="Por favor, selecione uma região primeiro.",
                        title="ERROR",
                        button='OK',
                        
                    )
                    
            
            
                    haystack = pyscreeze.screenshot(region=self.region)
                    ico = self.get_status_ico(haystack)
                    
                    if ico != None:
                        self.get_bar(ico)
                        self.status = int(self.comparator()[4])
                        self.lock.acquire()
                        self.bot()
                        self.lock.release()
                        
                    else:
                        pass
                
                
                pyautogui.sleep(self.speed)
            except Exception as error:
                make_log('ERROR GET STATUS: ' + str(error))
                pyautogui.sleep(self.speed)
                
    @staticmethod
    def rm_file(file: str):
        """
        Remove securely a file

        Args:
            file (str): File Path
        """
        try:
            os.remove(file)
        except FileNotFoundError:
            pass
    
    def get_status_ico(self, haystack: Any) -> Tuple[int, int, int, int]:
        """
        Find the icon on the haystack area and return his position on
        the screen

        Args:
            haystack (Any): A source of a image or a openCV image

        Returns:
            Tuple: A box (x, y, width, height ) of the icon based o n screen
        """
        needle = pyscreeze.locate(self.ico, haystack)
        needle_on_screen = (
            self.region[0] + needle[0],
            self.region[1] + needle[1],
            needle[2],
            needle[3]
        )
        
        return needle_on_screen
    
        
    @typeerror_pass
    def get_bar(self, ico_box) -> Tuple:
        """
        Get a bar image positioned by get_stop_button

        Returns:
            Tuple: _description_
        """
        ix, iy, iw, ih = ico_box
        self.rm_file(self._status_bar)
        bar_box = (ix, iy + self.y_add, 108, 10)
        pyautogui.screenshot(self._status_bar, region=bar_box)
        
        return bar_box
        
    def comparator(self):
        """
        Try to compare the status bar with all the images on the bar_folder
        untill find a match.
        """
        for image in sorted(os.listdir(self._bar_folder)):
            try:
                if pyscreeze.locate(
                    haystackImage=self._status_bar,
                    needleImage=self._bar_folder + image,
                    grayscale=True
                    
                    ):
                
                    return image
        
            except ValueError:
                pass
            
        return os.listdir(self._bar_folder)[8]

            

if __name__ == "__main__":
    pass