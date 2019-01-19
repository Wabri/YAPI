def get_language_pack():
    """Get language pack from configuration files."""
    from configuration.config_extractor import get_configuration
    from configparser import ConfigParser
    from os import getlogin
    config = get_configuration()
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
