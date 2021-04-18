from kivy.app import App
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.lang.builder import Builder
from kivy.clock import Clock


class CLS_PROGRESS_BAR(FloatLayout):
    background = StringProperty(None)
    progress_image = StringProperty(None)
    max = NumericProperty(0.0)

    def __init__(self, font_size=20, **kwargs):
        super(CLS_PROGRESS_BAR, self).__init__(**kwargs)
        self.progress_event = None
        self.font_size = font_size
        self.firstDraw = True
        self.pbi = None
        self.rect = None
        self.bgi = None
        self.value = 0.0
        self.value_normalized = 0.0

        self.progress_event = Clock.schedule_interval(self._progress, 0.5)

    def draw(self):
        if self.firstDraw:
            self.ids.bgi.source=self.background
            self.ids.pbi.source = self.progress_image
            self.ids.lab.font_size = self.font_size
            self.ids.lab.text = str(int(self.value_normalized*100)) + "%"
            self.ids.sten.width = self.size[0]*self.value_normalized
            self.firstDraw = False
        else:
            self.ids.lab.text = str(int(self.value_normalized*100)) + "%"
            self.ids.sten.width = self.size[0]*self.value_normalized

    def set_value(self, value):
        self.value = value
        self.value_normalized = self.value / self.max
        self.draw()

    def _progress(self, dt):
        if self.value < self.max - 1:
            self.set_value(self.value + 1)
        else:
            self.set_value(self.max)
            self.progress_event.cancel()


# Demo
class Main(App):

    def build(self):
        container = Builder.load_string(
            '''
<CLS_PROGRESS_BAR>:
    Image:
        id: bgi
        allow_stretch: True
        keep_ratio: False
    StencilView:
        id: sten
        size_hint: (None, None)
        size: (0, root.height)
        Image:
            id: pbi
            allow_stretch: True
            keep_ratio: False
            size_hint: (None, None)
            size: (root.width, lab.height)
            pos: (root.pos[0], root.pos[1] + (root.height - lab.height)/2.0)
    Label:
        id: lab
        text: '0%'
        size_hint: (None, None)
        size: self.texture_size
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}

CLS_PROGRESS_BAR:
    size_hint: (None, None)
    height: 100
    width: 500
    max: 100
    background: 'fakedata/test4.jpeg'
    progress_image: 'fakedata/test5.jpeg'
    ''')

        return container

if __name__ == '__main__':
    Main().run()