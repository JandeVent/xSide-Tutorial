# -*- coding: utf-8 -*-
# Copyright (C) 2018-2026 Connet Information Technology Company, Shanghai.

import uuid
from typing import Dict
from packaging.version import Version

from xSide import xside
from qSide import QPlugin, Signal, QWidget, QListWidget, QVBox, QListWidgetItem, Qt


class NotesView(QWidget):
    def __init__(self):
        super().__init__()
        self._list = QListWidget()
        self.setLayout(QVBox(self._list))

    def add(self, id: str, note: str):
        item = QListWidgetItem(note)
        item.setData(Qt.ItemDataRole.UserRole, id)
        self._list.addItem(item)

    def remove(self, id: str):
        for row in range(self._list.count()):
            item = self._list.item(row)
            if item.data(Qt.ItemDataRole.UserRole) == id:
                self._list.takeItem(row)

    def currentId(self) -> str | None:
        item = self._list.currentItem()
        if item:
            return item.data(Qt.ItemDataRole.UserRole)
        else:
            return None


class Notes(QPlugin):

    noteAdded = Signal(str)
    """UUID of note"""
    noteRemoved = Signal(str)
    """UUID of note"""

    def __init__(self):
        super().__init__(
            name='notes',
            version=Version('0.1.0a0'),
            author='Connet Information Technology Company Ltd, Shanghai.',
            title='Notes',
            description='Simple notes service',
        )
        self._view = None
        self._notes: Dict[str, str] = {}

    def bootup(self):
        self._view = NotesView()
        self._view.setObjectName('notes-view')
        xside.window.registerToolWindow(self._view)

    def add(self, note: str) -> str:
        """
        :param note:
        :return: Note UUID
        """
        id = str(uuid.uuid4())
        self._view.add(id, note)
        self._notes[id] = note
        self.noteAdded.emit(id)
        return id

    def remove(self, id: str):
        """
        :param id:
        :return:
        """
        self._notes.pop(id)
        self._view.remove(id)
        self.noteRemoved.emit(id)

    def currentId(self) -> str | None:
        return self._view.currentId()

