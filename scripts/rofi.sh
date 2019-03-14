# Rofi a window switcher, application launcher and dmenu replacement - https://github.com/DaveDavenport/rofi
sudo apt install libpango-1.0-0 libpangocairo-1.0-0 libcairo2 libglib2.0-0 librsvg2-2 libstartup-notification0 libxkbcommon0 libxkbcommon-x11-0 libxcb libxcb-util0 libxcb-ewmh2 libxcb-icccm4 libxcb-xrm0 bison flex librsvg-2-2
wget -O rofi.tar.gz https://github.com/DaveDavenport/rofi/releases/download/1.5.2/rofi-1.5.2.tar.gz
tar zxvf rofi.tar.gz
cd rofi-*
./configure
make
sudo make install
cd ../
rm rofi*
