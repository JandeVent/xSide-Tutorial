#: hello_tool_window.py
# -*- coding: utf-8 -*-
from xSide import xside
from qSide import QLabel


class HelloToolWindow(object):

    def setupWindowTitle(self):
        xside.window.setMainWindowTitle('Hello Tool Window')

    def setupToolWindow(self):
        # Tool Window 的内容只是一个普通 QWidget
        widget = QLabel("Hello from Tool Window!")
        # 设置对象ID
        widget.setObjectName('hello-tool')
        widget.setMinimumWidth(200)

        # 注册并添加 Tool Window
        xside.window.registerToolWindow(widget)
        xside.window.addToolWindow(
            title="Hello Tool",
            icon="target",
            id="hello-tool",
            area=xside.window.ToolWindowArea.Left
        )

        # 显示 Tool Window
        xside.window.showToolWindow("hello-tool")


if __name__ == "__main__":
    plugins = xside.findXPlugins()
    xside.bootup("0.1.0a", "HelloToolWindow", plugins=plugins, dev=True)

    app = HelloToolWindow()
    app.setupWindowTitle()
    app.setupToolWindow()

    xside.run()
