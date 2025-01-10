import os
import argparse
import lumafont

def main(args):
    args.font_file = os.path.normpath(args.font_file)
    args.output_directory = os.path.normpath(args.output_directory)

    renderer = lumafont.Renderer(font_path=args.font_file, font_size=args.font_size, image_size=args.image_size, output_path=args.output_directory)
    reporter = lumafont.Reporter(renderer=renderer, pretty_print=args.pretty_print)

    if not args.disable_output:
        renderer.save_characters()
        reporter.save_luminance_report()

    if not args.pretty_print:
        print(reporter._get_luminance_report())
    else:
        print(reporter._get_pretty_luminance_report())


if __name__ == "__main__":
    # Initialize the argument parser
    parser = argparse.ArgumentParser(description="Lumafont - A tool for rendering ASCII characters and calculating luminance values.")
    parser.add_argument("-f", "--font-file", type=str, required=True, help="path to the font file to be used for rendering ASCII characters")
    parser.add_argument("-s", "--font-size", type=int, default=256, help="font size to be used for rendering ASCII characters (default is 256)")
    parser.add_argument("-i", "--image-size", type=int, nargs=2, metavar=("width", "height"), default=(500, 500), help="size of the output image in pixels (default is 500x500)")
    parser.add_argument("-o", "--output-directory", type=str, default=".\\", help="path to save the luminance report and rendered images to (if not provided, the current directory will be used)")
    parser.add_argument("-d", "--disable-output", action="store_true", help="disable saving the rendered images and luminance report")
    parser.add_argument("-p", "--pretty-print", action="store_true", help="pretty print the luminance report")
    args = parser.parse_args()

    main(args)
