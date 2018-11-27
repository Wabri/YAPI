import glob
import os
import pickle

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
            package_description = str(open_file.readline())
            if package_description[0] == "#":
                package_description = package_description.strip(
                    "\n").strip("# ")
            else:
                package_description = package_name
            package_url = ""
            precedent_character = ""
            get_url = False
            for character in package_description:
                if not get_url and precedent_character == "-":
                    get_url = character == " "
                    if get_url:
                        continue
                elif get_url:
                    package_url += character
                precedent_character = character
            del precedent_character, get_url
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
                where_is_scripts + file
            ]
            counter_packages += 1
    os.chdir("..")
    with open(packages_binary_file_store, "wb") as packages_binary:
        pickle.dump(packages, packages_binary,
                    protocol=0)
        print("Packages store into {}".format(packages_binary_file_store))

print(packages)
