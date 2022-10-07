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
    download_latest_github_release,
)
import sys


parser = argparse.ArgumentParser()
parser.add_argument("--github-token", required=True)
parser.add_argument("--path", required=True, nargs="+")

parser.add_argument("--fetch-before", choices=("none", "googlefonts", "github-release"), default="none")
parser.add_argument("--repo", default="none")

parser.add_argument("--path-before", default="none")

parser.add_argument("--out", default="screenshots")
args = parser.parse_args()

out = os.path.abspath(args.out)
if not os.path.exists(out):
    os.mkdir(out)



ttFonts = [TTFont(os.path.abspath(f)) for f in args.path]
family_name = ttFonts[0]["name"].getBestFamilyName()
out = os.path.join(out, family_name.replace(" ", "-"))

# User just wants proofs
if args.path_before != "none":
    run_proofing_tools(ttFonts, out=out, imgs=True)
    sys.exit(0)

# get fonts before
if args.path_before != "none" and args.fetch_before == "none":
    raise ValueError("--fetch-before flag required since path_before is provided")

if args.fetch_before == "googlefonts":
    files_before = download_google_fonts_family(family_name, "files_before")
elif args.fetch_before == "github-release":
    if args.repo == "none":
        raise ValueError("--repo flag required e.g 'googlefonts/gulzar'")
    user, repo = args.repo.split("/")
    files_before = download_latest_github_release(user, repo, "files_before", args.github_token)
fonts_before = glob(os.path.abspath(os.path.join("files_before", args.path_before)))
ttFonts_before = [TTFont(os.path.abspath(f)) for f in fonts_before]

run_diffing_tools(ttFonts_before, ttFonts, out=os.path.abspath(out), imgs=True)
