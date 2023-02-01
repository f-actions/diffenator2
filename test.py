#!/usr/bin/env python3
"""
"""
import os
from fontTools.ttLib import TTFont
from glob import glob
import argparse
import ninja
from diffenator2 import ninja_proof, ninja_diff
from diffenator2.utils import (
    download_google_fonts_family,
    download_latest_github_release,
)
import sys


parser = argparse.ArgumentParser()
parser.add_argument("--github-token", required=True)
parser.add_argument("--path", required=True, nargs="+")

parser.add_argument(
    "--fetch-before", choices=("none", "googlefonts", "github-release"), default="none"
)
parser.add_argument("--repo", default="none")

parser.add_argument("--path-before", default="none")

parser.add_argument("--diffenator", default="false")
parser.add_argument("--diffbrowsers", default="false")

parser.add_argument("--user-wordlist", default="none")
parser.add_argument("--filter-styles", default="none")

parser.add_argument("--pt-size", "-pt", type=int, default=20)

parser.add_argument("--out", default="screenshots")
args = parser.parse_args()
args.filter_styles = None if args.filter_styles == "none" else args.filter_styles

out = os.path.abspath(args.out)
if not os.path.exists(out):
    os.mkdir(out)


ttFonts = [TTFont(os.path.abspath(f)) for f in args.path]
family_name = ttFonts[0]["name"].getBestFamilyName()
out = os.path.join(out, family_name.replace(" ", "-"))

# User just wants proofs
if args.path_before == "none":
    ninja_proof(
        ttFonts,
        out=out,
        imgs=True,
        filter_styles=args.filter_styles,
        pt_size=args.pt_size
    )
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
    files_before = download_latest_github_release(
        user, repo, "files_before", args.github_token
    )
fonts_before = glob(os.path.join("files_before", args.path_before))
ttFonts_before = [TTFont(os.path.abspath(f)) for f in fonts_before]

args.diffbrowsers = True if args.diffbrowsers == "true" else False
args.diffenator = True if args.diffenator == "true" else False
args.user_wordlist = None if args.user_wordlist == "none" else args.user_wordlist
ninja_diff(
    ttFonts_before,
    ttFonts,
    diffenator=args.diffenator,
    diffbrowsers=args.diffbrowsers,
    out=os.path.abspath(out),
    imgs=True,
    user_wordlist=args.user_wordlist,
    filter_styles=args.filter_styles,
    pt_size=args.pt_size,
)