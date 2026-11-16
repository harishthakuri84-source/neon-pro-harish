import kivy
from kivy.app import App
from kivy.uix.label import Label
import speech_recognition as sr
import pyttsx3

class NeonVoiceApp(App):
    def build(self):
        self.engine = pyttsx3.init()
        return Label(text="NEON PRO: Voice Active... Bol bhai!")

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

if __name__ == '__main__':
    NeonVoiceApp().run()
