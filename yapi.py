# YAPI - Yet Another Package Installer

import cache_manager
from configparser import ConfigParser
from configparser import ExtendedInterpolation
from language_pack_manager import get_language_pack
from os import getlogin
import script_runner  # Script Runner
import sys  # Make System Calls
import user_interface  # User Interface

config = ConfigParser(interpolation=ExtendedInterpolation())
config.read("config.ini")

packages_path = config["PACKAGES"]["packages_path"].replace(
    "~", "/home/" + getlogin()) + "/"

language_pack = get_language_pack()

options = language_pack["COMMANDS"]

help = language_pack["HELP"]


def print_commands_allowed():
    """Print on console all the commands allowed to run with YAPI."""
    print(language_pack["COMMON"]["2_argument_choose"])
    for option in options:
        print("\t - {} \n\t\t python3 yapi.py {} {} "
              .format(help[option], option, options[option]))


def argumentError(arg):
    """Print on console a message of Argument error.

    Arguments:
    arg -- this is the argument to print that is not allowed
    """
    print(language_pack["COMMON"]
          ["1_argument_not_allowed"].format(arg.upper()))
    print_commands_allowed()


if len(sys.argv) == 1:
    result = user_interface.main()
elif len(sys.argv) == 2:
    if (sys.argv[1] == "console"):
        import console_interface
        packages = cache_manager.get_packages(
            packages_path, str(config["PACKAGES"]["ignore"]).split(sep=", "))
        console_interface.run(packages)
    elif (sys.argv[1] == "update"):
        script_runner.runScript(
            packages_path + "updateYapiScripts" +
            config["COMMON"]["file_extension"])
    elif (sys.argv[1] == "cache"):
        try:
            result = cache_manager.delete_cache(packages_path)
            if not result:
                print("Previous cache not deleted")
            cache_manager.get_packages(
                packages_path,
                str(config["PACKAGES"]["ignore"]).split(sep=", "))
        except Exception:
            print(language_pack["COMMON"]["0_cache_not_found"])
    elif (sys.argv[1] == "help"):
        print_commands_allowed()
    else:
        argumentError(sys.argv[1])
elif len(sys.argv) == 3:
    if sys.argv[1] == "install":
        print(packages_path + sys.argv[2] + config["COMMON"]["file_extension"])
        script_runner.runScript(
            packages_path + sys.argv[2] + config["COMMON"]["file_extension"])
