import pyttsx3
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

class NeonProVoice(MDApp):
    def build(self):
        self.engine = pyttsx3.init()
        return MDLabel(text="Voice Engine Active: Harish, I am here!", halign="center")

    def on_start(self):
        self.engine.say("Hello Harish, main sun sakta hoon aur ab bol bhi paunga.")
        self.engine.runAndWait()

if __name__ == "__main__":
    NeonProVoice().run()
