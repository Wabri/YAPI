def get_language_pack():
    """Get language pack from configuration files."""
    from configparser import ConfigParser
    from modules.configuration.config_extractor import get_configuration
    config = get_configuration()
    language_dir = str(config["COMMON"]["language_dir"])
    language_name = str(config["COMMON"]["language"])
    language_config_file = language_dir + "/" + language_name + ".ini"
    language_config = ConfigParser()
    language_config.read(language_config_file)
    language_pack = dict()
    for key in language_config.keys():
        language_pack[key] = dict()
        for element in language_config[key]:
            language_pack[key][element] = language_config[key][element]
    return language_pack
