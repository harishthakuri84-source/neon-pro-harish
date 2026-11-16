from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField

class VideoGenerator(MDApp):
    def build(self):
        screen = MDScreen()
        self.input = MDTextField(hint_text="Enter text for video", pos_hint={'center_x': 0.5, 'center_y': 0.6})
        btn = MDRaisedButton(text="Generate Video", pos_hint={'center_x': 0.5, 'center_y': 0.4}, on_release=self.start_process)
        screen.add_widget(self.input)
        screen.add_widget(btn)
        return screen

    def start_process(self, instance):
        print("Starting video synthesis...")

VideoGenerator().run()
