from kivy.app import App
from kivy.core.window import Window
from kivy.lang.builder import Instruction
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.graphics import Line, Color
from typing import Final
from kivy.utils import rgba


class LinearFunction(Screen):
    sm = ScreenManager()
    txt = ObjectProperty()

    def __init__(self, **kw):
        super().__init__(**kw)

    def change(self):
        db = open('db.txt', 'w')
        db.write(self.txt.text)
        db.close()
        App.get_running_app().root.current = 'line'
