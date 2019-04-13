from os.path import dirname, join, realpath


def read_file(file_name, folder="mocks"):
    file = join(dirname(realpath(__file__)), folder, file_name)
    with open(file) as f:
        return f.read()


def get_api_url(path):
    return "https://api.postcodeapi.nu/v2/{}".format(path)
