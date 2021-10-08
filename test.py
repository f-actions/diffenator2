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
parser.add_argument("path")
parser.add_argument("--pt_size", default=16)
parser.add_argument("--fonts_before")
args = parser.parse_args()


fonts = glob(os.path.join(args.path, "*.ttf"))

# User just wants proofs
if not args.fonts_before:
    html = HtmlProof(
        fonts,
        out="screenshots",
        selenium_screenshots=True
    )
else:
    # User wants to diff against Google Fonts
    ttFont = TTFont(fonts[0])
    family_name = font_familyname(ttFont)
    if args.fonts_before == "google-fonts":
        os.mkdir("fonts_before")
        fonts_before = download_family_from_Google_Fonts(
            family_name,
            "fonts_before"
        )
    # TODO add more font_before inputs
    html = HtmlDiff(
        fonts_before,
        fonts,
        out="screenshots",
        selenium_screenshots=True
    )


html.build_pages(pt_size=args.pt_size)
html.save_imgs()