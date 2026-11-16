from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class InderSinghApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        layout.add_widget(Label(text="Inder Singh Investment Portfolio", font_size='24sp'))
        layout.add_widget(Label(text="Total Assets: ₹15,00,000", font_size='20sp'))
        layout.add_widget(Button(text="View Portfolio", size_hint=(1, 0.2)))
        layout.add_widget(Button(text="Add Transaction", size_hint=(1, 0.2)))
        return layout

if __name__ == '__main__':
    InderSinghApp().run()
