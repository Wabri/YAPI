# YAPI - Yet Another Package Installer

import os                     #Operating System Calls
import sys                    #Make System Calls
import time                   #Time Library
import cache_manager          #Cache Manager
import script_runner          #Script Runner
import user_interface         #User Interface

# File Locations
where_is_scripts = "scripts/"
packages_binary_file_store = "packages.bin"

# Response and run Options
options = {
    "install": ["<package_to_install>", "Install one of the packages"],
    "console": ["no", "Run Yapi with the terminal question installer"],
    "update": ["no", "Pull the newest YAPI version from github"],
    "cache": ["no", "Recreate the cache"],
    "help": ["no", "Information about YAPI"]
}

def print_commands_allowed():
    """Print commands."""
    print("You can choose from this arguments: ")
    for option in options:
        if options[option][0] != "no":
            print("\t - {} \n\t\t python yapi.py {} {}".format(
                options[option][1], option, options[option][0]))
        else:
            print("\t - {} \n\t\t python yapi.py {}".format(
                options[option][1], option))

def argumentError(arg):
    """Argument error."""
    print("The argument {} isn't allowed,".format(arg.upper()))
    print_commands_allowed()

if len(sys.argv) == 1:
    result = user_interface.main()
elif len(sys.argv) == 2:
    if (sys.argv[1] == "console"):
        import console_interface
        packages = cache_manager.get_packages(
            where_is_scripts, "test.sh", "updateYapiScripts.sh")
        console_interface.run(packages)
    elif (sys.argv[1] == "update"):
        script_runner.runScript(where_is_scripts + "updateYapiScripts.sh")
    elif (sys.argv[1] == "cache"):
        try:
            cache_file = where_is_scripts.strip("/") + ".bin"
            result = cache_manager.delete_cache(where_is_scripts)
            if (result == False):
                print("Previous cache not deleted")
            cache_manager.get_packages(
                where_is_scripts, "test.sh", "updateYapiScripts.sh")
        except Exception:
            print("No cache file found")
    elif (sys.argv[1] == "help"):
        print_commands_allowed()
    else:
        argumentError(sys.argv[1])
elif len(sys.argv) == 3:
    if sys.argv[1] == "install":
        script_runner.runScript(where_is_scripts + sys.argv[2] + ".sh")
