from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from moviepy.editor import TextClip, CompositeVideoClip

class NeonVideoApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.input = TextInput(hint_text='Enter text here...')
        btn = Button(text='Generate Video', on_press=self.generate)
        layout.add_widget(self.input)
        layout.add_widget(btn)
        return layout

    def generate(self, instance):
        text = self.input.text
        clip = TextClip(text, fontsize=50, color='white', size=(720, 1280))
        clip.set_duration(3).write_videofile("output.mp4", fps=24)

if __name__ == '__main__':
    NeonVideoApp().run()
