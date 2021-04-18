import json

from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition
from kivy.gesture import GestureDatabase, Gesture

from gallery.stage import StageLayout
from gallery.overview import OverviewScrollView

gesture_db = GestureDatabase()
gesture_string = json.load(open('gallery/gesture_string.json', 'rb'))
for name, gs in gesture_string.items():
    gesture = gesture_db.str_to_gesture(gs)
    gesture.name = name
    gesture_db.add_gesture(gesture)

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

        for name in gesture_string:
            self.register_event_type(f'on_{name}')

    def on_bottom_to_top_line(self):
        print('upupupup')

    def on_top_to_bottom_line(self):
        print('downdown')

    def on_touch_down(self, touch):
        touch.ud['gesture_path'] = [(touch.x, touch.y)]
        super(MyScreenManager, self).on_touch_down(touch)
    
    def on_touch_move(self, touch):
        try:
            touch.ud['gesture_path'].append((touch.x, touch.y))
        except KeyError:
            print('KeyError has excepted')
        super(MyScreenManager, self).on_touch_move(touch)
    
    def on_touch_up(self, touch):
        if 'gesture_path' in touch.ud:
            gesture = Gesture()
            gesture.add_stroke(touch.ud['gesture_path'])
            gesture.normalize()
            match = gesture_db.find(gesture, minscore=0.7)
            if match:
                print(f'on_{match[1].name}')
                self.dispatch(f'on_{match[1].name}')
        super(MyScreenManager, self).on_touch_up(touch)