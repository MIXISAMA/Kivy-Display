from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.image import AsyncImage
from kivy.properties import ObjectProperty
from gallery.database import clean_data

class StageLayout(AnchorLayout):
    carousel = ObjectProperty()
    def __init__(self):
        super(StageLayout, self).__init__()
        for d in clean_data:
            for m in d['media']:
                image = AsyncImage(source=m['url'], allow_stretch=True)
                self.carousel.add_widget(image)
