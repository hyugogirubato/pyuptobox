import webbrowser

import pyuptobox
from pyuptobox.client import Client
from pyuptobox.utils import get_code, get_size

# Demo: https://uptobox.com/5w4rff6r17oz
if __name__ == "__main__":
    print(f"I: PyUptobox version {pyuptobox.__version__}")

    # create client
    client = Client()

    # get file code
    url = input("I: File url/code: ")
    file_code = get_code(value=url)

    # login
    user = client.login(token="USER_TOKEN")

    # get file info
    info = client.get_files_info(file_codes=[file_code])[0]
    file_size = get_size(info["file_size"])

    # get file download link
    link = client.get_file_link(file_code=file_code)["dlLink"]

    print("I: Subscription: {}".format("PREMIUM" if user["premium"] == 1 else "FREE"))
    print("I: Name: {}".format(info["file_name"]))
    print("I: Size: {}".format(file_size))
    print("I: Link: {}".format(link))

    # download media with default browser
    webbrowser.open(link)
