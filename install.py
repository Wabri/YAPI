from configparser import ConfigParser
from configparser import ExtendedInterpolation
import glob
import os
import subprocess

config = ConfigParser(interpolation=ExtendedInterpolation())
config.read("config.ini")

config.set("COMMON", "yapi_dir", str(
    os.path.realpath(__file__)).rstrip("/install.py"))

with open("config.ini", "w") as configfile:
    config.write(configfile)

print("Choose the language:")
language_pack = dict()
counter = 0
for file in glob.glob(config["COMMON"]["language_dir"] + "/*.ini"):
    language = ConfigParser()
    language.read(file)
    language_pack[counter] = [language["DEFAULT"]["description"],
                              file.split(sep="/")[-1].split(sep=".")[0]]
    print("\t {}) {} - {}".format(counter,
                                  language_pack[counter][0],
                                  language_pack[counter][1]))
    counter += 1
choose = -1
while (choose > counter or choose < 0):
    try:
        choose = int(input("Write the number: > "))
        if 0 < choose < counter:
            break
    except:
        choose = -1
    print("You need to choose one of this languages:")
    for language_number in language_pack:
        print("\t {}) {} - {}".format(language_number,
                                      language_pack[language_number][0],
                                      language_pack[language_number][1]))

config.set("COMMON", "language", language_pack[choose][1])

with open("config.ini", "w") as configfile:
    config.write(configfile)

if config["INSTALL"]["want_soft_link"] == "yes":
    soft_link = "sudo ln -s " + \
        config["COMMON"]["yapi_dir"] + "/yapi.sh" + \
        config["INSTALL"]["soft_link"] + "/yapi"
    output = subprocess.call(
        soft_link, stderr=subprocess.STDOUT, shell=True)
