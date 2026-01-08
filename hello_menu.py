# -*- coding: utf-8 -*-
# Copyright (C) 2018-2026 Connet Information Technology Company, Shanghai.

from xSide import xside
from qSide import QAction, QRoundMenu, Qt


class HelloMenu(object):

    def setupWindowTitle(self):
        xside.window.setMainWindowTitle('Hello Menu Bar')

    def setupMenuBar(self):
        # ===== File Menu =====
        fileMenu = QRoundMenu("File", id='file-menu')

        helloAction = QAction(
            "Say Hello",
            triggered=self.sayHello
        )

        exitAction = QAction(
            "Exit",
            shortcut='Ctrl+Q',
            shortcutContext=Qt.ShortcutContext.WindowShortcut,
            triggered=self.exitApp,
            id='exit'
        )

        fileMenu.addAction(helloAction)
        fileMenu.addAction(exitAction)

        # ===== Edit Menu =====
        editMenu = QRoundMenu("Edit", id='edit-menu')

        dummyAction = QAction(
            "Nothing to Undo",
            enabledPredicate=lambda act: False
        )
        editMenu.addAction(dummyAction)

        # ===== Register menus & actions =====
        xside.window.registerMenu(fileMenu)
        xside.window.registerMenu(editMenu)

        xside.window.addMenu('file-menu')
        xside.window.addMenu('edit-menu')

        xside.window.registerAction(exitAction)
        xside.window.addMainWindowAction('exit')

    def sayHello(self):
        xside.window.showQuestionMessage("Hello from Menu!")

    def exitApp(self):
        from qSide import QApplication
        QApplication.instance().quit()


if __name__ == "__main__":
    plugins = xside.findXPlugins()
    xside.bootup("0.1.0a", "HelloMenu", plugins=plugins, dev=True)

    app = HelloMenu()
    app.setupWindowTitle()
    app.setupMenuBar()

    xside.run()