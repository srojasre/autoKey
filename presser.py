import pyautogui
import time

class Macro:
    def __init__(self, default_key='-'):
        self.default_key = default_key

    def auto_presser(self, time_ms, key=None, activo=False):
        
        key = key or self.default_key
        while activo:
            pyautogui.press(str(key))
            time.sleep(time_ms / 1000)

    def mouse_click(self, time_ms, click_button='left', activo=False):
        
        while activo:
            pyautogui.click(button=click_button)
            time.sleep(time_ms / 1000)