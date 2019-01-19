from configparser import ConfigParser
from configparser import ExtendedInterpolation
import glob
import os
import subprocess
import sys

config = ConfigParser(interpolation=ExtendedInterpolation())
real_config_path = os.path.realpath(
    __file__).rstrip("install.py") + "config.ini"
config.read(real_config_path)

yapi_real_path = os.path.realpath(__file__).rstrip("/install.py")
config.set("COMMON", "yapi_dir", str(yapi_real_path))

with open(real_config_path, "w") as configfile:
    config.write(configfile)

arguments = dict()
for arg in sys.argv[1:]:
    argument = tuple(arg.split(sep="="))
    arguments[argument[0]] = argument[1]

lang = ""
if "--lang" in arguments:
    lang = arguments["--lang"]
    lang_path_exists = os.path.exists(
        config["COMMON"]["language_dir"] + "/" + lang + ".ini")
    if not lang_path_exists:
        print("The language {} not exists".format(lang))
        lang = "en"
        print("Set default language: {}".format(lang))
else:
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
            if 0 <= choose < counter:
                break
        except Exception:
            choose = -1
        print("You need to choose one of this languages:")
        for language_number in language_pack:
            print("\t {}) {} - {}".format(language_number,
                                          language_pack[language_number][0],
                                          language_pack[language_number][1]))
    lang = language_pack[choose][1]

config.set("COMMON", "language", lang)

with open(real_config_path, "w") as configfile:
    config.write(configfile)

want_soft_link = "no"
if "--softlink" in arguments:
    want_soft_link = arguments["--softlink"]
    if want_soft_link == "yes":
        soft_link = "sudo ln -s " + \
            config["COMMON"]["yapi_dir"] + "/yapi.sh" + \
            config["INSTALL"]["soft_link"] + "/yapi"
        output = subprocess.call(
            soft_link, stderr=subprocess.STDOUT, shell=True)
else:
    if config["INSTALL"]["want_soft_link"] == "yes":
        want_soft_link = "yes"
        soft_link = "sudo ln -s " + \
            config["COMMON"]["yapi_dir"] + "/yapi.sh" + \
            config["INSTALL"]["soft_link"] + "/yapi"
        output = subprocess.call(
            soft_link, stderr=subprocess.STDOUT, shell=True)

config.set("INSTALL", "want_soft_link", want_soft_link)

with open(real_config_path, "w") as configfile:
    config.write(configfile)
