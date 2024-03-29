# Font Tester

Test fonts using diffenator2.

## Usage

```YAML
- uses: f-actions/diffenator2@main
  with:

    # Personal access token (PAT). This is required in order to download
    # fonts from upstream font projects. Use ${{ secrets.GITHUB_TOKEN }}
    # Required: True
    github-token: ''

    # Path to fonts which need to be tested. Wildcards are possible e.g
    # `fonts/variable/*.ttf`
    # Required: True
    path: ''

    # Method to fetch older fonts for comparison. Choose from
    # 'googlefonts' or 'github-release'.
    # Required: False
    fetch-before: ''

    # The 'username/repo' string if fetch-before is set to 'github-release'
    # e.g `googlefonts/gulzar`.
    # Required: False
    repo: ''

    # Font path to older fonts to compare against e.g `fonts_before/*.ttf.
    # Required: False
    path-before: ''

    # Output directory
    # Default: test_results
    # Required: False
    out: ''

    # Run diffenator
    # Default: False
    run-diffenator: bool

    # Run diffbrowsers
    # Default: False
    run-diffbrowsers: bool

    # Path to a user wordlist
    # Required: False
    user-wordlist: ''

    # Only test the following styles. Regex strings accepted e.g "Regular|Bold|.*Italic"
    # Required: False
    filter-styles: ''

    # Set font point size for diffbrowsers
    # Required False
    pt-size: int

    # Show changes over this percentage of changed pixels
    # Required: False (default 0.9)
    threshold: float

```



## Examples

Run proofing tools:

```YAML
on: [push]

jobs:
  font-render:
    runs-on: ubuntu-latest
    name: Check fonts on different browsers
    steps:
        - uses: actions/checkout@v2
        - uses: f-actions/diffenator2@main
          with:
            github-token: ${{ secrets.GITHUB_TOKEN }}
            path: "./fonts/*.ttf"
```

Diff fonts against Google Fonts:

```YAML
on: [push]

jobs:
  font-render:
    runs-on: ubuntu-latest
    name: Check fonts on different browsers
    steps:
        - uses: actions/checkout@v2
        - uses: f-actions/diffenator2@main
          with:
            github-token: ${{ secrets.GITHUB_TOKEN }}
            path: "./fonts/*.ttf"
            fetch-before: "googlefonts"
            path-before: "*.ttf"
            run-diffenator: true
            run-diffbrowsers: true
```

Diff fonts against a latest upstream release but only test Regular and Italic:

```YAML
on: [push]

jobs:
  font-render:
    runs-on: ubuntu-latest
    name: Check fonts on different browsers
    steps:
        - uses: actions/checkout@v2
        - uses: f-actions/diffenator2@main
          with:
            github-token: ${{ secrets.GITHUB_TOKEN }}
            path: "./gulzar/fonts/*.ttf"
            fetch-before: "github-release"
            repo: "googlefonts/gulzar"
            path-before: "*.ttf"
            run-diffenator: true
            run-diffbrowsers: true
            filter-styles: "Regular|Italic"
```

Generating screenshots on Mac, Win and Linux with a 14pt font size

```YAML
name: Test screenshots

on:
  push:
    branches: [main]

jobs:
  screenshot:
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        python-version: [3.9]
        os: [ubuntu-latest, windows-latest, macos-latest]
    steps:
      - uses: actions/checkout@v2
        with:
          submodules: recursive
          fetch-depth: 0
      - uses: f-actions/diffenator2@main
        with:
          github-token: ${{ secrets.GITHUB_TOKEN }}
          paths: "./fonts"
          fonts_before: "googlefonts"
          run-diffenator: false
          run-diffbrowsers: true
          pt-size: 14
```

For a complete project see https://github.com/m4rc1e/mavenproFont/blob/main/.github/workflows/build.yaml. This project will first build the fonts and then compare them against the latest release on Google Fonts. It uses a platform matrix to render browser screenshots for Win, Mac and Linux. It also runs diffenator on the latest Linux as a seperate job. This setup should be suitable for most font projects.