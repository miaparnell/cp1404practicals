from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

KILOMETRE_CONVERSION = 1.60934


class ConvertMilesKmApp(App):
    output_km = StringProperty()

    def build(self):
        """Build the Kivy app from the kv file."""
        Window.size = (300, 200)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    @staticmethod
    def convert_to_number(text):
        """Convert text to float or 0.0 if invalid."""
        try:
            return float(text)
        except ValueError:
            return 0.0

    def handle_conversion(self, text):
        """Update the value in miles after it has been converted."""
        miles = self.convert_to_number(text)
        self.update_result(miles)

    def handle_increment(self, text, change):
        """Add or subtract 1 based on the button that is pressed."""
        miles = self.convert_to_number(text) + change
        self.root.ids.input_miles.text = str(miles)

    def update_result(self, miles):
        """Update result once miles have been converted."""
        self.output_km = str(miles * KILOMETRE_CONVERSION)


ConvertMilesKmApp().run()
