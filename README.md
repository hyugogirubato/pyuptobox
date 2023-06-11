<div align="center">

<img src="https://github.com/hyugogirubato/pyuptobox/blob/main/docs/images/icon.png" width="10%">

# PyUptobox

[![License](https://img.shields.io/github/license/hyugogirubato/pyuptobox)](https://github.com/hyugogirubato/pyuptobox/blob/main/LICENSE)
[![Release](https://img.shields.io/github/release-date/hyugogirubato/pyuptobox)](https://github.com/hyugogirubato/pyuptobox/releases)
[![Latest Version](https://img.shields.io/pypi/v/pyuptobox)](https://pypi.org/project/pyuptobox/)

</div>

PyUptobox is a Python client for the Uptobox API. It provides convenient methods for authentication, file management,
and file download/upload operations with Uptobox, a popular file hosting service.

## Features

- Authenticate with Uptobox using login credentials or token
- Get user account information
- Set various user settings (SSL download, direct download, etc.)
- Manage files and folders (create, delete, move, rename)
- Retrieve file information and download links
- Upload files to Uptobox
- Get streaming links and transcode files
- and more...

## Installation

You can install PyUptobox using pip:

````shell
pip install pyuptobox
````

## Usage

Here's an example of how to use the PyUptobox library:

```python
from pyuptobox.client import Client
from pyuptobox.utils import get_code, get_size

# Create client
client = Client()

# Login
client.login(token="YOUR_USER_TOKEN")

# Get file code
file_code = get_code(value="https://uptobox.com/your-file-url")

# Get file info
info = client.get_files_info(file_codes=[file_code])[0]
file_size = get_size(info["file_size"])

# Get file download link
link = client.get_file_link(file_code=file_code)["dlLink"]

print("File Name: {}".format(info["file_name"]))
print("File Size: {}".format(file_size))
print("Download Link: {}".format(link))

```

For more information on how to use PyUptobox, please refer to the [documentation](https://docs.uptobox.com).

## Disclaimer

PyUptobox is an unofficial library and is not affiliated with or endorsed by Uptobox or Uptostream. The library is
provided "as is" without any warranty, and the usage of this library is at your own risk. Make sure to comply with the
terms and conditions of the Uptobox service while using this library.

### License

This project is licensed under the [GPL v3 License](https://github.com/hyugogirubato/pyuptobox/blob/main/LICENSE).