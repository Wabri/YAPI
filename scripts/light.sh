# Light GNU/Linux application to control backlights - http://haikarainen.github.io/light
wget https://github.com/haikarainen/light/releases/download/v1.2/light-1.2.tar.gz
sudo tar xvzf light-1.2.tar.gz
cd light-1.2/
./configure
make
sudo make install
cd ../
rm -r light-1.2 light-1.2.tar.gz
