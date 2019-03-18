from modules.cache.cache_manager import get_packages
from modules.configuration.config_extractor import get_configuration
from modules.languages.language_pack_manager import get_language_pack
import glob
import pickle

config = get_configuration()

packages_path = get_packages(
    config["PACKAGES"]["packages_path"],
    str(config["PACKAGES"]["ignore"]).split(sep=", "))

command_list = get_language_pack()["COMMANDS"]
help_list = get_language_pack()["HELP"]

readme_packages_path = config["PACKAGES"]["packages_path"] + "/README.md"
readme_help_path = config["COMMON"]["yapi_dir"] + "/README.md"


def packages_update(packages, readme_path):
    start_update = True
    continue_read = True
    readme_updated = list()
    with open(readme_path, "r") as readme:
        for line in readme.readlines():
            if not continue_read:
                if start_update:
                    for package_counter in packages:
                        readme_updated.append(
                            str("- {0} - {1} - {2}".format(
                                packages[package_counter][0].capitalize(),
                                packages[package_counter][1],
                                packages[package_counter][2])))
                    start_update = False
                if line == "<!--readme_update end packages -->\n":
                    readme_updated.append(line)
                    continue_read = True
            else:
                starter = "<!--readme_update start packages -->\n"
                continue_read = line != starter
                readme_updated.append(line)
    del start_update, continue_read

    with open(readme_path, "w") as readme:
        for line in readme_updated:
            print(line.strip("\n"), file=readme)
    del readme_path, readme_updated


def help_update(commands, help, readme_path):
    start_update = True
    continue_read = True
    readme_updated = list()
    with open(readme_path, "r") as readme:
        for line in readme.readlines():
            if not continue_read:
                if start_update:
                    for command in commands:
                        if not command == "description":
                            readme_updated.append(
                                str("To {}: \n \n \tyapi {} {} \n \n"
                                    .format(
                                        str(help[command]).lower(),
                                        command,
                                        commands[command])))
                    start_update = False
                if line == "<!--readme_update end help -->\n":
                    readme_updated.append(line)
                    continue_read = True
            else:
                continue_read = line != "<!--readme_update start help -->\n"
                readme_updated.append(line)
    del start_update, continue_read

    with open(readme_path, "w") as readme:
        for line in readme_updated:
            print(line.strip("\n"), file=readme)
    del readme_path, readme_updated

packages_update(packages_path, readme_packages_path)
help_update(command_list, help_list, readme_help_path)
