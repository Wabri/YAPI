
def runScript(path_to_file):
    """Run the script give in argument.

    Arguments:
    path_to_file -- the path to the script to run
    """
    from configparser import ConfigParser
    from configparser import ExtendedInterpolation
    from os import getlogin
    import subprocess
    config = ConfigParser(interpolation=ExtendedInterpolation())
    config.read("config.ini")
    language_config_file = str(config["COMMON"]["language_dir"]).replace(
        "~", "/home/" + getlogin()) + "/" + config["COMMON"]["language"] \
        + ".ini"
    del config
    language_config = ConfigParser()
    language_config.read(language_config_file)
    try:
        with open(path_to_file, "r") as file_script:
            bashCommand = ""
            for line in file_script.readlines():
                if line[0] != "#":
                    bashCommand += line
            bashCommand = bashCommand.replace("\n", " ; ")
            output = subprocess.call(
                bashCommand, stderr=subprocess.STDOUT, shell=True)
            return output
    except (OSError, IOError, KeyError):
        return language_config["SCRIPT-RUNNER"]["0_package_not_found_error"]
