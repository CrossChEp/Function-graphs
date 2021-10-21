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

class Straight(Widget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def draw(self):
        db = open('db.txt', 'r')
        coords = list(db.read().split())
        db.close()
        k = float(coords[0])
        b = float(coords[1])
        with self.canvas:
            Color(1, 1, 1)
            ed = 50
            x1 = 5700
            x2 = 70000
            x1 /= ed
            x2 /= ed
            y1 = (k * x1 + b) * -1
            y2 = (k * x2 + b) + 300
            self.y_axis = Line(points=[350, 1000, 350, 0], width=2)
            self.x_axis = Line(points=[0, 220, 1000, 220], width=2)
            self.line = Line(points=[x1, y1, x2, y2])
            self.unit_segment_x_negative = Line(points=[300, 260, 300, 180])
            self.unit_segment_y_negative = Line(points=[400, 260, 400, 180])
