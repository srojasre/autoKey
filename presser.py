import pyautogui
import time
class Macro:
    def __init__(self) -> None:
        pass
    
    def pressOne(self, key):
        pyautogui.press(str(key))
        
    def autoPresser(self, time_ms, key, activo=False):
        
        while activo:
            pyautogui.press(str(key))
            time.sleep(time_ms/1000)
            
            
            
            
        