from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager


class MenuScreen(Screen):
    pass


class LinearFunction(Screen):
    pass



class FunctionApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(LinearFunction(name='linear_function'))
        Window.size = (700,500)
        return sm


if __name__ == '__main__':
    FunctionApp().run()
