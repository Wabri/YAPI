
def load_packages_from_file(binary_file):
    """Load packages list from binary."""
    import pickle
    with open(binary_file, "rb") as binary_packages:
        packages_loaded = pickle.load(binary_packages)
        print("[LOG] {} Package load from {}".format(
            len(packages_loaded), binary_file))
    return packages_loaded


def get_package_info(info):
    """Get package description and url from info."""
    description = ""
    url = ""
    info = info.strip("\n").strip("# ")
    for character in info:
        if character == "-":
            break
        description += character
    precedent_character = ""
    get_url = False
    for character in info:
        if not get_url and precedent_character == "-":
            get_url = character == " "
            if get_url:
                continue
        elif get_url:
            url += character
        precedent_character = character
    if not url:
        url = "no url"
    del precedent_character, get_url
    return description, url


def load_packages_from_directory(directory, test="test.sh"):
    """Load packages from scripts."""
    import glob
    import os
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
                package_description, package_url = get_package_info(
                    package_info)
            else:
                package_description = package_url = package_name
        if file == test:
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
    import pickle
    with open(file_name, "wb") as file:
        pickle.dump(packages_list, file, protocol=0)
        print("[LOG] Packages store into {}".format(file_name))


def get_packages(from_file, directory):
    """Get packages."""
    import os
    if os.path.exists(from_file):
        return load_packages_from_file(from_file)
    else:
        packages = load_packages_from_directory(directory)
        make_file_from_packages(packages, from_file)
        return packages
