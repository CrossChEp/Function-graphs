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


class Parabola(Widget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def draw(self):
        db = open('db.txt', 'r')
        coords = list(db.read().split())
        db.close()
        ed = 50  # 1 единица отрезка
        a = int(coords[0])
        b = int(coords[1])
        c = int(coords[2])
        with self.canvas:

            self.y_axis = Line(points=[350, 1000, 350, 0], width=2)  # отрисовка оси абцисс
            self.x_axis = Line(points=[0, 220, 1000, 220], width=2)  # отрисовка оси ординат
            self.unit_segment_x_negative = Line(points=[300, 260, 300, 180])  # отрисовка 1-го единичного отрезка, где x < 0
            self.unit_segment_x_positive = Line(points=[400, 260, 400, 180])  # отрисовка 1-го единичного отрезка, где x > 0

            x_v = -b / 2 * a  # x вершины
            y_v = a * x_v ** 2 + b * x_v + c  # y вершины
            x_v *= ed  # конвертируем в пиксели
            y_v *= ed
            low = -1600  # минимальная точка
            high = 1600  # максимальная точка

            # отрисовка пораболы
            if a < 0:
                # Возрастает
                for x in range(low, int(x_v)):
                    for y in range(low, int(y_v)):
                        self.line = Ellipse(pos=(x,y))
                        low -= 1
                        break
                # Убывает
                for x in range(int(x_v), high):
                    for y in range(int(y_v), high):
                        self.line = Ellipse(pos=(x,y))
                        y_v += 1
                        x_v += 1
                        break
