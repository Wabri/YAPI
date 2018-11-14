# YAPI - Yet Another Package Installer

YAPI is a simple package installer made in python. it's free, open-source, and works on Debian distributions (some scripts even in MacOS). The project is currently in an early stage of development.

****

## Status

| Linux |
|-------|
|[![Build Status](https://travis-ci.org/Wabri/YAPI.svg?branch=master)](https://travis-ci.org/Wabri/YAPI)|

****

## Features

Current Packages Supported:
-   Atom
-   Discord
-   Dropbox
-   Eclipse
-   Gitkraken
-   Google Chrome
-   Java jdk 11 (Includes home path)
-   Light
-   Node JS
-   Nvidia Drivers
-   Oh My Zsh
-   Playerctl
-   Rambox
-   Skype
-   Steam
-   VirtualBox
-   Pycharm Community edition
-   IntelliJ Idea Community edition

****

## Install

To use YAPI you need to clone this repository:

    git clone https://github.com/Wabri/YAPI.git`

Then run the yapi.py python script:

    python3 yapi.py

Or use the short method with the name of the package you want to install:

    python3 yapi.py install <package_name>

****

## Usage without clone or download

If you dont want to download YAPI but you need one of the package, you can use it anyway with this command:

    curl -sL <https://raw.githubusercontent.com/Wabri/YAPI/master/scripts/<package_name>.sh | sudo bash -

****

## How to add new script

There is a sort of standard for the scripts:

    # <description of package> - <reference site of package>
    <bash commands>

Something like [test.sh](scripts/test.sh):

    # Description of package - https://github.com/Wabri/YAPI
    echo "Hello world!"

So if you want to add one script you have to mantain this standard. This is because the packages list on yapi.py is generated with this information, taken directly from the scripts.

****

## How To Contribute

Contributions are always welcome, either reporting issues/bugs or forking the repository and then issuing pull requests when you have completed some additional coding that you feel will be beneficial to the main project. If you are interested in contributing in a more dedicated capacity, then please contact me.

****

## License

YAPI source code is released under the GNU General Public License v3.0. Please see [LICENSE](LICENSE) for complete licensing information.

****

## Contributors:

[Wabri](https://github.com/Wabri), [IanDuncanT](https://github.com/IanDuncanT)
