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
from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.tab import MDTabsBase
from kivymd.icon_definitions import md_icons
from classes import straight, menu_screen, lin_function, draw_linear_function, sq_function, draw_square_function


class FunctionApp(MDApp):
    txt = ObjectProperty()

    def build(self):
        self.theme_cls.theme_style = "Dark"
        sm = ScreenManager()
        sm.add_widget(menu_screen.MenuScreen(name='menu'))
        sm.add_widget(lin_function.LinearFunction(name='linear_function'))
        sm.add_widget(sq_function.SquareFunction(name='square_function'))
        sm.add_widget(draw_linear_function.DrawLinearFunctionScreen(name='line'))
        sm.add_widget(draw_square_function.DrawSquareFunction(name='parabola'))
        Window.size = (700, 500)
        return sm


if __name__ == '__main__':
    FunctionApp().run()
