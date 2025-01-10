import os
import numpy as np
from PIL import Image, ImageFont, ImageDraw


class Renderer:
    BLACK = 0
    WHITE = 255
    PRINTABLE_ASCII_CHARACTERS = [chr(i) for i in range(32, 127)]

    def __init__(self, font_path: str, font_size: int, image_size: tuple[int, int], output_path: str) -> None:
        self.font: ImageFont.FreeTypeFont | ImageFont.ImageFont

        try:
            self.font = ImageFont.truetype(font_path, font_size)
        except IOError:
            # Fallback to default font if font file is not available
            self.font = ImageFont.load_default(font_size)
            print(f"Could not load font from path: '{font_path}'. Using default font instead.")

        self.font_size = font_size
        self.image_size = image_size
        self.output_path = output_path

    def _render_character(self, character: str) -> np.ndarray:
        # Create a new 1-bit image with a black background
        image = Image.new("1", self.image_size, color=self.BLACK)

        # Creates an object that can be used to draw on the given image
        draw = ImageDraw.Draw(image)

        # Draw the character in white in the certer of the image
        draw.text(xy=(self.image_size[0] // 2, self.image_size[1] // 2), text=character, fill=self.WHITE, font=self.font, align="center", anchor="mm")

        # Convert the image to a numpy array of 1-bit values and return it
        return np.array(image)

    def _calculate_luminance(self, image: np.ndarray) -> float:
        # Calculate the average luminance of the image using the average since 1-bit images only have 0 and 1 values
        return np.mean(image)

    def calculate_luminance_of_printable_characters(self) -> dict[str, float]:
        # Iterate through each printable ASCII character and calculate its luminance value
        luminance_values = {}

        for c in self.PRINTABLE_ASCII_CHARACTERS:
            luminance_values[c] = self._calculate_luminance(self._render_character(c))

        return luminance_values

    def save_characters(self) -> None:
        if isinstance(self.font, ImageFont.FreeTypeFont):
            font_name = self.font.getname()[0]
            font_style = self.font.getname()[1]
        else:
            font_name = "Aileron"
            font_style = "Regular"

        named_output_path = os.path.join(self.output_path, f"{font_name} {font_style}")

        # Create the output directory if it does not exist
        if not os.path.exists(named_output_path):
            os.makedirs(named_output_path)

        # Iterate through each printable ASCII character and save the rendered image
        for c in self.PRINTABLE_ASCII_CHARACTERS:
            Image.fromarray(self._render_character(c)).save(os.path.join(named_output_path, f"{ord(c)}.png"))
