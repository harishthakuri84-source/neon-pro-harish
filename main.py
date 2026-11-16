from kivy.app import App
from kivy.uix.label import Label

class NeonApp(App):
    def build(self):
        return Label(text="Sab set hai, Harish! \nSimple aur solid.")

if __name__ == "__main__":
    NeonApp().run()
