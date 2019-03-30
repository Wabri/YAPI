# YAPI - Yet Another Package Installer

[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source-150x25.png?v=103)](https://github.com/YetAnotherPackageInstaller/YAPI)


[![Build Status](https://travis-ci.org/YetAnotherPackageInstaller/YAPI.svg?branch=master)](https://travis-ci.org/YetAnotherPackageInstaller/YAPI)
[![Issues](https://img.shields.io/github/issues/YetAnotherPackageInstaller/YAPI.svg)](https://github.com/YetAnotherPackageInstaller/YAPI/issues)
[![Stars](https://img.shields.io/github/stars/YetAnotherPackageInstaller/YAPI.svg)](https://github.com/YetAnotherPackageInstaller/YAPI/stargazers)
[![Forks](https://img.shields.io/github/forks/YetAnotherPackageInstaller/YAPI.svg)](https://github.com/YetAnotherPackageInstaller/YAPI/network)
[![GitHub contributors](https://img.shields.io/github/contributors/YetAnotherPackageInstaller/YAPI.svg?maxAge=2592000)]()
<!-- [![Downloads](https://img.shields.io/github/downloads/YetAnotherPackageInstaller/YAPI/total.svg)](https://github.com/YetAnotherPackageInstaller/YAPI/releases) -->

[![GitHub license](https://img.shields.io/github/license/YetAnotherPackageInstaller/YAPI.svg)](https://github.com/YetAnotherPackageInstaller/YAPI/blob/master/LICENSE)


YAPI is a simple package installer made in python for version 3.x. It's free, open-source, and works on Debian distributions. The project is currently in an early stage of development.

****

## Install
To install YAPI you can use wget:

    wget https://raw.githubusercontent.com/YetAnotherPackageInstaller/YAPI/install.sh -O - | sudo bash -

This script clones the repository, delete all the useless files and set up basic arguments of configuration.

You can also clone the repository, edit the configuration by yourself (wiki page are not available yet) and run

    ./install.sh

****

## Usage

To use YAPI, run the yapi.sh shell script:

    ./yapi.sh

Or use the short method with the name of the package you want to install:

    ./yapi.sh install <package_name>

To call yapi like this:

    yapi <command> <package>

You need to set in the [config.ini](config.ini) file the argument "want_soft_link =" with "yes" value and run again install.py with this command:

    python3 install.py

****

## Help

<!--readme_update start help -->
To run yapi with the terminal question installer:

 	yapi console

To pull the newest yapi version from github:

 	yapi update

To get information about yapi:

 	yapi help

To install one of the packages:

 	yapi install <package_to_install>

To recreate the cache:

 	yapi cache
<!--readme_update end help -->

****

## Usage without clone or download

If you dont want to download YAPI but you need one of the packages, you can use the package manager to install a package with this command:

    wget https://raw.githubusercontent.com/YetAnotherPackageInstaller/YAPI/master/scripts/<package_name>.sh -O - | sudo bash -

****

## How to add new script

There is a format for the install scripts:

    # <description of package> - <reference site of package>
    <bash commands>

An example of this format is [test.sh](scripts/test.sh):

    # Description of package - https://github.com/YetAnotherPackageInstaller/YAPI
    echo "Hello world!"

If you want to add one script you **need** to mantain this standard. This is because the packages list on yapi.py is generated with this information, taken directly from the scripts.

****

## How To Contribute

Contributions are always welcome, either reporting issues/bugs or forking the repository and then issuing pull requests when you have completed some additional coding that you feel will be beneficial to the main project. If you are interested in contributing in a more dedicated capacity, then please contact us.

****

## License

YAPI source code is released under the GNU General Public License v3.0. Please see [LICENSE](LICENSE) for complete licensing information.

****

## Contributors:

[![Wabri](https://avatars3.githubusercontent.com/u/12409541?s=50&v=4)](https://github.com/Wabri), [![IanDuncanT](https://avatars1.githubusercontent.com/u/39711921?s=50&v=4)](https://github.com/IanDuncanT)
