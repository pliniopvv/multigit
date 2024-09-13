from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction
from PyQt5.QtGui import QIcon
import sys

from Window.RepositoryList import RepositoryList

__WINDOWS_OPEN = []

def open(window):
    __WINDOWS_OPEN.append(window)

def main():
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)

    # Criação do ícone
    icon = QIcon("icon.png")

    # Criação do SystemTray
    tray = QSystemTrayIcon()
    tray.setIcon(icon)
    tray.setVisible(True)

    # Criação do menu
    menu = QMenu()

    # Adicionando ações ao menu
    open_repositoryList = QAction("Configurar repositórios.")
    menu.addAction(open_repositoryList)
    open_repositoryList.triggered.connect(lambda : open(RepositoryList()))
    
    # Adicionando opção de sair
    quit_action = QAction("Sair")
    quit_action.triggered.connect(app.quit)
    menu.addAction(quit_action)

    # Adicionando o menu ao SystemTray
    tray.setContextMenu(menu)

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
