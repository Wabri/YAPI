# Install YAPI from Github - https://github.com/Wabri/YAPI
git clone https://github.com/Wabri/YAPI.git --depth 1
sudo rm -r YAPI/.git YAPI/.gitignore YAPI/.travis.yml YAPI/readme_updater.py
./YAPI/yapi.sh help
cd YAPI
