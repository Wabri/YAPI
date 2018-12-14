# Install YAPI from Github - https://github.com/Wabri/YAPI
git clone https://github.com/Wabri/YAPI.git --depth 1
cd YAPI
sudo rm -r .git .gitignore .travis.yml readme_updater.py
./yapi.sh help
