from Window.Screens.ListRepository import ListRepository
from pystray import Icon, Menu, MenuItem as Item
from PIL import Image
import pystray

__ICON = None
__ITEMS = []

def close():
    __ICON.stop()

def makeSystemTray():
    def IconImage():
        image = Image.open('src/icon.png')
        return image

    icon = pystray.Icon(
        'test name',
        icon=IconImage(),
        menu=tuple(__ITEMS))

    return icon

def makeItem(title, action):
    __ITEMS.append(Item(
            title,
            lambda : action()
    ))

def startSystemTray():
    makeItem('Repositórios', ListRepository)
    makeItem('Sair', close)
    makeSystemTray().run()


