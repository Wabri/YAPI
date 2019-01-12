import os
from configparser import ConfigParser
from configparser import ExtendedInterpolation

config = ConfigParser(interpolation=ExtendedInterpolation())
config.read("config.ini")

config.set("COMMON", "yapi_dir", str(
    os.path.realpath(__file__)).strip("installer.py"))

with open("config.ini", "w") as configfile:
    config.write(configfile)
