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
    with open(packages_binary_file_store, "wb") as packages_binary:
        pickle.dump(packages, packages_binary,
                    protocol=0)
        print("Packages store into {}".format(packages_binary_file_store))

start_update = True
continue_read = True
readme_updated = list()
with open("README.md", "r") as readme:
    for line in readme.readlines():
        if not continue_read:
            if start_update:
                for package_counter in packages:
                    readme_updated.append(
                        str("- " + packages[package_counter][0].capitalize() +
                            " - " + packages[package_counter][1]))
                start_update = False
            if line == "<!--readme_update end -->\n":
                readme_updated.append(line)
                continue_read = True
        else:
            continue_read = line != "<!--readme_update start -->\n"
            readme_updated.append(line)

with open("README.tmp", "w") as readme:
    for line in readme_updated:
        print(line.strip("\n"), file=readme)
