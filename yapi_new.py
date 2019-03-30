import subprocess
import glob
from configparser import ConfigParser
from modules.configuration.config_extractor import get_configuration
import os

config = get_configuration()
yapi_script = ConfigParser()
list_script = list()
directory = (str)(config["PACKAGES"]["packages_path"])
os.chdir(directory)
for file in glob.glob("*"+".yp"):
    yapi_script.read(file)
    if yapi_script["DEFAULT"]["class"] != "ignore":
        list_script.append((str)(file))
        print("{} - {}".format(len(list_script),
                               yapi_script["DEFAULT"]["name"]))
    else:
        print("File {} ignore!".format(yapi_script["DEFAULT"]["name"]))
print(list_script)
choose = input("Put number here -> ")
yapi_script.read(list_script[(int)(choose)-1])
output = subprocess.call(
    yapi_script["Script"]["install"], shell=True, stderr=subprocess.STDOUT)
if output == 0:
    print("ok")
else:
    print("not ok")
