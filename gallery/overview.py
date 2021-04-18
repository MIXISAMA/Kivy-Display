from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.properties import ObjectProperty
from kivy.uix.stencilview import StencilView

from gallery.database import clean_data

class OverviewScrollView(ScrollView):
    grid_layout: ObjectProperty()
    def __init__(self):
        super(OverviewScrollView, self).__init__()
        for d in clean_data:
            if not d['media']:
                continue
            self.grid_layout.add_widget(
                OverviewButton(d['name'], d['media'][0]['url'])
            )

class OverviewButton(Button, StencilView):
    image = ObjectProperty()
    def __init__(self, name, url):
        super(OverviewButton, self).__init__()
        self.text = name
        self.image.source = url
