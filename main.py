from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.animation import Animation
from kivymd.uix.screen import MDScreen

class NavScreen(MDScreen):
    Builder.load_file('nav.kv')
    def selected(self, ico):
        anim = Animation(pos = (self.ids[ico].center[0]-12, self.ids[ico].center[1]-54), duration = 0.08)
        anim.start(self.ids.dot)
        for i in range(4):
            self.ids[f'ico{i}'].text_color= (0.7,0.7,0.7,1)
        self.ids[ico].text_color = (1,0,1,1)
        
class MainApp(MDApp):
    def build(self):
        return NavScreen()
        
MainApp().run()