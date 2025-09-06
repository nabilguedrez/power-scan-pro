from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.recycleview import RecycleView
from kivy.uix.recyclegridlayout import RecycleGridLayout
from kivy.core.window import Window

# تغيير خلفية التطبيق
Window.clearcolor = (0.15, 0.15, 0.2, 1)  # لون غامق

class PowerScan(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", spacing=10, padding=10, **kwargs)

        # --- لوحة التحكم ---
        controls = BoxLayout(size_hint=(1, 0.15), spacing=10, padding=5)
        self.start_btn = Button(text="▶ Start", background_color=(0.2, 0.6, 0.2, 1))
        self.start_btn.bind(on_press=self.start_scan)
        self.stop_btn = Button(text="■ Stop", background_color=(0.8, 0.2, 0.2, 1))
        self.stop_btn.bind(on_press=self.stop_scan)
        controls.add_widget(self.start_btn)
        controls.add_widget(self.stop_btn)
        self.add_widget(controls)

        # --- إدخال المعطيات ---
        params = GridLayout(cols=2, size_hint=(1, 0.2), padding=5, spacing=5)
        params.add_widget(Label(text="Bots:", color=(1,1,1,1)))
        self.bots_input = TextInput(text="5", multiline=False)
        params.add_widget(self.bots_input)
        params.add_widget(Label(text="Min Exp Days:", color=(1,1,1,1)))
        self.days_input = TextInput(text="7", multiline=False)
        params.add_widget(self.days_input)
        self.add_widget(params)

        # --- رأس الجدول ---
        header = GridLayout(cols=5, size_hint=(1, 0.1), spacing=5)
        for title in ["MAC Address", "Expires", "Days", "Info", "TV"]:
            header.add_widget(Label(text=title, bold=True, color=(0.9,0.9,0.2,1)))
        self.add_widget(header)

        # --- جدول النتائج ---
        self.result = RecycleView(size_hint=(1, 0.55))
        self.result.viewclass = "Label"
        self.result.layout_manager = RecycleGridLayout(cols=5, default_size=(None, 40), size_hint_y=None)
        self.result.layout_manager.bind(minimum_height=self.result.setter("height"))
        self.add_widget(self.result)

    def start_scan(self, instance):
        days = self.days_input.text
        # بيانات تجريبية
        data = [
            {"text": "00:11:22:33:44:55", "color": (1,1,1,1)},
            {"text": "2025-09-10", "color": (1,1,1,1)},
            {"text": days, "color": (0.6,1,0.6,1)},
            {"text": "OK", "color": (0.6,1,0.6,1)},
            {"text": "Yes", "color": (0.6,1,0.6,1)},

            {"text": "66:77:88:99:AA:BB", "color": (1,1,1,1)},
            {"text": "2025-09-12", "color": (1,1,1,1)},
            {"text": str(int(days)+2), "color": (1,0.8,0.6,1)},
            {"text": "Active", "color": (1,0.8,0.6,1)},
            {"text": "No", "color": (1,0.8,0.6,1)},
        ]
        self.result.data = data

    def stop_scan(self, instance):
        self.result.data = [{"text": "Stopped", "color": (1,0.5,0.5,1)}]


class PowerScanApp(App):
    def build(self):
        return PowerScan()


if __name__ == "__main__":
    PowerScanApp().run()
