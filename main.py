from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class MainContainer(BoxLayout):
    pass


class LogoApp(App):
    def build(self):
        return MainContainer()


if __name__ == '__main__':
    LogoApp().run()
