# Steam ultimate entertainment platform - https://store.steampowered.com/about

# add architecture for steam installer
sudo dpkg --add-architecture i386
sudo apt install gdebi-core libgl1-mesa-dri:i386 libgl1-mesa-glx:i386
sudo apt update
sudo apt upgrade

#installer steam
wget -O steam.deb http://media.steampowered.com/client/installer/steam.deb
sudo gdebi steam.deb
rm -r steam.deb
