# YAPI - Yet Another Package Installer

YAPI is a simple package installer made in python. it's free, open-source, and works on Debian distributions (some scripts even in MacOS). The project is currently in an early stage of development.

****

## Badges

| Build status | LICENCE |
|----------|---------------|
| [![Build Status](https://travis-ci.org/Wabri/YAPI.svg?branch=master)](https://travis-ci.org/Wabri/YAPI) | [![license](https://img.shields.io/badge/LICENCE-GPL--3.0-green.svg)](LICENSE) | |

****

## Features

Current Packages Supported:
<!--readme_update start -->
- Test - Description of package - https://github.com/Wabri/YAPI
- Playerctl - Playerctl command-line controller and library - https://github.com/acrisci/playerctl
- Discord - Discord chat vocale e testuale - https://discordapp.com/
- Mailspring - The best mail client - https://getmailspring.com/
- Spotify - Spotify client music for all - https://www.spotify.com
- Gitkraken - GitKraken Git Client and Glo Boards to build epic software - https://www.gitkraken.com/
- Googlechrome - Google Chrome browser - https://www.google.it/chrome/
- Rambox - Rambox workspace browser - https://rambox.pro
- Pycharmcom - Pycharm Community edition - https://www.jetbrains.com/pycharm/
- Skype - Skype for linux instant chat and VoIP - https://www.skype.com/
- Nvidiadriver - NVIDIA driver support of Geforce 4xx and higher GPUs - https://wiki.debian.org/NvidiaGraphicsDrivers
- Light - Light GNU/Linux application to control backlights - http://haikarainen.github.io/light
- Oh-my-zsh - zsh + oh-my-zsh - https://ohmyz.sh/
- Virtualbox - VirtualBox is a general-purpose full virtualizer for x86 hardware - https://www.virtualbox.org
- Ideacom - IntelliJ IDEA Community edition - https://www.jetbrains.com/idea/
- Steam - Steam ultimate entertainment platform - https://store.steampowered.com/about
- Dropbox - Dropbox cloud storage - https://www.dropbox.com/
- Eclipseinstaller - Eclipse IDE installer - https://www.eclipse.org/
- Atom - Atom Text Editor - https://atom.io/
- Nodejs - NodeJs JavaScript runtime - https://github.com/nodesource/distributions#installation-instructions
- Javajdk11 - Java jdk 11 with path setup - https://www.oracle.com/technetwork/java/javase/downloads/index.html
<!--readme_update end -->

****

## Install

To use YAPI you need to clone this repository:

    git clone https://github.com/Wabri/YAPI.git

Then run the yapi.py python script:

    python3 yapi.py

Or use the short method with the name of the package you want to install:

    python3 yapi.py install <package_name>

****

## Usage without clone or download

If you dont want to download YAPI but you need one of the packages, you can use the package manager to install a package with this command:

    curl -sL <https://raw.githubusercontent.com/Wabri/YAPI/master/scripts/<package_name>.sh | sudo bash -

****

## How to add new script

There is a format for the install scripts:

    # <description of package> - <reference site of package>
    <bash commands>

An example of this format is [test.sh](scripts/test.sh):

    # Description of package - https://github.com/Wabri/YAPI
    echo "Hello world!"

If you want to add one script you **need** to mantain this standard. This is because the packages list on yapi.py is generated with this information, taken directly from the scripts.

****

## How To Contribute

Contributions are always welcome, either reporting issues/bugs or forking the repository and then issuing pull requests when you have completed some additional coding that you feel will be beneficial to the main project. If you are interested in contributing in a more dedicated capacity, then please contact me.

****

## License

YAPI source code is released under the GNU General Public License v3.0. Please see [LICENSE](LICENSE) for complete licensing information.

****

## Contributors:

[Wabri](https://github.com/Wabri), [IanDuncanT](https://github.com/IanDuncanT)
