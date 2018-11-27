# The best mail client - https://getmailspring.com/
wget -O mailspring.deb https://updates.getmailspring.com/download?platform=linuxDeb
sudo dpkg -i mailspring.deb
sudo apt --fix-broken install
rm -r mailspring.deb
