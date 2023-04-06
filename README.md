<p align="center">
    <img src="docs/images/binance_icon_24.svg"> <a href="https://github.com/hyugogirubato/pybinance">pyuptobox</a>
    <br/>
    <sup><em>Python SDK to interact with Binance API.</em></sup>
</p>

<p align="center">
    <a href="https://pypi.org/project/pybinance">
        <img src="https://img.shields.io/badge/python-3.7%2B-informational" alt="Python version">
    </a>
    <a href="https://github.com/hyugogirubato/pybinance/releases">
        <img src="https://img.shields.io/github/release-date/hyugogirubato/pycbzhelper?style=plastic" alt="Release">
    </a>
</p>

> **Warning**
> 
> The client is currently in development, many changes are to be expected. If you have any suggestions for improvement, don't hesitate.

## Features

- 🛡️ Multiple connection method
- 📦 Direct use of the service, without restrictions
- 🛠️ Easy implementation in other programs
- 🧩 Plug-and-play installation via setup.py
- ❤️ Forever FOSS!

## Installation

*Note: Requires [Python] 3.7.0 or newer with PIP installed.*

```shell
$ python setup.py install
```

You now have the `pybinance` package installed and a `pybinance` executable is now available.


### From Source Code

The following steps are instructions on download, preparing, and running the code under a Venv environment.
You can skip steps 3-5 with a simple `pip install .` call instead, but you miss out on a wide array of benefits.

1. `git clone https://github.com/hyugogirubato/pybinance`
2. `cd pybinance`
3. `python -m venv env`  
4. `source env/bin/activate`   
5. `python setup.py install`

As seen in Step 5, running the `pybinance` executable is somewhat different to a normal PIP installation.
See [Venv's Docs] on various ways of making calls under the virtual-environment.

  [Python]: <https://python.org>
  [Venv's]: <https://docs.python.org/3/tutorial/venv.html>
  [Venv's Docs]: <https://docs.python.org/3/library/venv.html>

## Usage

The following is a minimal example of using pybinance in a script. He obtains the access token
of a registered device There's various stuff not shown in this specific example like:

- ...
- and much more!

Just take a look around the Client code to see what stuff does. Everything is documented quite well.
There's also various functions in `utils.py` that showcases a lot of features.

```py
from pybinance import Client

if __name__ == "__main__":
    client = Client()
    client.immed_register(device_id="4a48e4adc872f0755da18b8d1294a878")
```

## Credit

- Binance Icon &copy; Binance.
- The great community for their shared research and knowledge about Binance and its API.

## License

[GNU General Public License, Version 3.0](LICENSE)
