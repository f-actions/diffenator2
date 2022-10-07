# Font Tester

Test fonts using the Google Fonts font testing tools

## Usage

Create a `.github/workflows/test.yml` with the following contents:


Run proofing tools:

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
        - uses: m4rc1e/font-browser-tests-action@latest
          with:
            path: "./fonts/*.ttf"
            fetch-before: "googlefonts"
            path-before: "*.ttf"
```

Diff fonts against a latest upstream release:

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
            path: "./gulzar/fonts/*.ttf"
            fetch-before: "github-release"
            repo: "googlefonts/gulzar"
            path-before: "*.ttf"
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
          paths: "./fonts"
          fonts_before: "googlefonts"
```

Examples:
TODO