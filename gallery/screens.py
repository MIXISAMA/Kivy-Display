from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition

from gallery.stage import StageLayout
from gallery.overview import OverviewScrollView
class MyScreen(Screen):
    content = ObjectProperty()
    
    def __init__(self, name, content):
        super(MyScreen, self).__init__(name=name)
        self.content.add_widget(content)


class MyScreenManager(ScreenManager):
    transition = FadeTransition()

    def __init__(self):
        super(MyScreenManager, self).__init__()
        # self.overview_screen = MyScreen('overview')
        # self.stage_screen = MyScreen('stage')

        self.add_widget(MyScreen('overview', OverviewScrollView()))
        self.add_widget(MyScreen('stage', StageLayout()))
        self.current = 'overview'
