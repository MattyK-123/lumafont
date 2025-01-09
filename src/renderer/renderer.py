import numpy as np
from PIL import ImageFont


class Renderer:
    def __init__(self, font_path: str, font_size: int) -> None:
        self.font = ImageFont.truetype(font_path, font_size)
        self.font_size = font_size
