import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.progressbar import ProgressBar
from kivy.clock import Clock
import threading

class NeonBuildManager(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=40, spacing=20)
        
        self.header = Label(text="NEON PRO: Build Manager", font_size='24sp', bold=True)
        self.layout.add_widget(self.header)
        
        self.progress_bar = ProgressBar(max=100, value=0, size_hint_y=None, height=40)
        self.layout.add_widget(self.progress_bar)
        
        self.status_label = Label(text="System IDLE", font_size='18sp')
        self.layout.add_widget(self.status_label)
        
        self.start_btn = Button(text="START COMPILATION (.APK & .EXE)", size_hint_y=None, height=70)
        self.start_btn.bind(on_press=self.start_build_process)
        self.layout.add_widget(self.start_btn)
        
        return self.layout

    def start_build_process(self, instance):
        self.start_btn.disabled = True
        threading.Thread(target=self.run_build_logic).start()

    def run_build_logic(self):
        # Simulation of Buildozer and PyInstaller stages
        stages = ["Configuring SDK", "Compiling Python Bytecode", "Packing Assets", "Signing APK", "Building EXE"]
        for i, stage in enumerate(stages):
            for p in range(0, 101, 20):
                Clock.schedule_once(lambda dt, s=stage, prog=p: self.update_status(s, prog))
                import time
                time.sleep(0.5)
        
        Clock.schedule_once(lambda dt: self.final_step())

    def update_status(self, stage, prog):
        self.status_label.text = f"Stage: {stage}... {prog}%"
        self.progress_bar.value = ((stages_index(stage) * 100) + prog) / 5
        
    def final_step(self):
        self.status_label.text = "Success! .APK & .EXE Ready in /builds folder."

# Helper to track stages
def stages_index(s):
    return ["Configuring SDK", "Compiling Python Bytecode", "Packing Assets", "Signing APK", "Building EXE"].index(s)

if __name__ == "__main__":
    NeonBuildManager().run()
