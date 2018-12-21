# YAPI - Yet Another Package Installer

import glob                   #UNIX Pathname Expansion
import os                     #Operating System Calls
import pickle                 #Serialization and Deserialization of .bin files
import subprocess             #Run Bash Commands
import sys                    #Make System Calls
import time                   #Time Library
try:
    import toga                   #GUI Library
    from toga.style.pack import * #GUI Components
except:
    pass
import cache_manager          #Cache Manager
import script_runner          #Script Runner

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

def build(app):
    def installHandle(widget):
        import script_runner
        packageToInstall = packageInput.value
        resultInput.value = script_runner.runScript(where_is_scripts + packageToInstall + ".sh")

    packageString = ""
    for package_counter in packages:
        packageString += "{:>2}) {} - {}".format(
            package_counter,
            packages[package_counter][0].capitalize(),
            packages[package_counter][1])
    box = toga.Box()
    listBox = toga.Box()
    listLabel = toga.Label('Packages Available: ' + packageString)
    packageBox = toga.Box()
    packageLabel = toga.Label('Package To Install:', style=Pack(text_align=RIGHT))
    packageInput = toga.TextInput()
    submitBox = toga.Box()
    install = toga.Button('Install Package', on_press=installHandle)
    resultBox = toga.Box()
    resultInput = toga.TextInput(readonly = True)

    listBox.add(listLabel)
    packageBox.add(packageLabel)
    packageBox.add(packageInput)
    submitBox.add(install)
    resultBox.add(resultInput)
    box.add(listBox)
    box.add(packageBox)
    box.add(submitBox)
    box.add(resultBox)

    box.style.update(direction=COLUMN, padding_top=10)
    listBox.style.update(direction=ROW, padding=5)
    packageBox.style.update(direction=ROW, padding=5)
    submitBox.style.update(direction=ROW, padding=5)
    return box

def main():
    return toga.App('Yet Another Package Manager', 'org.YAPI.yapi', startup=build)

if len(sys.argv) == 1:
    main().main_loop()
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
            import os
            cache_file = where_is_scripts.strip("/") + ".bin"
            os.remove(cache_file)
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
