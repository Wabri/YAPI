def get_language_pack():
    """Get language pack from configuration files."""
    from configparser import ConfigParser
    from configparser import ExtendedInterpolation
    from os import getlogin
    config = ConfigParser(interpolation=ExtendedInterpolation())
    config.read("config.ini")
    language_config_file = str(config["COMMON"]["language_dir"]).replace(
        "~", "/home/" + getlogin()) + "/" + config["COMMON"]["language"] \
        + ".ini"
    language_config = ConfigParser()
    language_config.read(language_config_file)
    language_pack = dict()
    for key in language_config.keys():
        language_pack[key] = dict()
        for element in language_config[key]:
            language_pack[key][element] = language_config[key][element]
    return language_pack
