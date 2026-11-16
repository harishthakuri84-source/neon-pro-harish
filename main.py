import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button

class VetAIDoctor(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        self.layout.add_widget(Label(text="NEON PRO: VET-AI DOCTOR", font_size='22sp', bold=True))
        
        self.user_input = TextInput(hint_text="Janwar ki pareshani yahan likho ya bolo...", multiline=True, height=100)
        self.layout.add_widget(self.user_input)
        
        self.result_label = Label(text="AI Doctor abhi ready hai, apni pareshani batayein.", text_size=(300, None))
        self.layout.add_widget(self.result_label)
        
        self.check_btn = Button(text="DIAGNOSE KAREIN", size_hint_y=0.2, background_color=(0, 1, 0, 1))
        self.check_btn.bind(on_press=self.analyze_symptoms)
        self.layout.add_widget(self.check_btn)
        
        return self.layout

    def analyze_symptoms(self, instance):
        # Yahan main Veterinary Database ka logic integrate kar raha hoon
        symptom = self.user_input.text.lower()
        if "bukhar" in symptom or "fever" in symptom:
            self.result_label.text = "Symptom: Bukhar\nDiagnosis: FMD (Foot and Mouth Disease) ho sakta hai.\nAdvice: Turant doctor ko dikhayein aur isolation mein rakhein."
        else:
            self.result_label.text = "Data analyze ho raha hai... Veterinary database se check kar raha hoon."

if __name__ == "__main__":
    VetAIDoctor().run()
