"""Setup module"""

from setuptools import setup

with open("README.md", mode="r", encoding="utf-8") as f:
    LONG_DESCRIPTION = f.read()

setup(
    name="pybinance",
    version="1.0.2",
    description="Python SDK to interact with Binance API.",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/hyugogirubato/pybinance",
    author="hyugogirubato",
    author_email="hyugogirubato@gmail.com",
    license="GNU GPLv3",
    packages=["pybinance"],
    install_requires=["requests", "PyJWT"],
    classifiers=[
        "Environment :: Console",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Utilities"
    ]
)
