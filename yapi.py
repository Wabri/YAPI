# YAPI - Yet Another Packages Installer

import glob
import os
import subprocess

where_is_scripts = "scripts/"

packages = {}

os.chdir(where_is_scripts)
counter_packages = 1
for file in glob.glob("*.sh"):
    package_name = file.split(".")[0].capitalize()
    package_description = ""
    with open(file, "r") as open_file:
        package_description = str(open_file.readline())
        if package_description[0] == "#":
            package_description = package_description.strip("\n").strip("# ")
        else:
            package_description = package_name
    if file == "test.sh":
        packages[0] = [
            package_name,
            package_description,
            where_is_scripts + file
        ]
    else:
        packages[counter_packages] = [
            package_name,
            package_description,
            where_is_scripts + file
        ]
        counter_packages += 1
os.chdir("..")

yes_answer = ("Y", "Yes", "y", "yes")
no_answer = ("N", "No", "n", "no")
right_answer = yes_answer + no_answer

continue_to_ask = True

while continue_to_ask:
    print("-" * 79)
    print("You can choose to install this packages:")
    for package_counter in packages:
        print("{:>2}) {} - {}".format(
            package_counter,
            packages[package_counter][0],
            packages[package_counter][1]))
    choose = -1
    while choose not in range(0, package_counter + 1):
        choose = int(input("What package do you want to install? "))
    package_to_install = choose
    while choose not in right_answer:
        choose = input(
            "Do you want to install {}? ".format(
                packages[package_to_install][0]))
    if choose in yes_answer:
        print("Let's start the installation, these take a moment...")
        with open(packages[package_to_install][2], "r") as file_script:
            bashCommand = ""
            for line in file_script.readlines():
                if line[0] != "#":
                    bashCommand += line
            bashCommand = bashCommand.replace("\n", " ; ")
            # try:
            #     retcode = call(bashCommand, shell=True)
            #     if retcode < 0:
            #         print("Child was terminated by signal", -retcode,
            #               file=sys.stderr)
            #     else:
            #         print("Child returned", retcode, file=sys.stderr)
            # except OSError as e:
            #     print("Execution failed:", e, file=sys.stderr)
            output = subprocess.check_output(
                bashCommand,
                stderr=subprocess.STDOUT,
                shell=True)
    else:
        print("Ok, no problem...")
    choose = ""
    while choose not in right_answer:
        choose = input("Do you want to install something else? ")
    if choose in yes_answer:
        continue
    else:
        print("Ok, bye bye!")
        break
print("-" * 79)
