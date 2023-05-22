"""Setup module"""

from setuptools import setup

with open("README.md", mode="r", encoding="utf-8") as f:
    LONG_DESCRIPTION = f.read()

setup(
    name="pyuptobox",
    version="1.0.4",
    description="Python SDK to interact with Uptobox API.",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/hyugogirubato/pyuptobox",
    author="hyugogirubato",
    author_email="hyugogirubato@gmail.com",
    license="GNU GPLv3",
    packages=["pyuptobox"],
    install_requires=["requests", "requests_toolbelt", "beautifulsoup4"],
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
