# YAPI - Yet Another Package Installer

import cache_manager
from configparser import ConfigParser
from configparser import ExtendedInterpolation
from os import getlogin
import script_runner  # Script Runner
import sys  # Make System Calls
import user_interface  # User Interface

config = ConfigParser(interpolation=ExtendedInterpolation())
config.read("config.ini")

packages_path = config["PACKAGES"]["packages_path"].replace(
    "~", "/home/" + getlogin())

# Response and run Options
options = {
    "install": ["<package_to_install>", "Install one of the packages"],
    "console": ["no", "Run Yapi with the terminal question installer"],
    "update": ["no", "Pull the newest YAPI version from github"],
    "cache": ["no", "Recreate the cache"],
    "help": ["no", "Information about YAPI"]
}


def print_commands_allowed():
    """Print on console all the commands allowed to run with YAPI."""
    print("You can choose from this arguments: ")
    for option in options:
        if options[option][0] != "no":
            print("\t - {} \n\t\t python yapi.py {} {}".format(
                options[option][1], option, options[option][0]))
        else:
            print("\t - {} \n\t\t python yapi.py {}".format(
                options[option][1], option))


def argumentError(arg):
    """Print on console a message of Argument error.

    Arguments:
    arg -- this is the argument to print that is not allowed
    """
    print("The argument {} isn't allowed,".format(arg.upper()))
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
        script_runner.runScript(packages_path + "updateYapiScripts.sh")
    elif (sys.argv[1] == "cache"):
        try:
            result = cache_manager.delete_cache(packages_path)
            if not result:
                print("Previous cache not deleted")
            cache_manager.get_packages(
                packages_path,
                str(config["PACKAGES"]["ignore"]).split(sep=", "))
        except Exception:
            print("No cache file found")
    elif (sys.argv[1] == "help"):
        print_commands_allowed()
    else:
        argumentError(sys.argv[1])
elif len(sys.argv) == 3:
    if sys.argv[1] == "install":
        script_runner.runScript(packages_path + sys.argv[2] + ".sh")
