#: hello_commands.py
# -*- coding: utf-8 -*-
from xSide import xside
from qSide import QAction, QRoundMenu, Qt


class HelloCommands(object):

    def setupWindowTitle(self):
        xside.window.setMainWindowTitle('Hello Commands')

    def registerCommands(self):
        # Command = 用户意图
        xside.commands.register('hello.sayHello', self.sayHello)
        xside.commands.register('hello.exit', self.exitApp)

    def setupMenuBar(self):
        fileMenu = QRoundMenu("File", id='file-menu')

        helloAction = QAction(
            "Say Hello",
            triggered=lambda: xside.commands.execute('hello.sayHello')
        )

        exitAction = QAction(
            "Exit",
            shortcut='Ctrl+Q',
            shortcutContext=Qt.ShortcutContext.WindowShortcut,
            triggered=lambda: xside.commands.execute('hello.exit'),
            id='exit'
        )

        fileMenu.addAction(helloAction)
        fileMenu.addAction(exitAction)

        xside.window.registerMenu(fileMenu)
        xside.window.addMenu('file-menu')

        xside.window.registerAction(exitAction)
        xside.window.addMainWindowAction('exit')

    def sayHello(self):
        # 通过 Window Service 操作 UI
        xside.window.showErrorMessage("Hello from Command!")
        return True

    def exitApp(self):
        from qSide import QApplication
        QApplication.instance().quit()
        return True


if __name__ == "__main__":
    plugins = xside.findXPlugins()
    xside.bootup("0.1.0a", "HelloCommands", plugins=plugins, dev=True)

    app = HelloCommands()
    app.setupWindowTitle()
    app.registerCommands()
    app.setupMenuBar()

    xside.run()
