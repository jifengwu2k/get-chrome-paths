from __future__ import print_function
import os
import os.path
import platform
import sys


def get_unique_elements(iterable):
    seen = set()
    unique_elements = []

    for element in iterable:
        if element not in seen:
            seen.add(element)
            unique_elements.append(element)
    
    return unique_elements


def filter_existing_paths(paths):
    return [p for p in paths if os.path.isfile(p)]


def get_chrome_paths():
    system = platform.system()
    chrome_paths = []

    if system == 'Windows':
        if sys.version_info < (3,):
            import _winreg as winreg
        else:
            import winreg

        common_registry_paths = [
            # Google Chrome
            "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\App Paths\\chrome.exe",
            "SOFTWARE\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\App Paths\\chrome.exe",
            # Chromium
            "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\App Paths\\chromium.exe",
            "SOFTWARE\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\App Paths\\chromium.exe",
            # Microsoft Edge
            "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\App Paths\\msedge.exe",
            "SOFTWARE\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\App Paths\\msedge.exe",
        ]

        for path in common_registry_paths:
            try:
                key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path)
                browser_path = winreg.QueryValue(key, None)
                winreg.CloseKey(key)
                if browser_path is not None and os.path.isfile(browser_path):
                    chrome_paths.append(browser_path)
            except (IOError, OSError):
                continue

    elif system == 'Darwin':
        common_paths = [
            # Google Chrome
            '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
            '/Applications/Google Chrome Beta.app/Contents/MacOS/Google Chrome Beta',
            '/Applications/Google Chrome Canary.app/Contents/MacOS/Google Chrome Canary',
            '/Applications/Google Chrome Dev.app/Contents/MacOS/Google Chrome Dev',
            # Chromium
            '/Applications/Chromium.app/Contents/MacOS/Chromium',
            # Microsoft Edge
            '/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge',
            '/Applications/Microsoft Edge Beta.app/Contents/MacOS/Microsoft Edge Beta',
            '/Applications/Microsoft Edge Canary.app/Contents/MacOS/Microsoft Edge Canary',
            '/Applications/Microsoft Edge Dev.app/Contents/MacOS/Microsoft Edge Dev',
        ]

        chrome_paths.extend(filter_existing_paths(common_paths))

    elif system == 'Linux':
        common_paths = [
            # Google Chrome
            '/usr/bin/google-chrome',
            '/snap/bin/google-chrome',
            # Chromium
            '/usr/bin/chromium',
            '/usr/bin/chromium-browser',
            '/snap/bin/chromium',
            # Microsoft Edge
            '/usr/bin/microsoft-edge',
        ]

        chrome_paths.extend(filter_existing_paths(common_paths))

    return get_unique_elements(chrome_paths)


if __name__ == '__main__':
    for chrome_path in get_chrome_paths():
        print(chrome_path)