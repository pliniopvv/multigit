from Window.Screens import ListRepository
from pystray import Icon, MenuItem as Item
from PIL import Image

import threading
import psutil
import os

def upPriority(win):
    p = psutil.Process(os.getpid())
    p.nice(psutil.REALTIME_PRIORITY_CLASS)
    win()

def createThread(win):
    threading.Thread(daemon=True, target=lambda : upPriority(win)).start()

__ITEMS = []

def close():
    # __ICON.stop()
    os._exit(0)

def makeSystemTray():
    def IconImage():
        image = Image.open('src/icon.png')
        return image

    icon = Icon(
        'test name',
        icon=IconImage(),
        menu=tuple(__ITEMS))
    
    return icon

def makeItem(title, action):
    __ITEMS.append(Item(
            title,
            action=action
    ))

def startSystemTray():
    makeItem('Repositórios', lambda : createThread(ListRepository))
    makeItem('Sair', close)

    process = psutil.Process(os.getpid())
    process.nice(psutil.ABOVE_NORMAL_PRIORITY_CLASS)

    makeSystemTray().run()
