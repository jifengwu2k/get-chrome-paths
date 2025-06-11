# Get Chrome Paths

A cross-platform Python utility to find Chromium-based browser executable paths on Windows, macOS, and Linux.

Supports Python 2+.

## Features

- Detects installed Chrome, Chromium, and Microsoft Edge browsers
- Supports Windows (common registry path lookup), macOS (common application paths), and Linux (common installation paths)

## Installation

```bash
pip install get-chrome-paths
```

## Usage

```python
from __future__ import print_function

from get_chrome_paths import get_chrome_paths

# Get all available Chrome/Chromium-based browser paths
for path in get_chrome_paths():
    print(path)
# Example output on Windows:
# C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe
# C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe
```

You can also run as a module:

```bash
python -m get_chrome_paths
# Example output on Windows:
# C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe
# C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements.

## License

MIT License. See [LICENSE](LICENSE) for more information.
