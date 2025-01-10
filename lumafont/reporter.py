import os
import csv
import numpy as np
from PIL import ImageFont
from .renderer import Renderer
from prettytable import PrettyTable


class Reporter:
    def __init__(self, renderer: Renderer, pretty_print: bool) -> None:
        self.font = renderer.font
        self.output_path = renderer.output_path
        self.luminance_values: dict[str, float] = renderer.calculate_luminance_of_printable_characters()

    def _get_luminance_report(self) -> str:
        # Print the luminance values of each character in a CSV format
        out_string = "Character, Luminance\n"

        for char, luminance in self.luminance_values.items():
            out_string += f"{char}, {"{:.5f}".format(luminance)}\n"

        return out_string

    def _get_pretty_luminance_report(self) -> str:
        # Pretty print the luminance values of each character into a table
        table = PrettyTable()
        table.field_names = ["Character", "Luminance"]

        for char, luminance in self.luminance_values.items():
            table.add_row([char, "{:.5f}".format(luminance)])

        return str(table)

    def save_luminance_report(self) -> None:
        # Save the luminance values of each character to a CSV file
        if isinstance(self.font, ImageFont.FreeTypeFont):
            font_name = self.font.getname()[0]
            font_style = self.font.getname()[1]
        else:
            font_name = "Aileron"
            font_style = "Regular"

        named_output_path = os.path.join(self.output_path, f"{font_name} {font_style}")

        # Create the output directory if it does not exist
        if not os.path.exists(named_output_path):
            os.mkdir(named_output_path)

        named_outputfile = os.path.join(named_output_path, "luminance_report.csv")

        with open(named_outputfile, "w", newline="\n") as file:
            csv_file = csv.DictWriter(file, fieldnames=["Character", "Luminance"], quoting=csv.QUOTE_NONE, delimiter="\t", escapechar="\\")
            csv_file.writeheader()
            
            for char, luminance in self.luminance_values.items():
                csv_file.writerow({"Character": char, "Luminance": "{:.5f}".format(luminance)})