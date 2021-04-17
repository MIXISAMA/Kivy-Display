import kivy
kivy.require('2.0.0')
from kivy.app import App
from kivy.properties import ObjectProperty

from gallery.screens import MyScreenManager

class MyApp(App):
    # mgr = ObjectProperty()

    def build(self):
        return MyScreenManager()