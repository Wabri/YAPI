# IntelliJ IDEA Community edition - https://www.jetbrains.com/idea/
cd ~
wget -O idea.tar.gz https://download.jetbrains.com/idea/ideaIC-2018.2.5.tar.gz
tar zxvf idea.tar.gz
sudo rm -r idea.tar.gz
mv idea-* idea
cd idea/bin
sudo ln -s ~/idea/bin/idea.sh /usr/local/bin/idea
echo "You can now run IntelliJ IDEA by run command idea"
