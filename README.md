<p align="center">
    <img src="docs/images/uptobox_icon_24.png"> <a href="https://github.com/hyugogirubato/UptoboxSDK">UptoboxSDK</a>
    <br/>
    <sup><em>Python SDK to interact with Uptobox API.</em></sup>
</p>

<p align="center">
    <a href="https://pypi.org/project/UptoboxSDK">
        <img src="https://img.shields.io/badge/python-3.7%2B-informational" alt="Python version">
    </a>
    <a href="https://deepsource.io/gh/hyugogirubato/UptoboxSDK">
        <img src="https://deepsource.io/gh/hyugogirubato/UptoboxSDK.svg/?label=active+issues" alt="DeepSource">
    </a>
</p>
UptoboxSDK is a powerful, user-friendly Python package designed for seamless interaction with Uptobox API. It allows users to perform various operations such as multiple connection methods, unrestricted direct use, easy implementation with other programs, and a simple plug-and-play installation. UptoboxSDK is forever free and open-source software.

## Features

* 🛡️ Multiple connection methods support
* 📦 Unrestricted direct use of the service
* 🛠️ Simple integration with other applications
* 🧩 Easy plug-and-play installation via setup.py
* ❤️ Always free and open-source software (FOSS)

## Installation 

**Note**: UptoboxSDK requires [Python](https://python.org/) 3.7.0 or newer with PIP installed.

### With setup.py

```sh
$ python setup.py install
```
You now have the `UptoboxSDK` package installed, and a `UptoboxSDK` executable is available.

### From Source Code
The following steps provide instructions on downloading, preparing, and running the code under a Venv environment. You can skip steps 3-5 with a simple `pip install .` call instead, but you will miss out on a wide array of benefits.
```sh
$ git clone https://github.com/hyugogirubato/UptoboxSDK
$ cd UptoboxSDK
$ python -m venv env
$ source env/bin/activate
$ python setup.py install
```
As seen in Step 5, running the `UptoboxSDK` executable is somewhat different to a normal PIP installation.
See [Venv's Docs](https://docs.python.org/3/tutorial/venv.html) on various ways of making calls under the virtual-environment.


### Usage
The following is a minimal example of using UptoboxSDK in a script. It retrieves the download link of a file. There are various other functionalities not shown in this specific example, such as:

* Searching for a file
* Uploading a file
* User information retrieval
* and much more!

Explore the Client code to discover additional features. Everything is well-documented. Also, check out the various functions in [utils.py](UptoboxSDK/utils.py) that showcase many other capabilities.
```py
from UptoboxSDK.client import Client

# Demo: https://uptobox.com/5w4rff6r17oz
if __name__ == "__main__":
    # Create client
    client = Client()

    # Login
    data = client.login(token="USER_TOKEN")

    # File code
    file_code = "5w4rff6r17oz"
    
    # Get file info
    info = client.get_file_info(code=file_code)
    
    # Get file download link
    link = client.get_link(code=file_code)
    
    print("I: Subscription: {}".format("PREMIUM" if data["premium"] == 1 else "FREE"))
    print("I: Name: {}".format(info["file_name"]))
    print("I: Size: {}".format(info["file_size"]))
    print("I: Link: {}".format(link))

```
## Credit

- Uptobox Icon &copy; Uptobox.
- The great community for their shared research and knowledge about Uptobox and its API.

## License

[GNU General Public License, Version 3.0](LICENSE)
