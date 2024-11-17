from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class ConvertingApp(App):
    """Kivy app for converting miles to kilometers."""
    output = StringProperty()

    def build(self):
        """Build the Kivy app."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.output = "0.0 km"  # Initialize output with default text
        return self.root

    def handle_calculate(self, text):
        """Handle the calculation of miles to kilometers."""
        number = self.validating_values(text)
        result = number * MILES_TO_KM
        self.output = f"{result:.2f} km"

    def handle_increment(self, text, change):
        """Handle increment or decrement of the input value."""
        number = self.validating_values(text) + change
        self.root.ids.input_number.text = str(number)
        self.handle_calculate(str(number))  # Automatically update the result after increment

    def validating_values(self, text):
        """Validate the input value and convert it to float."""
        try:
            return float(text)
        except ValueError:
            return 0.0

ConvertingApp().run()
