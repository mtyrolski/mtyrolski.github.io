#!/usr/bin/env python3
"""
generate_icons.py

Convert a source logo (SVG/PNG/WebP/other Pillow-supported) into:
 - apple-touch-icon-180x180.png
 - favicon.svg (copy if source is SVG, otherwise embed PNG)
 - favicon-32x32.png
 - favicon-192x192.png
 - favicon-512.png
 - manifest.json
 - favicon.ico (contains multiple sizes: 256,128,64,48,32,16 using PNG-compressed entries)

Usage:
  pip install pillow cairosvg
  python generate_icons.py input_logo.svg --out-dir images --fill pad
  python generate_icons.py input_logo.png --out-dir images --fill crop

Options:
  --fill {pad,crop}  pad: keep entire image centered with transparency; crop: center-crop to fill square (default: pad)
"""
from PIL import Image
import io, struct, os, sys, argparse, base64, json

try:
    import cairosvg
    _HAS_CAIROSVG = True
except Exception:
    _HAS_CAIROSVG = False

STANDARD_ICO_SIZES = [256, 128, 64, 48, 32, 16]

def load_image(path):
    path_lower = path.lower()
    if path_lower.endswith(".svg"):
        if not _HAS_CAIROSVG:
            raise RuntimeError("Input is SVG but cairosvg is not installed. pip install cairosvg")
        # render SVG to PNG bytes at a large size for quality
        png_bytes = cairosvg.svg2png(url=path, output_width=2048, output_height=2048)
        return Image.open(io.BytesIO(png_bytes)).convert("RGBA")
    else:
        im = Image.open(path)
        return im.convert("RGBA")

def pad_to_square(img: Image.Image, size: int):
    w, h = img.size
    # If image is larger than requested size, resize down preserving aspect ratio
    if max(w, h) > size:
        if w >= h:
            new_w = size
            new_h = round(h * (size / w))
        else:
            new_h = size
            new_w = round(w * (size / h))
        img = img.resize((new_w, new_h), Image.LANCZOS)
        w, h = img.size
    side = size
    bg = Image.new("RGBA", (side, side), (0,0,0,0))
    paste_x = (side - w)//2
    paste_y = (side - h)//2
    bg.paste(img, (paste_x, paste_y), img)
    return bg

def crop_center_to_square(img: Image.Image, size: int):
    w, h = img.size
    side = min(w, h)
    left = (w - side)//2
    top = (h - side)//2
    cropped = img.crop((left, top, left+side, top+side))
    return cropped.resize((size, size), Image.LANCZOS)

def crop_center_top_to_square(img: Image.Image, size: int):
    w, h = img.size
    side = min(w, h)
    left = (w - side)//2
    top = 0  # align to top
    cropped = img.crop((left, top, left+side, top+side))
    return cropped.resize((size, size), Image.LANCZOS)

def write_ico_from_png_bytes(png_bytes_list, sizes_list, out_path):
    count = len(png_bytes_list)
    with open(out_path, "wb") as f:
        # ICONDIR
        f.write(struct.pack("<HHH", 0, 1, count))
        offset = 6 + 16 * count
        # entries
        for size, data in zip(sizes_list, png_bytes_list):
            w = size if size < 256 else 0
            h = size if size < 256 else 0
            f.write(struct.pack("<BBBBHHII",
                                w,          # width
                                h,          # height
                                0,          # color count
                                0,          # reserved
                                1,          # planes
                                32,         # bit count
                                len(data),  # size in bytes
                                offset))    # offset
            offset += len(data)
        # write data blobs
        for data in png_bytes_list:
            f.write(data)

