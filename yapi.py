import subprocess
import glob
from configparser import ConfigParser
from modules.configuration.config_extractor import get_configuration
import os

config = get_configuration()
print("-"*79)
print("Configuration")
print("Language: {}".format(config["COMMON"]["language"]))
print("Yapi directory: {}".format(config["COMMON"]["yapi_dir"]))
print("Keep cache: {}".format(config["CACHE"]["keep_cache"]))
print("-"*79)
while True:
    print("What do you want to do?")
    print("1 - Install packages")
    print("2 - Change configuration")
    print("0 - Exit")
    choose = (int)(input("    -> "))
    print("-"*79)
    if choose == 0:
        print("Bye, Bye")
        exit()
    elif choose == 1:
        yapi_script = ConfigParser()
        directory = (str)(config["PACKAGES"]["packages_path"])

        # Start Method Get packages
        # this print need to be the init of output string
        os.chdir(directory)
        names_script = list()
        categories = dict()
        for file in glob.glob("*"+".yp"):
            yapi_script.read(file)
            class_script = yapi_script["DEFAULT"]["class"]
            if class_script not in categories.keys():
                categories[class_script] = list()
            if class_script != "ignore":
                names_script.append((str)(file))
                categories[class_script].append(len(names_script))
            else:
                categories[class_script].append((str)(file))
        # print(names_script)
        # print(categories)
        # this method return 2 object: the list of the names and
        # the list of the categories.
        # return names_script, categories
        # End method get packages

        # Categories
        print("Choose one of this categories")
        print("0 - Return to main")
        num_category = list()
        num_category.append("Return to main menu")
        for category in categories.keys():
            if category != "ignore":
                num_category.append(category)
                print("{} - {}".format(len(num_category)-1, category))
        choose = input("    -> ")
        if (int)(choose) <= len(num_category):
            if (int)(choose) == 0:
                print("Return to menu...")
            else:
                print("-"*79)

                # Packages
                print("This is the packages of category {}".format(
                    num_category[(int)(choose)]))
                print("0 - Return to menu")
                for num_name in categories[num_category[(int)(choose)]]:
                    print("{} - {}".format(num_name, names_script[num_name-1]))
                choose = input("    -> ")
                if (int)(choose) != 0:
                    yapi_script.read(names_script[(int)(choose)-1])

                    # package infos
                    print("-"*79)
                    print("Infos about {}".format(
                        yapi_script["DEFAULT"]["name"].capitalize()))
                    print("Description: {}".format(
                        yapi_script["DEFAULT"]["description"]))
                    print("Link reference: {}".format(
                        yapi_script["DEFAULT"]["url"]))
                    print("Is install: {}".format(
                        yapi_script["Common"]["installed"]))
                    print("What do you want to do?")
                    print("0 - return to packages chooose")
                    print("1 - install")
                    print("2 - go to link")
                    choose = input("    -> ")

                    # install package
                    if (int)(choose) == 1:
                        print("-"*79)
                        output = subprocess.call(
                            yapi_script["Script"]["install"], shell=True, stderr=subprocess.STDOUT)
                        if output == 0:
                            print("ok")
                        else:
                            print("not ok")

                    # url
                    elif (int)(choose) == 2:
                        print("You are now redirected to {}".format(
                            yapi_script["DEFAULT"]["url"]))
                        # this need to return to the menu of package
        print("-"*79)
    elif choose == 2:
        print("not yet implemented")
        print("-"*79)
