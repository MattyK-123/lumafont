# Lumafont

**Lumafont** is a Python application designed to process user-provided fonts to render all ASCII characters and calculate their luminance values. This tool is ideal for developers, graphic designers, and enthusiasts who are interested in:

- Analyzing typography.
- Creating ASCII art.
- Utilizing luminance data for creative projects like visualizations or games.

## Features

- **Font Rendering**: Generates images for all printable ASCII characters using a specified font.
- **Luminance Calculation**: Computes the average luminance for each rendered character.
- **Pretty Reports**: Outputs luminance data in both raw CSV format and a visually pleasing table.
- **Customizable Output**: Allows for configuration of font size, image size, and output directory.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/MattyK-123/lumafont.git
   cd lumafont
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the `lumafont.py` script with the following options:

```bash
python lumafont.py -f <font-file-path> [-s <font-size>] [-i <width> <height>] [-o <output-directory>] [-d] [-p]
```

### Arguments:

- `-f, --font-file`: Path to the font file to use for rendering (required).
- `-s, --font-size`: Font size to use (default: 256).
- `-i, --image-size`: Dimensions of the rendered image in pixels (default: 500x500).
- `-o, --output-directory`: directory to save output files (default: current directory).
- `-d, --disable-output`: Disable saving the rendered images and luminance report.
- `-p, --pretty-print`: Print the luminance report as a table instead of CSV.

### Example:

Render ASCII characters using `Arial.ttf`, save outputs to `./outputs`, and pretty print the luminance report:

```bash
python lumafont.py -f fonts/arial.ttf -o .\output -i 64 64 -s 16
```

### Example Output:

