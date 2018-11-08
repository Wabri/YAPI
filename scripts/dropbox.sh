# Dropbox cloud storage - https://www.dropbox.com/
wget -O dropbox.deb https://www.dropbox.com/download?dl=packages/ubuntu/dropbox_2015.10.28_amd64.deb
sudo dpkg -i dropbox.deb
rm -r dropbox.deb
dropbox start -i
