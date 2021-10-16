from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager


class MainContainer(BoxLayout):
    pass

class MenuScreen(Screen):
    pass

class FunctionApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        Window.size = (700,500)
        return sm


if __name__ == '__main__':
    FunctionApp().run()
