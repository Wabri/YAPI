def get_configuration():
    """Get configurations from configuration files."""
    from configparser import ConfigParser
    from configparser import ExtendedInterpolation
    from os import getlogin

    config = ConfigParser(interpolation=ExtendedInterpolation())
    config.read("config.ini")
    configuration = dict()
    for key in config.keys():
        configuration[key] = dict()
        for element in config[key]:
            configuration[key][element] = config[key][element].replace(
                "~", "/home/" + getlogin())
    return configuration
