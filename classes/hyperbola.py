from kivy.core.window import Window
from kivy.lang.builder import Instruction
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.graphics import Line, Color, Rectangle, Ellipse
from typing import Final
from kivy.utils import rgba



class Hyperbola(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def draw(self):
        db = open('db.txt', 'r')
        coords = list(db.read().split())
        db.close()
        ed = 50  # 1 единица отрезка
        k = int(coords[0]) * ed

        with self.canvas:
            Color(1, 1, 1)
            x = -1600
            self.y_axis = Line(points=[350, 1000, 350, 0], width=2)  # отрисовка оси абцисс
            self.x_axis = Line(points=[0, 220, 1000, 220], width=2)  # отрисовка оси ординат
            self.unit_segment_x_negative = Line(points=[300, 260, 300, 180])  # отрисовка 1-го единичного отрезка, где x < 0
            self.unit_segment_x_positive = Line(points=[400, 260, 400, 180])  # отрисовка 1-го единичного отрезка, где x > 0
            self.hyperb = Line(points=[x, k/x], width=2)
            for x in range(1, 1600):
                y1 = k/x
                self.hyperb.points += [x + 350, y1 + 220]

            for x in range(-1600, -1):
                y1 = k/x
                self.hyperb.points += [x + 350, y1 + 220]

