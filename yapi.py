# YAPI - Yet Another Packages Installer

import glob
import os
import pickle
import subprocess
import sys

where_is_scripts = "scripts/"
packages_binary_file_store = "packages.bin"
packages = {}

if os.path.exists(packages_binary_file_store):
    with open(packages_binary_file_store, "rb") as packages_binary:
        packages = pickle.load(packages_binary)
        print("Packages load from {}".format(packages_binary_file_store))
else:
    os.chdir(where_is_scripts)
    counter_packages = 1
    for file in glob.glob("*.sh"):
        package_name = file.split(".")[0]
        package_description = ""
        with open(file, "r") as open_file:
            package_info = str(open_file.readline())
            if package_info[0] == "#":
                package_info = package_info.strip(
                    "\n").strip("# ")
                for character in package_info:
                    if character == "-":
                        break
                    package_description += character
                package_url = ""
                precedent_character = ""
                get_url = False
                for character in package_info:
                    if not get_url and precedent_character == "-":
                        get_url = character == " "
                        if get_url:
                            continue
                    elif get_url:
                        package_url += character
                    precedent_character = character
                if not package_url:
                    package_url = "no url"
                del precedent_character, get_url
            else:
                package_description = package_url = package_name
        if file == "test.sh":
            packages[0] = [
                package_name,
                package_description,
                package_url,
                where_is_scripts + file
            ]
        else:
            packages[counter_packages] = [
                package_name,
                package_description,
                package_url,
                where_is_scripts + file
            ]
            counter_packages += 1
    os.chdir("..")
    with open(packages_binary_file_store, "wb") as packages_binary:
        pickle.dump(packages, packages_binary,
                    protocol=0)
        print("Packages store into {}".format(packages_binary_file_store))

yes_answer = ("Y", "Yes", "y", "yes")
no_answer = ("N", "No", "n", "no")
right_answer = yes_answer + no_answer
options = {
    "install": ["<package_to_install>", "Install one of the packages"],
    "console": ["no", "Run Yapi with the terminal question installer"]
}

if len(sys.argv) == 1:
    print("GUI not develop yet")

elif len(sys.argv) == 2:
    if (sys.argv[1] == "console"):
        continue_to_ask = True
        while continue_to_ask:
            print("-" * 79)
            print("You can choose to install this packages:")
            for package_counter in packages:
                print("{:>2}) {} - {}".format(
                    package_counter,
                    packages[package_counter][0].capitalize(),
                    packages[package_counter][1]))
            choose = -1
            while choose not in range(package_counter + 1):
                choose = input("What package do you want to install? ")
                try:
                    choose = int(choose)
                    if choose not in range(package_counter + 1):
                        print("The package number must be between " +
                              " 0 and {}".format(package_counter))
                except ValueError:
                    if choose == "exit":
                        print("Ok, bye bye!")
                        exit()
                    print("Please insert a number between 0 and {}".format(
                        package_counter))
                    choose = -1
            package_to_install = choose
            while choose not in right_answer:
                choose = input(
                    "Do you want to install {}? ".format(
                        packages[package_to_install][0]))
            if choose in yes_answer:
                print("Let's start the installation, these take a moment...")
                with open(packages[package_to_install][3], "r") as file_script:
                    bashCommand = ""
                    for line in file_script.readlines():
                        if line[0] != "#":
                            bashCommand += line
                    bashCommand = bashCommand.replace("\n", " ; ")
                    subprocess.call(
                        bashCommand, stderr=subprocess.STDOUT, shell=True)
            else:
                print("Ok, no problem...")
            choose = ""
            while choose not in right_answer:
                choose = input("Do you want to install something else? ")
            if choose in yes_answer:
                continue
            else:
                print("Ok, bye bye!")
                exit()
        print("-" * 79)
    else:
        print("The argument {} isn't allowed,".format(sys.argv[1].upper()) +
              " you can choose from this arguments:")
        for option in options:
            if options[option][0] != "no":
                print("\t - {} \n\t\t python yapi.py {} {}".format(
                    options[option][1], option, options[option][0]))
            else:
                print("\t - {} \n\t\t python yapi.py {}".format(
                    options[option][1], option))

elif len(sys.argv) == 3:
    if sys.argv[1] == "install":
        package_to_install = sys.argv[2]
        print("Let's start the installation, these take a moment...")
        try:
            file_script = where_is_scripts + sys.argv[2] + ".sh"
            with open(file_script, "r") as file_script:
                bashCommand = ""
                for line in file_script.readlines():
                    if line[0] != "#":
                        bashCommand += line
                bashCommand = bashCommand.replace("\n", " ; ")
                subprocess.call(
                    bashCommand, stderr=subprocess.STDOUT, shell=True)
        except (OSError, IOError, KeyError) as e:
            print("Package not found. Try again.")
