# Eclipse IDE installer - https://www.eclipse.org/
cd ~
wget -O eclipseInst.tar.gz ftp.fau.de/eclipse/oomph/products/eclipse-inst-linux64.tar.gz
tar zxvf eclipseInst.tar.gz
sudo rm -r eclipseInst.tar.gz
ln -s ~/eclipse-installer/eclipse-inst /usr/local/bin/eclipse-inst
