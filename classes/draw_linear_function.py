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
from classes import straight, menu_screen, lin_function


class DrawLinearFunctionScreen(Screen):
    drawButton = ObjectProperty()

    def __init__(self, **kw):
        super().__init__(**kw)
        self.straight_line = straight.Straight()
        self.add_widget(self.straight_line)

    def drawingWindow(self):
        self.drawButton.text = ''
        self.straight_line.draw()
