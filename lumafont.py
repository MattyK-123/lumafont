import argparse
from renderer import Renderer

def main(args):
    pass


if __name__ == "__main__":
    # Initialize the argument parser
    parser = argparse.ArgumentParser(description="Lumafont - A tool for rendering ASCII characters and calculating luminance values.")
    parser.add_argument("-f", "--font", type=str, required=True, help="path to the font file to be used for rendering ASCII characters")
    parser.add_argument("-s", "--size", type=int, default=16, help="font size to be used for rendering ASCII characters (default is 16)")
    parser.add_argument("-o", "--output", type=str, default=None, help="path to save the luminance report (if not provided, the data will be printed to the console)")
    parser.add_argument("-v", "--verbose", action="store_true", help="enable verbose output for additional details during execution")
    parser.add_argument("-t", "--type", type=str, choices=["png", "jpeg", "jpg"], default="png", help="output image type (default is PNG)")
    args = parser.parse_args()

    main(args)
