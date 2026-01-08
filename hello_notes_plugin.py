# -*- coding: utf-8 -*-
# Copyright (C) 2018-2026 Connet Information Technology Company, Shanghai.

try:
    import x_notes
except ImportError:
    raise ImportError("Please install Notes plugin first! run `cd Notes; pip install -e .`")


from qSide import QAction
from xSide import xside

class HelloNotes(object):

    def setupWindowTitle(self):
        xside.window.setMainWindowTitle('Hello Notes')

    def setupTooBar(self):
        self.addNoteAction = QAction(
            '+',
            tip='Add note',
            triggered=self.onAddNoteActionTriggered,
            id='add-note'
        )
        self.removeNoteAction = QAction(
            '-',
            tip='Delete note',
            triggered=self.onRemoveNoteActionTriggered,
            id='remove-note'
        )

        xside.window.registerAction(self.addNoteAction)
        xside.window.registerAction(self.removeNoteAction)

        xside.window.addToolBarAction(
            'top-tool-bar',
            'add-note',
        )
        xside.window.addToolBarAction(
            'top-tool-bar',
            'remove-note',
        )

    def setupLayout(self):
        xside.window.addToolWindow(
            title="Notes",
            icon="text",
            id="notes-view",
            area=xside.window.ToolWindowArea.Right
        )

        # 显示 Tool Window
        xside.window.showToolWindow("notes-view")

    def onAddNoteActionTriggered(self):
        def then(text, ok):
            if not ok:
                return
            else:
                xside.notes.add(text)

        xside.window.showTextInputBox("Take note", then=then)

    def onRemoveNoteActionTriggered(self):
        id = xside.notes.currentId()
        xside.notes.remove(id) if id is not None else ...


if __name__ == "__main__":
    plugins = xside.findXPlugins()
    xside.bootup("0.1.0a", 'Hello Notes', plugins=plugins, dev=True)
    hello = HelloNotes()
    hello.setupWindowTitle()
    hello.setupTooBar()
    hello.setupLayout()
    xside.run()
