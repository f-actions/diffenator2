# Diffbrowsers Action

Test how fonts render on different browsers using `gftools gen-html`

## Usage

Create a `.github/workflows/test.yml` with the following contents:

```YAML
on: [push]

jobs:
  font-render:
    runs-on: ubuntu-latest
    name: Check fonts on different browsers
    steps:
        - uses: actions/checkout@v2
        - uses: m4rc1e/font-browser-tests-action@latest
          with:
            paths: ./fonts # Path to a directory of fonts
            pt_size: 15 # Change text pt size in html docs (Optional) 
            fonts_before: 'google-fonts' # Diff against previous fonts (Optional)
```

Want to test different operating systems? use a matrix.

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
      - uses: m4rc1e/font-browser-tests-action@latest
        with:
          paths: ./fonts
          pt_size: 15
          fonts_before: google-fonts
          width: 1280
```
