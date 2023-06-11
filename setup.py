from setuptools import setup, find_packages

setup(
    name="pyuptobox",
    version="1.1.0",
    author="hyugogirubato",
    author_email="hyugogirubato@gmail.com",
    description="Python client for the Uptobox API.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/hyugogirubato/pyuptobox",
    packages=find_packages(),
    license="GPL-3.0-only",
    keywords=[
        "client",
        "uptobox",
        "cloudstorage",
        "uptostream"
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Utilities"
    ],
    install_requires=[
        "requests",
        "requests_toolbelt",
        "beautifulsoup4"
    ],
    python_requires=">=3.7"
)
