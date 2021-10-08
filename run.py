"""
Script is too complicated to be a simple bash script.
"""
import os
from fontTools.ttLib import TTFont
from gftools.html import HtmlProof, HtmlDiff
from gftools.utils import font_familyname, download_family_from_Google_Fonts
from glob import glob

envs = os.environ
fonts = glob(envs['path'])

# User just wants proofs
if not "fonts_before" in envs:
    html = HtmlProof(
        fonts,
        out="screenshots",
        selenium_screenshots=True
    )
else:
    # User wants to diff against Google Fonts
    ttFont = TTFont(fonts[0])
    family_name = font_familyname(ttFont)
    if "google-fonts" in envs['fonts_before']:
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


html.build_pages(pt_size=envs['pt_size'])
html.save_imgs()