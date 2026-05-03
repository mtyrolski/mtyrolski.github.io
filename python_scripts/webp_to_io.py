#!/usr/bin/env python3
"""
Convert an input WebP (or any Pillow-supported image) into a multi-size .ico file.
This script center-crops to square (so the square is filled) and resizes to the standard favicon sizes,
then writes an ICO that contains PNG-encoded images for each size (widely supported).
"""

from PIL import Image
import io
import struct
import sys

STANDARD_SIZES = [256, 128, 64, 48, 32, 16]

def crop_center_to_square(img: Image.Image) -> Image.Image:
    img = img.convert("RGBA")
    w, h = img.size
    side = min(w, h)
    left = (w - side) // 2
    top = (h - side) // 2
    return img.crop((left, top, left + side, top + side))

def make_resized_images(src_path: str, sizes=STANDARD_SIZES, fill_method="crop"):
    src = Image.open(src_path)
    if fill_method == "crop":
        base = crop_center_to_square(src)
    elif fill_method == "pad":
        # pad to square with transparent background
        src = src.convert("RGBA")
        w, h = src.size
        side = max(w, h)
        sq = Image.new("RGBA", (side, side), (0,0,0,0))
        sq.paste(src, ((side-w)//2, (side-h)//2), src)
        base = sq
    else:
        raise ValueError("fill_method must be 'crop' or 'pad'")

    images = []
    for s in sizes:
        im = base.resize((s, s), Image.LANCZOS)
        images.append(im)
    return images

def write_ico_from_png_bytes(png_bytes_list, sizes_list, out_path):
    """
    Create ICO file where each entry is a PNG blob (modern ICO supports PNG images).
    Structure per ICO spec:
    - ICONDIR (6 bytes): 0 (2), type=1(2), count(2)
    - For each image: ICONDIRENTRY (16 bytes)
    - Followed by image data blobs
    """
    count = len(png_bytes_list)
    # ICONDIR
    with open(out_path, "wb") as f:
        f.write(struct.pack("<HHH", 0, 1, count))
        # offset starts right after ICONDIR + entries
        offset = 6 + 16 * count
        # write entries
        for size, data in zip(sizes_list, png_bytes_list):
            w = size if size < 256 else 0
            h = size if size < 256 else 0
            bpp = 32
            # color count and reserved are 0
            # planes and bitcount: set to 1 and 32 (common)
            f.write(struct.pack("<BBBBHHII",
                                w,          # width (1 byte; 0 means 256)
                                h,          # height (1 byte; 0 means 256)
                                0,          # color count
                                0,          # reserved
                                1,          # planes
                                bpp,        # bit count
                                len(data),  # bytes in resource
                                offset))    # image offset
            offset += len(data)
        # write image data blobs
        for data in png_bytes_list:
            f.write(data)

def convert_webp_to_ico(in_path: str, out_path: str, sizes=STANDARD_SIZES, fill_method="crop"):
    imgs = make_resized_images(in_path, sizes=sizes, fill_method=fill_method)
    png_bytes = []
    for im in imgs:
        b = io.BytesIO()
        # save each as PNG bytes (keeps alpha)
        im.save(b, format="PNG")
        png_bytes.append(b.getvalue())
    write_ico_from_png_bytes(png_bytes, sizes, out_path)
    print(f"Wrote {out_path} containing sizes: {sizes}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python webp_to_ico.py input.webp output.ico [crop|pad]")
        sys.exit(1)
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    method = sys.argv[3] if len(sys.argv) >= 4 else "crop"
    convert_webp_to_ico(input_path, output_path, fill_method=method)