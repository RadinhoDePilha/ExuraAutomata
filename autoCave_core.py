import tools
import os
import shutil
from threading import Lock, Thread
import cv2
import pyautogui
from imageLocation import locate_alpha
import pyscreeze as ps
from pathlib import Path
from time import sleep
from logs import make_log
import numpy as np
import ctypes

print(ctypes.CDLL('libX11.so.6').XInitThreads())
pyautogui.PAUSE = 0.001
 
class Bot():
    def __init__(self, lock: Lock) -> None:
        super().__init__()
        self.walk_on = False
        self.middle_map= None
        self.region_map= None
        self.region_backpack= None
        self.region_skm= None
        self.aa_region = None
        self.autoattack = False
        self.monsters_here= False
        self.dir = 'tmp/working/'
        self.middle_skm = None
        self.autolooting = False
        self.is_attacking = False
        self.autoloot_on = False
        self.spell = None
        self.trapped = 0
        self.lock = lock
              
    def run(self) -> None:
        
        Thread(target=self.botting, daemon=True).start()
        Thread(target=self.autoattack_bot, daemon=True).start()
      
    def botting(self) -> None:
        """
        Execute one function to each file in workfolder
        """
        make_log('iniciando...')
        while True:
            try:
                for file in sorted(os.listdir('tmp/working/')):
                    
                    sf = Path(file).suffix     
                    make_log(f'consultando {file}')
                    
                    if sf == '.png':
                        make_log('{file} é png')
                        while True:
                            
                            while self.walk_on == False:                  
                                sleep(1)
                                
                            
                            if not self.monsters_here:
                                make_log(f'Capturando mapa {self.region_map}')
                                
                                map = ps.screenshot(region=self.region_map)
                                middle = ps.screenshot(
                                    region=self.middle_map
                                )
                                
                                needle = ps.locate(self.dir + file, map)
                                
                                needle_on_middle = ps.locate(
                                    self.dir + file, middle
                                )
                                
                                make_log('checando...')
                                if needle != None and needle_on_middle == None:
                                    make_log( f'lesgooo') 
                                    needle = (
                                        self.region_map[0] + needle[0],
                                        self.region_map[1] + needle[1]
                                    )
                                    make_log('concatenou')
                                    make_log(needle) 
                                    self.lock.acquire()
                                    pyautogui.moveTo(needle[0], needle[1])
                                    pyautogui.click(needle[0], needle[1])
                                    self.lock.release()
                                    
                                    sleep(1)
                                else:
                                    make_log('next')
                                    break
                                
                            sleep(1)
                        
                    if sf == ".slp":
                        while self.walk_on == False:                  
                            sleep(1)
                            
                        make_log('é sleep')
                        with open(self.dir + file, 'r') as sleep_f:
                            x = sleep_f.read()
                            make_log('sleep' + x)
                            sleep(float(x))

                    if sf == '.py':
                        while self.walk_on == False:                  
                            sleep(1)
                                
                        os.system(f'python3 {self.dir + file}')
                        
            except pyautogui.FailSafeException:
                pyautogui.alert(
                text='Fail Safe ativado. Por favor, encerre o aplicativo',
                title='Aplicativo Abortado'
                )
                exit()
        
                    
            except Exception as error:
                make_log('ERROR IN BOTTING: ' + str(error))
                sleep(1)
            sleep(1)
                    
    def auto_loot(self) -> None:
        """
        Based on self.middle_skm, get the tiles of skm and do one right click
        for each tile
        """
        try:
            if self.middle_skm != None:
                tile = (
                        self.middle_skm[2] // 3,
                        self.middle_skm[3] // 3
                    )
                    
                tile1 = (self.middle_skm[0] + tile[0] * 1, \
                    self.middle_skm[1] + tile[1])
                tile2 = (self.middle_skm[0] + tile[0] * 2, \
                    self.middle_skm[1] + tile[1])
                tile3 = (self.middle_skm[0] + tile[0] * 3, \
                    self.middle_skm[1] + tile[1])
                tile4 = (self.middle_skm[0] + tile[0] * 1, \
                    self.middle_skm[1] + tile[1] * 2)
                tile5 = (self.middle_skm[0] + tile[0] * 2, \
                    self.middle_skm[1] + tile[1] * 2)
                tile6 = (self.middle_skm[0] + tile[0] * 3, \
                    self.middle_skm[1] + tile[1] * 2)
                tile7 = (self.middle_skm[0] + tile[0] * 1, \
                    self.middle_skm[1] + tile[1] * 3)
                tile8 = (self.middle_skm[0] + tile[0] * 2, \
                    self.middle_skm[1] + tile[1] * 3)
                tile9 = (self.middle_skm[0] + tile[0] * 3, \
                    self.middle_skm[1] + tile[1] * 3)

                tiles = (tile1, tile2, tile3,
                        tile4, tile5, tile6,
                        tile7, tile8, tile9)
                self.lock.acquire()
                pyautogui.keyDown('shift')
                for tile in tiles:
                    make_log(f'looting {tile}')
                    pyautogui.rightClick(tile)
                    sleep(0.2)
                pyautogui.keyUp('shift')
                self.lock.release()
            
            else:
                pyautogui.alert(
                    text='A área de loot ainda não foi configurada.',
                    title='Reconfigure o bot'
                    )
                
        except pyautogui.FailSafeException:
                pyautogui.alert(
                text='Fail Safe ativado. Por favor, encerre o aplicativo',
                title='Aplicativo Abortado'
                )
                exit()
        
                
        except Exception as error:
            make_log('ERROR IN AUTOLOOT :' + str(error))       
                
    def autoattack_bot(self) -> None:
        """
        Attack the enemies based on battle list
        """
        make_log('Iniciando o Bot Auto Attack')
        try:
            trapped = 0
            while True:
                
                if self.aa_region != None and self.autoattack == True:
                    tools.rm_file('tmp/m.png')
                    monster_list = ps.screenshot('tmp/m.png',region=self.aa_region)
                    
                    make_log('Pesquisando monstros...')
                    if ps.locate('assets/battlelist.png',\
                        monster_list) == None:
                        
                        monster_list = cv2.imread('tmp/m.png')
                        self.monsters_here = True
                        make_log('Tem monstro')
                        
                        if locate_alpha(
                            'assets/triggers/redsquare.png',
                            monster_list
                        ) or locate_alpha(
                            'assets/triggers/pinksquare.png',
                            monster_list
                        ):
                            if self.is_attacking == True:
                                self.trapped += 1
                            
                            if self.trapped > 30:
                                make_log('Trocando de alvo')
                                self.lock.acquire()
                                pyautogui.press(' ')
                                self.lock.release()
                                self.trapped = 15
                                
                                
                            self.is_attacking = True
                            make_log('Já está atacando, vou aproveitar para\
                                castar uma spell')
                            
                            if self.spell != None:
                                self.lock.acquire()
                                for spell in self.spell:
                                    pyautogui.press(spell)
                                self.lock.release()
                            
                            
                        else:
                            if self.is_attacking and self.autoloot_on:
                                self.auto_loot()
                                self.trapped = 0
                                
                            make_log('Ninguém sendo atacado, vou atacar')
                            self.lock.acquire()
                            pyautogui.press(' ')
                            self.lock.release()
                            sleep(0.5)
                        # pyautogui.hotkey('ctrl', ' ')
                        
                        
                    else:
                        make_log('sem monstros')
                        if self.monsters_here and self.autoloot_on:
                            self.auto_loot()
                            self.trapped = 0
                            
                        self.monsters_here = False    
        
                sleep(1)
        except pyautogui.FailSafeException:
                pyautogui.alert(
                text='Fail Safe ativado. Por favor, encerre o aplicativo',
                title='Aplicativo Abortado'
                )
                exit()
                
        except Exception as error:
            make_log('ERROR IN AUTOATTACK: ' + str(error))

                    
                
                
            
    
if __name__ == "__main__":
    sleep(3)
    bot = Bot()
    bot.run()