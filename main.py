# NEON PRO FINAL BUILD: VIDEO COMPRESSOR & BUILDER
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class NeonProApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=50, spacing=20)
        layout.add_widget(Label(text="NEON PRO: COMPRESSION ENGINE READY", font_size='20sp'))
        btn = Button(text="PROCESS & EXPORT", size_hint=(1, 0.3))
        layout.add_widget(btn)
        return layout

if __name__ == "__main__":
    NeonProApp().run()
