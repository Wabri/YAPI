# VirtualBox is a general-purpose full virtualizer for x86 hardware - https://www.virtualbox.org
sudo add-apt-repository "deb http://download.virtualbox.org/virtualbox/debian stretch contrib"
wget https://www.virtualbox.org/download/oracle_vbox_2016.asc
sudo apt-key add oracle_vbox_2016.asc
sudo apt-get update
sudo apt install virtualbox-5.2
rm oracle_vbox_2016.asc
