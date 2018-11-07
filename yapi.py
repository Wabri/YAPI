#

where_is_scripts = "/script/"

packages = {
    0:
        [
            "Name of Package",
            "Description of package",
            where_is_scripts + "hello_test.sh"
        ],
    1:
        [
            "Atom",
            "Atom Text editor",
            where_is_scripts + "atom_installer.sh"
        ],
    2:
        [
            "Discord",
            "Discord chat application",
            where_is_scripts + "discord_installer.sh"
        ],
    3:
        [
            "Dropbox",
            "Dropbox cloud storage",
            where_is_scripts + "dropbox_installer.sh"
        ],
    4:
        [
            "Eclipse Installer",
            "Eclipse IDE installer",
            where_is_scripts + "eclipseInstaller_installer.sh"
        ],
    5:
        [
            "GitKraken",
            "GitKraken is a extended git GUI",
            where_is_scripts + "gitkraken_installer.sh"
        ],
    6:
        [
            "Google Chrome",
            "",
            ""
        ],
    7:
        [
            "Java jdk 11",
            "",
            ""
        ],
    8:
        [
            "Light",
            "",
            ""
        ],
    9:
        [
            "NodeJs",
            "",
            ""
        ],
    10:
        [
            "NVidia Driver",
            "",
            ""
        ],
    11:
        [
            "Oh-My-Zsh",
            "",
            ""
        ],
    12:
        [
            "Playerctl",
            "",
            ""
        ],
    13:
        [
            "Rambox",
            "",
            ""
        ],
    14:
        [
            "Skype",
            "",
            ""
        ],
    15:
        [
            "Steam",
            "",
            ""
        ],
    16:
        [
            "VirtualBox",
            "",
            ""
        ]
}

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
        print("Let's start the installation")
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
