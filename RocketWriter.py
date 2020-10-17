import keyboard
from pathlib import Path
import time

cfg = "My awesome text"


def readCfg():
    global cfg
    if not Path("cfg.txt").is_file():
        with open('cfg.txt', 'w') as myfile:
            myfile.write(cfg)
    else:
        with open('cfg.txt', 'r') as myfile:
            cfg = myfile.read()


def writeText():
    global cfg
    time.sleep(0.25)
    for x in range(len(cfg)):
        keyboard.press_and_release(str(cfg[x]))


readCfg()
print("Hotkey2write: ctrl+h | Hotkey2readfile: ctrl+j")
keyboard.add_hotkey('ctrl+h', writeText)
keyboard.add_hotkey('ctrl+j', readCfg)
while True:
    pass
