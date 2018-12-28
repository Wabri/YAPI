cd ~
git clone https://github.com/YetAnotherPackageInstaller/YAPI.git --depth 1
cd YAPI
sudo rm -r .git* .travis.yml install.sh readme_updater.py
sudo ln -s ~/YAPI/yapi.sh /usr/local/bin/yapi
