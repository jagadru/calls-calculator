import configparser

config = configparser.ConfigParser()
config.read("calls_calculator.conf")


def get_server_port():
    return int(get_property('server_port', 3101))


def get_server_url():
    return get_property("server_url", "localhost")


def get_property(name, default):
    if ("DEFAULT" in config):
        if (name in config["DEFAULT"]):
            return config["DEFAULT"][name]
    return default
