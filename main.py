import argparse

from picture import Picture

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True, help="input file")
ap.add_argument("-c", "--color", action='store_true', help="color/greyscale")
ap.add_argument("-r", "--resolution", type=int, default=120, help="output resolution")
ap.add_argument("-t", "--txt", action='store_true', help="also save as text")
ap.add_argument("-o", "--output", default='output', help="output file")
args = vars(ap.parse_args())

pic = Picture(args["filename"], args["resolution"])

pic.generate()

if args["color"]:
    pic.draw_color()
else:
    pic.draw_bw()

pic.save_image(args["output"])
if args["txt"]:
    pic.save_text(args["output"])