```bash
+-----------+-----------+
| Character | Luminance |
+-----------+-----------+
|           |  0.00000  |
|     !     |  0.01245  |
|     "     |  0.01074  |
|     #     |  0.05029  |
|     $     |  0.04688  |
|     %     |  0.05200  |
|     &     |  0.04517  |
|     '     |  0.00537  |
|     (     |  0.01904  |
|     )     |  0.01904  |
|     *     |  0.01172  |
|     +     |  0.01978  |
|     ,     |  0.00439  |
|     -     |  0.00659  |
|     .     |  0.00220  |
|     /     |  0.01172  |
|     0     |  0.04102  |
|     1     |  0.02075  |
|     2     |  0.03418  |
|     3     |  0.03662  |
|     4     |  0.03491  |
|     5     |  0.04053  |
|     6     |  0.04419  |
|     7     |  0.02515  |
|     8     |  0.04321  |
|     9     |  0.04321  |
|     :     |  0.00439  |
|     ;     |  0.00659  |
|     <     |  0.01978  |
|     =     |  0.02197  |
|     >     |  0.01978  |
|     ?     |  0.02563  |
|     @     |  0.09985  |
|     A     |  0.03906  |
|     B     |  0.05322  |
|     C     |  0.03931  |
|     D     |  0.04810  |
|     E     |  0.04321  |
|     F     |  0.03442  |
|     G     |  0.04932  |
|     H     |  0.04175  |
|     I     |  0.01685  |
|     J     |  0.02368  |
|     K     |  0.04126  |
|     L     |  0.02490  |
|     M     |  0.06372  |
|     N     |  0.04712  |
|     O     |  0.04590  |
|     P     |  0.04077  |
|     Q     |  0.05078  |
|     R     |  0.04907  |
|     S     |  0.04321  |
|     T     |  0.02856  |
|     U     |  0.03833  |
|     V     |  0.03491  |
|     W     |  0.06543  |
|     X     |  0.03662  |
|     Y     |  0.02856  |
|     Z     |  0.04175  |
|     [     |  0.02563  |
|     \     |  0.01172  |
|     ]     |  0.02563  |
|     ^     |  0.01465  |
|     _     |  0.01392  |
|     `     |  0.00342  |
|     a     |  0.03613  |
|     b     |  0.03784  |
|     c     |  0.02539  |
|     d     |  0.03760  |
|     e     |  0.03271  |
|     f     |  0.02271  |
|     g     |  0.04517  |
|     h     |  0.03442  |
|     i     |  0.01465  |
|     j     |  0.02051  |
|     k     |  0.03345  |
|     l     |  0.01685  |
|     m     |  0.04541  |
|     n     |  0.02979  |
|     o     |  0.03027  |
|     p     |  0.03784  |
|     q     |  0.03809  |
|     r     |  0.01660  |
|     s     |  0.03247  |
|     t     |  0.02173  |
|     u     |  0.02954  |
|     v     |  0.02222  |
|     w     |  0.03979  |
|     x     |  0.02344  |
|     y     |  0.02905  |
|     z     |  0.03052  |
|     {     |  0.02563  |
|     |     |  0.01465  |
|     }     |  0.02515  |
|     ~     |  0.01245  |
+-----------+-----------+
```
## Sample Images

Here are some sample images rendered using the Arial Regular font:

![Character 32](./output/Arial%20Regular/32.png)
![Character 33](./output/Arial%20Regular/33.png)
![Character 34](./output/Arial%20Regular/34.png)
![Character 35](./output/Arial%20Regular/35.png)
![Character 36](./output/Arial%20Regular/36.png)
![Character 37](./output/Arial%20Regular/37.png)
![Character 38](./output/Arial%20Regular/38.png)
![Character 39](./output/Arial%20Regular/39.png)
![Character 40](./output/Arial%20Regular/40.png)
![Character 41](./output/Arial%20Regular/41.png)
![Character 42](./output/Arial%20Regular/42.png)
![Character 43](./output/Arial%20Regular/43.png)
![Character 44](./output/Arial%20Regular/44.png)
![Character 45](./output/Arial%20Regular/45.png)
![Character 46](./output/Arial%20Regular/46.png)
![Character 47](./output/Arial%20Regular/47.png)
![Character 48](./output/Arial%20Regular/48.png)
![Character 49](./output/Arial%20Regular/49.png)
![Character 50](./output/Arial%20Regular/50.png)
![Character 51](./output/Arial%20Regular/51.png)
![Character 52](./output/Arial%20Regular/52.png)
![Character 53](./output/Arial%20Regular/53.png)
![Character 54](./output/Arial%20Regular/54.png)
![Character 55](./output/Arial%20Regular/55.png)
![Character 56](./output/Arial%20Regular/56.png)
![Character 57](./output/Arial%20Regular/57.png)
![Character 58](./output/Arial%20Regular/58.png)
![Character 59](./output/Arial%20Regular/59.png)
![Character 60](./output/Arial%20Regular/60.png)
![Character 61](./output/Arial%20Regular/61.png)
![Character 62](./output/Arial%20Regular/62.png)
![Character 63](./output/Arial%20Regular/63.png)
![Character 64](./output/Arial%20Regular/64.png)
![Character 65](./output/Arial%20Regular/65.png)
![Character 66](./output/Arial%20Regular/66.png)
![Character 67](./output/Arial%20Regular/67.png)
![Character 68](./output/Arial%20Regular/68.png)
![Character 69](./output/Arial%20Regular/69.png)
![Character 70](./output/Arial%20Regular/70.png)
![Character 71](./output/Arial%20Regular/71.png)
![Character 72](./output/Arial%20Regular/72.png)
![Character 73](./output/Arial%20Regular/73.png)
![Character 74](./output/Arial%20Regular/74.png)
![Character 75](./output/Arial%20Regular/75.png)
![Character 76](./output/Arial%20Regular/76.png)
![Character 77](./output/Arial%20Regular/77.png)
![Character 78](./output/Arial%20Regular/78.png)
![Character 79](./output/Arial%20Regular/79.png)
![Character 80](./output/Arial%20Regular/80.png)
![Character 81](./output/Arial%20Regular/81.png)
![Character 82](./output/Arial%20Regular/82.png)
![Character 83](./output/Arial%20Regular/83.png)
![Character 84](./output/Arial%20Regular/84.png)
![Character 85](./output/Arial%20Regular/85.png)
![Character 86](./output/Arial%20Regular/86.png)
![Character 87](./output/Arial%20Regular/87.png)
![Character 88](./output/Arial%20Regular/88.png)
![Character 89](./output/Arial%20Regular/89.png)
![Character 90](./output/Arial%20Regular/90.png)
![Character 91](./output/Arial%20Regular/91.png)
![Character 92](./output/Arial%20Regular/92.png)
![Character 93](./output/Arial%20Regular/93.png)
![Character 94](./output/Arial%20Regular/94.png)
![Character 95](./output/Arial%20Regular/95.png)
![Character 96](./output/Arial%20Regular/96.png)
![Character 97](./output/Arial%20Regular/97.png)
![Character 98](./output/Arial%20Regular/98.png)
![Character 99](./output/Arial%20Regular/99.png)
![Character 100](./output/Arial%20Regular/100.png)
![Character 101](./output/Arial%20Regular/101.png)
![Character 102](./output/Arial%20Regular/102.png)
![Character 103](./output/Arial%20Regular/103.png)
![Character 104](./output/Arial%20Regular/104.png)
![Character 105](./output/Arial%20Regular/105.png)
![Character 106](./output/Arial%20Regular/106.png)
![Character 107](./output/Arial%20Regular/107.png)
![Character 108](./output/Arial%20Regular/108.png)
![Character 109](./output/Arial%20Regular/109.png)
![Character 110](./output/Arial%20Regular/110.png)
![Character 111](./output/Arial%20Regular/111.png)
![Character 112](./output/Arial%20Regular/112.png)
![Character 113](./output/Arial%20Regular/113.png)
![Character 114](./output/Arial%20Regular/114.png)
![Character 115](./output/Arial%20Regular/115.png)
![Character 116](./output/Arial%20Regular/116.png)
![Character 117](./output/Arial%20Regular/117.png)
![Character 118](./output/Arial%20Regular/118.png)
![Character 119](./output/Arial%20Regular/119.png)
![Character 120](./output/Arial%20Regular/120.png)
![Character 121](./output/Arial%20Regular/121.png)
![Character 122](./output/Arial%20Regular/122.png)
![Character 123](./output/Arial%20Regular/123.png)
![Character 124](./output/Arial%20Regular/124.png)
![Character 125](./output/Arial%20Regular/125.png)
![Character 126](./output/Arial%20Regular/126.png)



## Output

- **Rendered Images**: PNG files of each character saved in a subdirectory named after the font.
- **Luminance Report**: A CSV file containing luminance values for each character.
- **Pretty Table**: A tabular view of the luminance values (optional).

## Dependencies

- Python 3.9+
- PIL (Pillow)
- PrettyTable
- NumPy

Install dependencies via:
```bash
pip install -r requirements.txt
```
## License

This project is licensed under the MIT License. See the `LICENSE` file for details.