def generate_images(src_path, out_dir, fill_method="pad"):
    os.makedirs(out_dir, exist_ok=True)
    src_img = load_image(src_path)

    # produce masters
    # We'll render a 512 master for PWA and 256 master for ico/svg embedding
    if fill_method == "pad":
        master_512 = pad_to_square(src_img, 512)
        master_256 = pad_to_square(src_img, 256)
    else:
        master_512 = crop_center_top_to_square(src_img, 512)
        master_256 = crop_center_top_to_square(src_img, 256)

    # Save PNG outputs
    apple_path = os.path.join(out_dir, "apple-touch-icon-180x180.png")
    favicon_32 = os.path.join(out_dir, "favicon-32x32.png")
    favicon_192 = os.path.join(out_dir, "favicon-192x192.png")
    favicon_512 = os.path.join(out_dir, "favicon-512.png")

    master_512.resize((180,180), Image.LANCZOS).save(apple_path, format="PNG")
    master_256.resize((32,32), Image.LANCZOS).save(favicon_32, format="PNG")
    master_512.resize((192,192), Image.LANCZOS).save(favicon_192, format="PNG")
    master_512.save(favicon_512, format="PNG")

    # Create favicon.svg:
    svg_out = os.path.join(out_dir, "favicon.svg")
    if src_path.lower().endswith(".svg"):
        # If original is SVG, copy it to favicon.svg (keeping original vector version)
        with open(src_path, "rb") as r, open(svg_out, "wb") as w:
            w.write(r.read())
    else:
        # Embed base64 PNG (256) inside a simple SVG wrapper as a raster fallback
        b = io.BytesIO()
        master_256.save(b, format="PNG")
        encoded = base64.b64encode(b.getvalue()).decode("ascii")
        svg_content = f'''<?xml version="1.0" encoding="utf-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="256" height="256" viewBox="0 0 256 256" preserveAspectRatio="xMidYMid meet">
  <image width="256" height="256" href="data:image/png;base64,{encoded}" />
</svg>
'''
        with open(svg_out, "w", encoding="utf-8") as f:
            f.write(svg_content)

    # Create favicon.ico with multiple sizes (PNG-compressed entries)
    png_blobs = []
    for s in STANDARD_ICO_SIZES:
        img = master_256.resize((s,s), Image.LANCZOS)
        b = io.BytesIO()
        img.save(b, format="PNG")
        png_blobs.append(b.getvalue())
    ico_out = os.path.join(out_dir, "favicon.ico")
    write_ico_from_png_bytes(png_blobs, STANDARD_ICO_SIZES, ico_out)

    # Create manifest.json
    manifest = {
        "name": "Site",
        "short_name": "Site",
        "icons": [
            {"src": os.path.join("/", out_dir, "favicon-192x192.png").lstrip("/"), "sizes": "192x192", "type": "image/png", "purpose": "any"},
            {"src": os.path.join("/", out_dir, "favicon-512.png").lstrip("/"), "sizes": "512x512", "type": "image/png", "purpose": "any"},
            {"src": os.path.join("/", out_dir, "favicon-512.png").lstrip("/"), "sizes": "512x512", "type": "image/png", "purpose": "maskable"}
        ],
        "theme_color": "#ffffff",
        "background_color": "#ffffff",
        "display": "standalone"
    }
    manifest_path = os.path.join(out_dir, "manifest.json")
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)

    # Return paths
    return {
        "apple": apple_path,
        "svg": svg_out,
        "png32": favicon_32,
        "png192": favicon_192,
        "png512": favicon_512,
        "ico": ico_out,
        "manifest": manifest_path
    }

def main():
    p = argparse.ArgumentParser(description="Generate favicons and manifest from a source logo")
    p.add_argument("source", help="Source image (SVG/PNG/WebP/...)")
    p.add_argument("--out-dir", default="images", help="Output directory for generated images")
    p.add_argument("--fill", choices=["pad","crop"], default="pad", help="pad to square (keep whole image) or crop center to square (fill)")
    args = p.parse_args()

    paths = generate_images(args.source, args.out_dir, fill_method=args.fill)
    print("Generated icons:")
    for k, v in paths.items():
        print(f"  {k}: {v}")

if __name__ == "__main__":
    main()