"""
CP1404/CP5632 Practical
Kivy GUI program to square a number
Lindsay Ward, IT@JCU
Started 13/10/2015
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = 'Lindsay Ward'


class SquareNumberApp(App):
    """SquareNumberApp is a Kivy App for squaring a number."""

    def build(self):
        """Build the Kivy app from the kv file."""
        Window.size = (300, 150)  # Adjusted size for better UI
        self.title = "Square Number"
        self.root = Builder.load_file('squaring.kv')
        return self.root

    def handle_calculate(self, value):
        """Handle calculation, output result to label widget."""
        try:
            number = self.validate_input(value)
            result = number ** 2
            self.root.ids.output_label.text = str(result)
        except ValueError:
            self.root.ids.output_label.text = "Invalid input"

    def handle_clear(self):
        """Clear the input and output fields."""
        self.root.ids.input_number.text = ""
        self.root.ids.output_label.text = ""

    @staticmethod
    def validate_input(value):
        """Validate the input; return 0.0 if invalid."""
        try:
            return float(value)
        except ValueError:
            return 0.0

SquareNumberApp().run()
