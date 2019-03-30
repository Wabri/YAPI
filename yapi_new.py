import subprocess
import glob
from configparser import ConfigParser
from modules.configuration.config_extractor import get_configuration
import os

config = get_configuration()
print("-----------------------------------------------------------------------------")
print("Configuration")
print("Language: {}".format(config["COMMON"]["language"]))
print("Yapi directory: {}".format(config["COMMON"]["yapi_dir"]))
print("Keep cache: {}".format(config["CACHE"]["keep_cache"]))
print("-----------------------------------------------------------------------------")
while True:
    print("What do you want to do?")
    print("0 - exit")
    print("1 - list of packages")
    print("2 - change configuration")
    choose = (int)(input("    -> "))
    print("-----------------------------------------------------------------------------")
    if choose == 0:
        print("Bye, Bye")
        exit()
    elif choose == 1:
        # Start Method Get packages
        yapi_script = ConfigParser()
        list_script = list()
        directory = (str)(config["PACKAGES"]["packages_path"])
        os.chdir(directory)
        # this print need to be the init of output string
        print("0 - return to main menu")
        for file in glob.glob("*"+".yp"):
            yapi_script.read(file)
            if yapi_script["DEFAULT"]["class"] != "ignore":
                list_script.append((str)(file))
                # This will be the string return of the method
                print("{} - {}".format(len(list_script),
                                       yapi_script["DEFAULT"]["name"]))
            else:
                print("File {} ignore!".format(yapi_script["DEFAULT"]["name"]))
        print(list_script)
        # this method return 2 object: the list of the script and the string output
        # return list_script, output
        # End method get packages
        choose = input("    -> ")
        if (int)(choose) == 0:
            print("Return to menu...")
            print("-----------------------------------------------------------------------------")
        else:
            yapi_script.read(list_script[(int)(choose)-1])
            output = subprocess.call(
            yapi_script["Script"]["install"], shell=True, stderr=subprocess.STDOUT)
            if output == 0:
                print("ok")
            else:
                print("not ok")
            print("-----------------------------------------------------------------------------")
    elif choose == 2:
        print("not yet implemented")
        print("-----------------------------------------------------------------------------")
