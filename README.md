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

## Features

- 🛡️ Methode de connexion multiple
- 📦 Direct use of the service, without restrictions
- 🛠️ Easy implementation in other programs
- 🧩 Plug-and-play installation via setup.py
- ❤️ Forever FOSS!

## Installation

*Note: Requires [Python] 3.7.0 or newer with PIP installed.*

```shell
$ python setup.py install
```

You now have the `UptoboxSDK` package installed and a `UptoboxSDK` executable is now available.


### From Source Code

The following steps are instructions on download, preparing, and running the code under a Venv environment.
You can skip steps 3-5 with a simple `pip install .` call instead, but you miss out on a wide array of benefits.

1. `git clone https://github.com/hyugogirubato/UptoboxSDK`
2. `cd pydvdfab`
3. `python -m venv env`  
4. `source env/bin/activate`   
5. `python setup.py install`

As seen in Step 5, running the `UptoboxSDK` executable is somewhat different to a normal PIP installation.
See [Venv's Docs] on various ways of making calls under the virtual-environment.

  [Python]: <https://python.org>
  [Venv's]: <https://docs.python.org/3/tutorial/venv.html>
  [Venv's Docs]: <https://docs.python.org/3/library/venv.html>

## Usage

The following is a minimal example of using UptoboxSDK in a script. It gets the download link of a
file. There's various stuff not shown in this specific example like:

- Searching for a file
- Uploading a file
- User information
- and much more!

Just take a look around the Client code to see what stuff does. Everything is documented quite well.
There's also various functions in `utils.py` that showcases a lot of features.

```py
from UptoboxSDK.client import Client

# Demo: https://uptobox.com/5w4rff6r17oz
if __name__ == "__main__":
    # create client
    client = Client()

    # login
    data = client.login(token="USER_TOKEN")

    # get cached keys
    file_code = "5w4rff6r17oz"
    
    # get file info
    info = client.get_file_info(code=file_code)
    
    # get file download link
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
