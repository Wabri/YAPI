# YAPI - Yet Another Package Installer

from cache.cache_manager import get_packages, delete_cache
from configuration.config_extractor import get_configuration
from languages.language_pack_manager import get_language_pack
from utility.script_runner import runScript  # Script Runner
import sys  # Make System Calls

config = get_configuration()

packages_path = config["PACKAGES"]["packages_path"]

language_pack = get_language_pack()


def print_commands_allowed():
    """Print on console all the commands allowed to run with YAPI."""
    help = language_pack["HELP"]
    options = language_pack["COMMANDS"]
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
        from interfaces.console_interface import run
        packages = get_packages(
            packages_path, str(config["PACKAGES"]["ignore"]).split(sep=", "))
        run(packages)
    elif (sys.argv[1] == "update"):
        runScript(
            packages_path + "/updateYapiScripts" +
            config["COMMON"]["file_extension"])
    elif (sys.argv[1] == "cache"):
        try:
            result = delete_cache(packages_path)
            get_packages(
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
        runScript(
            packages_path + "/" + sys.argv[2] +
            config["COMMON"]["file_extension"])
