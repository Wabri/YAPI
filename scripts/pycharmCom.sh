# Pycharm Community edition - https://www.jetbrains.com/pycharm/
cd ~
wget -O pycharm.tar.gz https://download.jetbrains.com/python/pycharm-community-2018.2.4.tar.gz
tar zxvf pycharm.tar.gz
sudo rm -r pycharm.tar.gz
mv pycharm-* pycharm
echo "You can find Pycharm in your home folder"
echo "To use you can simply run pycharm.sh in pycharm/bin folder"
