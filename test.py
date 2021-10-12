#!/usr/bin/env python3
"""
Script is too complicated to be a simple bash script.
"""
import os
from fontTools.ttLib import TTFont
from gftools.html import HtmlProof, HtmlDiff
from gftools.utils import font_familyname, download_family_from_Google_Fonts
from glob import glob
import argparse



parser = argparse.ArgumentParser()
parser.add_argument("--paths", nargs="+", required=True)
parser.add_argument("--pt_size", default=16)
parser.add_argument("--fonts_before", default="none")
parser.add_argument("--width", type=int, default=1280)
parser.add_argument("--out", default="screenshots")
args = parser.parse_args()

os.mkdir(args.out)

for font_dir in args.paths:
    fonts = glob(os.path.join(font_dir, "*.ttf"))
    ttFont = TTFont(fonts[0])
    family_name = font_familyname(ttFont)
    out = os.path.join(args.out, family_name)

    # User just wants proofs
    if args.fonts_before == "none":
        html = HtmlProof(
            fonts,
            out=out,
            selenium_screenshots=True
        )
    else:
        # User wants to diff against Google Fonts
        if args.fonts_before == "google-fonts":
            os.mkdir("fonts_before")
            fonts_before = download_family_from_Google_Fonts(
                family_name,
                "fonts_before"
            )
        html = HtmlDiff(
            fonts_before,
            fonts,
            out=out,
            selenium_screenshots=True
        )

    html.build_pages(pt_size=args.pt_size)
    html.save_imgs(width=args.width)