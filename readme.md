# Font Browser Tests Action

Test how your fonts render on different browsers

## Example

Create a `.github/workflows/test.yml` with the following contents:

```
on: [push]

jobs:
  font-render:
    runs-on: ubuntu-latest
    name: Check fonts on different browsers
    steps:
        - uses: actions/checkout@v2
        - uses: m4rc1e/font-browser-tests-action
```


Want to test different operating systems? use a matrix.

```
TODO
```

## Inputs

You can further customise the action using the following inputs:
