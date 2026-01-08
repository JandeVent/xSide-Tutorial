# -*- coding: utf-8 -*-
# Copyright (C) 2018-2026 Connet Information Technology Company, Shanghai.

from xSide import xside

class HelloWorld(object):
    def setupWindowTitle(self):
        xside.window.setMainWindowTitle('Hello World')

if __name__ == "__main__":
    plugins = xside.findXPlugins()
    xside.bootup("0.1.0a", 'Hello', plugins=plugins, dev=True)
    hello = HelloWorld()
    hello.setupWindowTitle()
    xside.run()
