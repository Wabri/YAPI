import glob
import os
import pickle

packages_binary_file = "packages.bin"


def load_packages_from_file(binary_file):
    """Load packages list from binary."""
    with open(binary_file, "rb") as binary_packages:
        packages_loaded = pickle.load(binary_packages)
        print("[LOG] {} Package load from {}".format(
            len(packages_loaded), binary_file))
    return packages_loaded


def load_packages_from_directory(directory):
    """Load packages from scripts."""
    directory = str(directory)
    packages_loaded = dict()
    os.chdir(directory)
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
            packages_loaded[0] = [
                package_name,
                package_description,
                package_url,
                directory + file
            ]
        else:
            packages_loaded[counter_packages] = [
                package_name,
                package_description,
                package_url,
                str(directory + file)
            ]
            counter_packages += 1
    os.chdir("..")
    return packages_loaded


def make_file_from_packages(packages_list, file_name):
    """Create binary file from list."""
    with open(file_name, "wb") as file:
        pickle.dump(packages_list, file, protocol=0)
        print("[LOG] Packages store into {}".format(file_name))
    return ""

if os.path.exists(packages_binary_file):
    packages = load_packages_from_file(packages_binary_file)
else:
    packages = load_packages_from_directory("scripts/")
    make_file_from_packages(packages, packages_binary_file)
