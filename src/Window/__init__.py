from Kernel import ImplKernel as Kernel
from Window.Screens import ListRepository

from git import Repo
from pystray import Icon, MenuItem as Item

from PIL import Image
import schedule
import time

import threading
import psutil
import os

import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

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
    Kernel.tray = icon
    return icon

def makeItem(title, action):
    __ITEMS.append(Item(
            title,
            action=action
    ))

def checkRepos():
    logger.info("Executando checagem ...")
    repos = Kernel.config.getRepositorios()
    hasUpdate = []
    for model in repos:
        try:
            repo = Repo(model.path)
            repo.remotes.origin.fetch()
            remote_commits = repo.git.rev_list('HEAD..origin/master','--count')
            if int(remote_commits) > 0:
                hasUpdate.append(model.name)
                logger.info("Updates detectados no " + model.name + " disparando notificação .")
                # Kernel.tray.notify(model.name + " com updates !")
        except Exception:
            logger.error(model.name + " sem origin/master para checar.")
    if (len(hasUpdate) > 0):
        Kernel.tray.notify("Os repositórios " + ",".join(hasUpdate) + " possuem updates !")
    logger.info("Checagem finalizada .")


def configSchedule():
    # schedule.every(1).hours.do(checkRepos)
    schedule.every(10).seconds.do(checkRepos)
    logger.info("Configurado Schedule .")

    while True:
        schedule.run_pending()
        time.sleep(1)


def startSystemTray():
    makeItem('Repositórios', lambda : createThread(ListRepository))
    makeItem('Sair', close)

    process = psutil.Process(os.getpid())
    process.nice(psutil.ABOVE_NORMAL_PRIORITY_CLASS)

    threading.Thread(target=configSchedule, daemon=True).start()
    # configSchedule()
    makeSystemTray().run()
