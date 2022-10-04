#!/usr/bin/env python3
"""
"""
import os
from fontTools.ttLib import TTFont
from glob import glob
import argparse
from diffenator import run_proofing_tools, run_diffing_tools
from diffenator.utils import (
    download_google_fonts_family,
    download_latest_github_release_archive,
)


parser = argparse.ArgumentParser()
parser.add_argument("--paths", nargs="+", required=True)
parser.add_argument("--fonts_before", default="none")
parser.add_argument("--out", default="screenshots")
args = parser.parse_args()

out = os.path.abspath(args.out)


os.mkdir(out)


for font_dir in args.paths:
    fonts = glob(os.path.abspath(os.path.join(font_dir, "*.ttf")))
    ttFonts = [TTFont(f) for f in fonts]
    family_name = ttFonts[0]["name"].getBestFamilyName()
    out = os.path.join(out, family_name)

    # User just wants proofs
    if args.fonts_before == "none":
        run_proofing_tools(ttFonts, out=out, imgs=True)
    else:
        # User wants to diff against Google Fonts
        fonts_before_fp = "fonts_before"
        if args.fonts_before == "google-fonts":
            fonts_before = download_google_fonts_family(family_name, "fonts_before")
## TODO bring this back
#        else:
#            user, repo = args.fonts_before.split("/")
#            gf_archive = download_latest_github_release_archive(
#                user,
#                repo,
#                fonts_before_fp,
#                os.environ["GITHUB_TOKEN"] or os.environ["GH_TOKEN"],
#            )
        ttFonts_before = [TTFont(os.path.abspath(f)) for f in fonts_before]
        run_diffing_tools(ttFonts_before, ttFonts, out=out, imgs=True)
