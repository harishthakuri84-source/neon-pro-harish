from kivy.app import App
from kivy.uix.spinner import Spinner
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class VetMasterApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        layout.add_widget(Label(text="Select Animal Species", font_size='20sp'))
        
        self.species = Spinner(
            text='Select',
            values=('Dog', 'Cat', 'Sheep', 'Goat', 'Buffalo', 'Horse', 'Cow'),
        )
        layout.add_widget(self.species)
        
        self.btn = Button(text="Consult AI Doctor", on_press=self.get_advice)
        layout.add_widget(self.btn)
        
        self.result = Label(text="Selection ka wait kar raha hoon...")
        layout.add_widget(self.result)
        return layout

    def get_advice(self, instance):
        animal = self.species.text
        self.result.text = f"Analyzing {animal} health database...\nSearching for common symptoms..."

if __name__ == "__main__":
    VetMasterApp().run()
