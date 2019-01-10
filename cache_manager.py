
def load_packages_from_file(binary_file):
    """Load packages list from cache.

    Arguments:
    binary_file -- cache file of packages
    """
    import pickle
    with open(binary_file, "rb") as binary_packages:
        packages_loaded = pickle.load(binary_packages)
        print("[LOG] {} Package load from {}".format(
            len(packages_loaded), binary_file))
    return packages_loaded


def get_package_info(info):
    """Get package description and url from info.

    Arguments:
    info -- The line to parse
    """
    description = ""
    url = ""
    info = info.strip("\n").strip("# ")
    precedent_character = ""
    get_url = False
    for character in info:
        if not get_url and precedent_character == "-":
            get_url = character == " "
            if get_url:
                continue
            description += character
        elif get_url:
            url += character
        else:
            description += character
        precedent_character = character
    if not url:
        url = "no url"
    del precedent_character, get_url
    return description[:-2], url


def load_packages_from_directory(directory, ignore_file=[]):
    """Load packages from scripts.

    Arguments:
    directory -- load cache of this directory
    *ignore_file -- string name of files to ignore
    """
    from config_extractor import get_configuration
    import glob
    import os
    config = get_configuration()
    packages_loaded = dict()
    os.chdir(directory)
    counter_packages = 1
    for file in glob.glob("*" + config["COMMON"]["file_extension"]):
        package_name = file.split(".")[0]
        package_description = ""
        with open(file, "r") as open_file:
            package_info = str(open_file.readline())
            if package_info[0] == "#":
                package_description, package_url = get_package_info(
                    package_info)
            else:
                package_description = package_url = package_name
        if file in ignore_file:
            print("File {} ignored".format(file))
        else:
            packages_loaded[counter_packages] = [
                package_name,
                package_description,
                package_url,
                str(directory + "/" + file)
            ]
            counter_packages += 1
    os.chdir(config["COMMON"]["yapi_dir"])
    return packages_loaded


def make_bin_from_packages(packages_list, file_name="packages.bin"):
    """Create binary file from list.

    Arguments:
    packages_list -- dictionary of packages to cache
    *ignore_file -- string name of files to ignore
    """
    import pickle
    with open(file_name, "wb") as file:
        pickle.dump(packages_list, file, protocol=0)
        print("[LOG] {} Packages store into {}".format(
            len(packages_list), file_name))


def get_packages(directory, ignore_file=[]):
    """Get packages.

    Arguments:
    directory -- directory where packages are
    *test -- specification of file using in test
    """
    import os
    from_file = directory.split(sep="/")[-1].strip("/") + ".bin"
    if os.path.exists(from_file):
        return load_packages_from_file(from_file)
    else:
        if os.path.exists(directory):
            packages = load_packages_from_directory(directory, ignore_file)
            make_bin_from_packages(packages, from_file)
            return packages
        else:
            print("[LOG] {} directory not found".format(directory))
    return {}


def delete_cache(directory):
    """Delete binary packages cache.

    Arguments:
    directory -- delete the cache of this directory
    """
    import os
    try:
        cache_file = directory.split(sep="/")[-1].strip("/")
        os.chdir(directory.rstrip("/" + cache_file + "/"))
        os.remove(cache_file + ".bin")
        return True
    except Exception:
        return False
