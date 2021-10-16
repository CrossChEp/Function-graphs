from kivy.app import App
from kivy.core.window import Window
from kivy.lang.builder import Instruction
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.graphics import Line


class Straight(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.line = Line(points=[10, 0, 6, 10]) #x1,y1,x2,y2
        self.canvas.add(self.line)


class MenuScreen(Screen):
    pass


class LinearFunction(Screen):
    pass


class DrawLinearFunctionScreen(Screen):

    def __init__(self, **kw):
        super().__init__(**kw)
        self.straight_line = Straight()
        self.add_widget(self.straight_line)


class FunctionApp(App):
    txt = ObjectProperty()

    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(LinearFunction(name='linear_function'))
        sm.add_widget(DrawLinearFunctionScreen(name='line'))
        Window.size = (700,500)
        return sm


if __name__ == '__main__':
    FunctionApp().run()
